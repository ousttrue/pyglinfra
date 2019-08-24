import glb
import gltftypes

accessor_component_type_map = {
    gltftypes.Accessor_componentType.BYTE: 1,
    gltftypes.Accessor_componentType.SHORT: 2,
    gltftypes.Accessor_componentType.UNSIGNED_BYTE: 1,
    gltftypes.Accessor_componentType.UNSIGNED_SHORT: 2,
    gltftypes.Accessor_componentType.UNSIGNED_INT: 4,
    gltftypes.Accessor_componentType.FLOAT: 4,
}

accessor_type_map = {
    gltftypes.Accessor_type.SCALAR: 1,
    gltftypes.Accessor_type.VEC2: 2,
    gltftypes.Accessor_type.VEC3: 3,
    gltftypes.Accessor_type.VEC4: 4,
    gltftypes.Accessor_type.MAT2: 4,
    gltftypes.Accessor_type.MAT3: 9,
    gltftypes.Accessor_type.MAT4: 16,
}


def get_accessor_stride(accessor: gltftypes.Accessor) -> int:
    return accessor_component_type_map[
        accessor.componentType] * accessor_type_map[accessor.type]


class GltfManipulator:
    def __init__(self, gltf: gltftypes.glTF, bin: bytes) -> None:
        self.gltf = gltf
        self.buffers = [bin]

    def get_bytes_from_bufferview(self, index: int) -> bytes:
        buffer_view = self.gltf.bufferViews[index]
        buffer = self.buffers[buffer_view.buffer]
        return buffer[buffer_view.byteOffset:buffer_view.byteOffset +
                      buffer_view.byteLength]

    def get_bytes_from_accessor(self, index: int) -> bytes:
        accessor = self.gltf.accessors[index]
        data = self.get_bytes_from_bufferview(accessor.bufferView)
        byteslength = get_accessor_stride(accessor) * accessor.count
        return data[accessor.byteOffset:accessor.byteOffset + byteslength]


def load(data: bytes) -> GltfManipulator:
    gltf, bin = glb.parse_glb(data)
    return GltfManipulator(gltf, bin)
