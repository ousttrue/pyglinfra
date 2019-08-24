'''
GLObjects => SceneDescription => Gltf
'''
from typing import List
import gltf
import gltftypes


class Node:
    def __init__(self, name: str) -> None:
        self.name = name

    @staticmethod
    def create(gltf: gltftypes.glTF, node: gltftypes.Node) -> 'Node':
        return Node(node.name)


class SubMesh:
    def __init__(self):
        pass


class Mesh:
    def __init__(self):
        self.indices: bytes = b''
        self.index_count = 0
        self.positions: bytes = b''
        self.texcoords: bytes = b''
        self.normals: bytes = b''
        self.tangents: bytes = b''
        self.joints: bytes = b''
        self.weights: bytes = b''

    def get_vertex_count(self) -> int:
        return len(self.positions) // 12

    def get_attributes(self):
        if self.texcoords: yield '[tex]'
        if self.normals: yield '[nrm]'
        if self.tangents: yield '[tangents]'
        if self.joints and self.weights: yield '[skin]'

    def __repr__(self) -> str:
        return f'{self.get_vertex_count()}{"".join(self.get_attributes())}'


class MeshGroup:
    def __init__(self, name: str) -> None:
        self.name = name
        self.meshes: List[Mesh] = []


class Scene:
    def __init__(self) -> None:
        self.mesh_groups: List[MeshGroup] = []
        # self.images: List[Image] = []
        # self.textures: List[Texture] = []
        # self.maerials: List[Material] = []
        # self.nodes: List[Node] = []

    def load(self, data: gltf.GltfManipulator) -> None:
        for m in data.gltf.meshes:
            group = MeshGroup(m.name)
            for p in m.primitives:
                mesh = Mesh()
                mesh.index_count = data.gltf.accessors[p.indices].count
                mesh.indices = data.get_bytes_from_accessor(p.indices)
                for k, v in p.attributes.items():
                    if k == "POSITION":
                        mesh.positions = data.get_bytes_from_accessor(v)
                    elif k == "NORMAL":
                        mesh.normals = data.get_bytes_from_accessor(v)
                    elif k == "TEXCOORD_0":
                        mesh.texcoords = data.get_bytes_from_accessor(v)
                    elif k == "TANGENT":
                        mesh.tangents = data.get_bytes_from_accessor(v)
                    else:
                        raise Exception(f'unknown {k}')
                group.meshes.append(mesh)

            self.mesh_groups.append(group)
