import struct
import json
from typing import Tuple
try:
    from . import gltftypes
except:
    import gltftypes


class Reader:
    def __init__(self, data: bytes) -> None:
        self.data = data
        self.pos = 0

    def read(self, size) -> bytes:
        result = self.data[self.pos:self.pos + size]
        self.pos += size
        return result

    def read_uint(self):
        result = struct.unpack('I', self.data[self.pos:self.pos + 4])[0]
        self.pos += 4
        return result


def parse_glb(data: bytes) -> Tuple[gltftypes.glTF, bytes]:
    reader = Reader(data)
    magic = reader.read(4)
    if magic != b'glTF':
        raise Exception(f'magic not found: #{magic}')

    version = reader.read_uint()
    if version != 2:
        raise Exception(f'version:#{version} is not 2')

    size = reader.read_uint()
    size -= 12

    json_str = None
    body = None
    while size > 0:
        # print(size)

        chunk_size = reader.read_uint()
        size -= 4

        chunk_type = reader.read(4)
        size -= 4

        chunk_data = reader.read(chunk_size)
        size -= chunk_size

        if chunk_type == b'BIN\x00':
            body = chunk_data
        elif chunk_type == b'JSON':
            json_str = chunk_data
        else:
            raise Exception(f'unknown chunk_type: {chunk_type}')

    if not json_str:
        raise Exception("no json chunk")
    if not body:
        raise Exception("no body chunk")

    # print(json_str)
    gltf = gltftypes.from_json(json.loads(json_str))
    return gltf, body
