from OpenGL.GL import *  # pylint: disable=W0614, W0622, W0401
from OpenGL.GLU import *  # pylint: disable=W0614, W0622, W0401
from typing import Dict
import scenedescription
import ctypes
from typing import List, Tuple

VERTICES = (
    -1.0,
    -1.0,  #v0
    1.0,
    -1.0,  #v1
    0.0,
    1.0  #v2
)

VS = '''
#version 330
in vec2 aPosition;
void main ()
{
    gl_Position = vec4(aPosition, 0.5, 1);
}
'''

FS = '''
#version 330
out vec4 FragColor;
void main()
{
    FragColor = vec4(1, 1, 1, 1);
}
'''


class VBO:
    def __init__(self) -> None:
        self.vbo = glGenBuffers(1)
        self.component_count = 0  # Vec2, Vec3, Vec4 などの2, 3, 4
        self.vertex_count = 0

    def __del__(self) -> None:
        glDeleteBuffers(1, [self.vbo])

    def bind(self) -> None:
        glBindBuffer(GL_ARRAY_BUFFER, self.vbo)

    def unbind(self) -> None:
        glBindBuffer(GL_ARRAY_BUFFER, 0)

    def set_vertex_attribute(self, component_count: int, data: bytes) -> None:
        ''' float2, 3, 4'''
        self.component_count = component_count
        stride = 4 * self.component_count
        self.vertex_count = len(data) // stride
        self.bind()
        glBufferData(GL_ARRAY_BUFFER, len(data), data, GL_STATIC_DRAW)

    def set_slot(self, slot: int) -> None:
        self.bind()
        glEnableVertexAttribArray(slot)
        glVertexAttribPointer(slot, self.component_count, GL_FLOAT, GL_FALSE,
                              0, None)

    def draw(self) -> None:
        glDrawArrays(GL_TRIANGLES, 0, self.vertex_count)


class IBO:
    def __init__(self) -> None:
        self.vbo = glGenBuffers(1)
        self.index_count = 0
        self.index_type = 0

    def __del__(self) -> None:
        glDeleteBuffers(1, [self.vbo])

    def bind(self) -> None:
        glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, self.vbo)

    def unbind(self) -> None:
        glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, 0)

    def set_indices(self, data: bytes, index_count: int) -> None:
        self.index_count = index_count
        self.bind()
        stride = len(data) // index_count
        if stride == 1:
            raise Exception("not implemented")
        elif stride == 2:
            self.index_type = GL_UNSIGNED_SHORT
        elif stride ==4:
            self.index_type = GL_UNSIGNED_INT
        glBufferData(GL_ELEMENT_ARRAY_BUFFER, len(data), data, GL_STATIC_DRAW)

    def draw(self) -> None:
        glDrawElements(GL_TRIANGLES, self.index_count, self.index_type, None)


def load_shader(src: str, shader_type: int) -> int:
    shader = glCreateShader(shader_type)
    glShaderSource(shader, src)
    glCompileShader(shader)
    error = glGetShaderiv(shader, GL_COMPILE_STATUS)
    if error != GL_TRUE:
        info = glGetShaderInfoLog(shader)
        glDeleteShader(shader)
        raise Exception(info)
    return shader


class Shader:
    def __init__(self) -> None:
        self.program = glCreateProgram()

    def __del__(self) -> None:
        glDeleteProgram(self.program)

    def compile(self, vs_src: str, fs_src: str) -> None:
        vs = load_shader(vs_src, GL_VERTEX_SHADER)
        if not vs:
            return
        fs = load_shader(fs_src, GL_FRAGMENT_SHADER)
        if not fs:
            return
        glAttachShader(self.program, vs)
        glAttachShader(self.program, fs)
        glLinkProgram(self.program)
        error = glGetProgramiv(self.program, GL_LINK_STATUS)
        glDeleteShader(vs)
        glDeleteShader(fs)
        if error != GL_TRUE:
            info = glGetShaderInfoLog(self.program)
            raise Exception(info)

    def use(self):
        glUseProgram(self.program)

    def unuse(self):
        glUseProgram(0)


class Model:
    def __init__(self) -> None:
        self.positions = VBO()
        self.indices: IBO = None
        self.shader = Shader()

    def set_vertices(self, component_count: int, data: bytes) -> None:
        self.positions.set_vertex_attribute(component_count, data)

    def set_indices(self, data: bytes, index_count: int) -> None:
        self.indices = IBO()
        self.indices.set_indices(data, index_count)

    def draw(self) -> None:
        self.shader.use()
        if self.indices:
            self.positions.set_slot(0)
            self.indices.bind()
            self.indices.draw()
        else:
            self.positions.set_slot(0)
            self.positions.draw()


def create_triangle():
    m = Model()
    m.shader.compile(VS, FS)
    m.set_vertices(2, VERTICES)
    m.set_indices([0, 1, 2])

    return m


class Renderer:
    def __init__(self):
        self.drawable_map: Dict[scenedescription.Mesh, Model] = {}

    def get_drawable(self, mesh: scenedescription.Mesh) -> Model:
        d = self.drawable_map.get(mesh)
        if not d:
            print(glGetString(GL_VENDOR))
            print(glGetString(GL_VERSION))
            print(glGetString(GL_SHADING_LANGUAGE_VERSION))
            print(glGetString(GL_RENDERER))
            # d = create_triangle()
            d = Model()
            d.shader.compile(VS, FS)
            d.set_vertices(3, mesh.positions)
            d.set_indices(mesh.indices, mesh.index_count)
            self.drawable_map[mesh] = d
        return d

    def draw(self, scene: scenedescription.Scene) -> None:
        for g in scene.mesh_groups:
            for m in g.meshes:
                d = self.get_drawable(m)
                d.draw()
