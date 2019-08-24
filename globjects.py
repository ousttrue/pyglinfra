from OpenGL.GL import *  # pylint: disable=W0614, W0622, W0401
from OpenGL.GLU import *  # pylint: disable=W0614, W0622, W0401


class TriangleLegacy:
    def draw(self) -> None:
        glBegin(GL_TRIANGLES)
        glVertex(-1.0, -1.0)
        glVertex(1.0, -1.0)
        glVertex(0.0, 1.0)
        glEnd()


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

    def set_data(self, component_count: int,
                 values: List[Tuple[float, float]]) -> None:
        self.component_count = 2
        self.vertex_count = int(len(values) / self.component_count)
        self.bind()
        bytelength = ctypes.sizeof(ctypes.c_float) * len(values)
        typedarray = (ctypes.c_float * len(values))(*values)
        glBufferData(GL_ARRAY_BUFFER, bytelength, typedarray, GL_STATIC_DRAW)

    def draw(self) -> None:
        self.bind()
        slot = 0
        glEnableVertexAttribArray(slot)
        glVertexAttribPointer(slot, self.component_count, GL_FLOAT, GL_FALSE,
                              0, None)
        glDrawArrays(GL_TRIANGLES, 0, self.vertex_count)


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
        try:
            self.use()
        except OpenGL.error.GLError as ex:
            if ex.description:
                error = ex.description.decode('utf8')
                print(error)

    def use(self):
        glUseProgram(self.program)

    def unuse(self):
        glUseProgram(0)


class Model:
    def __init__(self) -> None:
        self.positions = VBO()
        self.shader = Shader()

    def set_vertices(self, component_count: int,
                     vertices: List[float]) -> None:
        self.positions.set_data(component_count, vertices)

    def draw(self) -> None:
        self.shader.use()
        self.positions.draw()


def create_triangle():
    print(glGetString(GL_VENDOR))
    print(glGetString(GL_VERSION))
    print(glGetString(GL_SHADING_LANGUAGE_VERSION))
    print(glGetString(GL_RENDERER))

    #m = TriangleLegacy()
    m = Model()
    m.shader.compile(VS, FS)
    m.set_vertices(2, VERTICES)

    return m
