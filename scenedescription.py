'''
GLObjects => SceneDescription => Gltf
'''
from typing import List
import gltftypes


class Node:
    def __init__(self, name: str) -> None:
        self.name = name

    @staticmethod
    def create(gltf: gltftypes.glTF, node: gltftypes.Node) -> 'Node':
        return Node(node.name)


class Scene:
    def __init__(self) -> None:
        pass
        # self.images: List[Image] = []
        # self.textures: List[Texture] = []
        # self.maerials: List[Material] = []
        # self.mesh: List[Mesh] = []
        # self.nodes: List[Node] = []

    def load(self, gltf: gltftypes.glTF, bin: bytes) -> None:
        pass