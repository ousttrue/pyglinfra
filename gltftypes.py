import struct
from typing import Dict, Any, List, Optional
from enum import Enum


class Accessor_componentType(Enum):
    """The datatype of components in the attribute."""
    BYTE = 5120
    UNSIGNED_BYTE = 5121
    SHORT = 5122
    UNSIGNED_SHORT = 5123
    UNSIGNED_INT = 5125
    FLOAT = 5126


class Accessor_type(Enum):
    """Specifies if the attribute is a scalar, vector, or matrix."""
    SCALAR = "SCALAR"
    VEC2 = "VEC2"
    VEC3 = "VEC3"
    VEC4 = "VEC4"
    MAT2 = "MAT2"
    MAT3 = "MAT3"
    MAT4 = "MAT4"


class AccessorSparseIndices_componentType(Enum):
    """The indices data type."""
    UNSIGNED_BYTE = 5121
    UNSIGNED_SHORT = 5123
    UNSIGNED_INT = 5125


class AccessorSparseIndices:
    """Index array of size `count` that points to those accessor attributes that deviate from their initialization value. Indices must strictly increase."""

    def __init__(self, js: dict = None)->None:
        self.js: dict = js
        self.extensions: Dict[str, Any] = {}
        """Dictionary object with extension-specific objects."""
        if (js and "extensions" in js):
            self.extensions: Dict[str, Any] = js["extensions"]

        self.extras: Dict[str, Any] = {}
        """Application-specific data."""
        if (js and "extras" in js):
            self.extras: Dict[str, Any] = js["extras"]

        self.bufferView: int = -1
        """The index of the bufferView with sparse indices. Referenced bufferView can't have ARRAY_BUFFER or ELEMENT_ARRAY_BUFFER target."""
        if (js and "bufferView" in js):
            self.bufferView: int = js["bufferView"]

        self.byteOffset: int = 0
        """The offset relative to the start of the bufferView in bytes. Must be aligned."""
        if (js and "byteOffset" in js):
            self.byteOffset: int = js["byteOffset"]

        self.componentType: AccessorSparseIndices_componentType = None
        """The indices data type."""
        if (js and "componentType" in js):
            self.componentType: AccessorSparseIndices_componentType = AccessorSparseIndices_componentType(
                js["componentType"])


class AccessorSparseValues:
    """Array of size `count` times number of components, storing the displaced accessor attributes pointed by `indices`. Substituted values must have the same `componentType` and number of components as the base accessor."""

    def __init__(self, js: dict = None)->None:
        self.js: dict = js
        self.extensions: Dict[str, Any] = {}
        """Dictionary object with extension-specific objects."""
        if (js and "extensions" in js):
            self.extensions: Dict[str, Any] = js["extensions"]

        self.extras: Dict[str, Any] = {}
        """Application-specific data."""
        if (js and "extras" in js):
            self.extras: Dict[str, Any] = js["extras"]

        self.bufferView: int = -1
        """The index of the bufferView with sparse values. Referenced bufferView can't have ARRAY_BUFFER or ELEMENT_ARRAY_BUFFER target."""
        if (js and "bufferView" in js):
            self.bufferView: int = js["bufferView"]

        self.byteOffset: int = 0
        """The offset relative to the start of the bufferView in bytes. Must be aligned."""
        if (js and "byteOffset" in js):
            self.byteOffset: int = js["byteOffset"]


class AccessorSparse:
    """Sparse storage of attributes that deviate from their initialization value."""

    def __init__(self, js: dict = None)->None:
        self.js: dict = js
        self.extensions: Dict[str, Any] = {}
        """Dictionary object with extension-specific objects."""
        if (js and "extensions" in js):
            self.extensions: Dict[str, Any] = js["extensions"]

        self.extras: Dict[str, Any] = {}
        """Application-specific data."""
        if (js and "extras" in js):
            self.extras: Dict[str, Any] = js["extras"]

        self.count: int = -1
        """Number of entries stored in the sparse array."""
        if (js and "count" in js):
            self.count: int = js["count"]

        self.indices: AccessorSparseIndices = None
        """Index array of size `count` that points to those accessor attributes that deviate from their initialization value. Indices must strictly increase."""
        if (js and "indices" in js):
            self.indices: AccessorSparseIndices = AccessorSparseIndices(
                js["indices"])

        self.values: AccessorSparseValues = None
        """Array of size `count` times number of components, storing the displaced accessor attributes pointed by `indices`. Substituted values must have the same `componentType` and number of components as the base accessor."""
        if (js and "values" in js):
            self.values: AccessorSparseValues = AccessorSparseValues(
                js["values"])


class Accessor:
    """A typed view into a bufferView.  A bufferView contains raw binary data.  An accessor provides a typed view into a bufferView or a subset of a bufferView similar to how WebGL's `vertexAttribPointer()` defines an attribute in a buffer."""

    def __init__(self, js: dict = None)->None:
        self.js: dict = js
        self.extensions: Dict[str, Any] = {}
        """Dictionary object with extension-specific objects."""
        if (js and "extensions" in js):
            self.extensions: Dict[str, Any] = js["extensions"]

        self.extras: Dict[str, Any] = {}
        """Application-specific data."""
        if (js and "extras" in js):
            self.extras: Dict[str, Any] = js["extras"]

        self.name: str = ""
        """The user-defined name of this object."""
        if (js and "name" in js):
            self.name: str = js["name"]

        self.bufferView: int = -1
        """The index of the bufferView."""
        if (js and "bufferView" in js):
            self.bufferView: int = js["bufferView"]

        self.byteOffset: int = 0
        """The offset relative to the start of the bufferView in bytes."""
        if (js and "byteOffset" in js):
            self.byteOffset: int = js["byteOffset"]

        self.componentType: Accessor_componentType = None
        """The datatype of components in the attribute."""
        if (js and "componentType" in js):
            self.componentType: Accessor_componentType = Accessor_componentType(
                js["componentType"])

        self.normalized: bool = False
        """Specifies whether integer data values should be normalized."""
        if (js and "normalized" in js):
            self.normalized: bool = js["normalized"]

        self.count: int = -1
        """The number of attributes referenced by this accessor."""
        if (js and "count" in js):
            self.count: int = js["count"]

        self.type: Accessor_type = None
        """Specifies if the attribute is a scalar, vector, or matrix."""
        if (js and "type" in js):
            self.type: Accessor_type = Accessor_type(js["type"])

        self.max: List[float] = []
        if (js and "max" in js):
            self.max: List[float] = js["max"]

        self.min: List[float] = []
        if (js and "min" in js):
            self.min: List[float] = js["min"]

        self.sparse: AccessorSparse = None
        """Sparse storage of attributes that deviate from their initialization value."""
        if (js and "sparse" in js):
            self.sparse: AccessorSparse = AccessorSparse(js["sparse"])


class AnimationChannelTarget_path(Enum):
    """The name of the node's TRS property to modify, or the "weights" of the Morph Targets it instantiates. For the "translation" property, the values that are provided by the sampler are the translation along the x, y, and z axes. For the "rotation" property, the values are a quaternion in the order (x, y, z, w), where w is the scalar. For the "scale" property, the values are the scaling factors along the x, y, and z axes."""
    translation = "translation"
    rotation = "rotation"
    scale = "scale"
    weights = "weights"


class AnimationChannelTarget:
    """The index of the node and TRS property to target."""

    def __init__(self, js: dict = None)->None:
        self.js: dict = js
        self.extensions: Dict[str, Any] = {}
        """Dictionary object with extension-specific objects."""
        if (js and "extensions" in js):
            self.extensions: Dict[str, Any] = js["extensions"]

        self.extras: Dict[str, Any] = {}
        """Application-specific data."""
        if (js and "extras" in js):
            self.extras: Dict[str, Any] = js["extras"]

        self.node: int = -1
        """The index of the node to target."""
        if (js and "node" in js):
            self.node: int = js["node"]

        self.path: AnimationChannelTarget_path = None
        """The name of the node's TRS property to modify, or the "weights" of the Morph Targets it instantiates. For the "translation" property, the values that are provided by the sampler are the translation along the x, y, and z axes. For the "rotation" property, the values are a quaternion in the order (x, y, z, w), where w is the scalar. For the "scale" property, the values are the scaling factors along the x, y, and z axes."""
        if (js and "path" in js):
            self.path: AnimationChannelTarget_path = AnimationChannelTarget_path(
                js["path"])


class AnimationChannel:
    """Targets an animation's sampler at a node's property."""

    def __init__(self, js: dict = None)->None:
        self.js: dict = js
        self.extensions: Dict[str, Any] = {}
        """Dictionary object with extension-specific objects."""
        if (js and "extensions" in js):
            self.extensions: Dict[str, Any] = js["extensions"]

        self.extras: Dict[str, Any] = {}
        """Application-specific data."""
        if (js and "extras" in js):
            self.extras: Dict[str, Any] = js["extras"]

        self.sampler: int = -1
        """The index of a sampler in this animation used to compute the value for the target."""
        if (js and "sampler" in js):
            self.sampler: int = js["sampler"]

        self.target: AnimationChannelTarget = None
        """The index of the node and TRS property to target."""
        if (js and "target" in js):
            self.target: AnimationChannelTarget = AnimationChannelTarget(
                js["target"])


class AnimationSampler_interpolation(Enum):
    """Interpolation algorithm."""
    LINEAR = "LINEAR"
    STEP = "STEP"
    CUBICSPLINE = "CUBICSPLINE"


class AnimationSampler:
    """Combines input and output accessors with an interpolation algorithm to define a keyframe graph (but not its target)."""

    def __init__(self, js: dict = None)->None:
        self.js: dict = js
        self.extensions: Dict[str, Any] = {}
        """Dictionary object with extension-specific objects."""
        if (js and "extensions" in js):
            self.extensions: Dict[str, Any] = js["extensions"]

        self.extras: Dict[str, Any] = {}
        """Application-specific data."""
        if (js and "extras" in js):
            self.extras: Dict[str, Any] = js["extras"]

        self.input: int = -1
        """The index of an accessor containing keyframe input values, e.g., time."""
        if (js and "input" in js):
            self.input: int = js["input"]

        self.interpolation: AnimationSampler_interpolation = AnimationSampler_interpolation(
            "LINEAR")
        """Interpolation algorithm."""
        if (js and "interpolation" in js):
            self.interpolation: AnimationSampler_interpolation = AnimationSampler_interpolation(
                js["interpolation"])

        self.output: int = -1
        """The index of an accessor, containing keyframe output values."""
        if (js and "output" in js):
            self.output: int = js["output"]


class Animation:
    """A keyframe animation."""

    def __init__(self, js: dict = None)->None:
        self.js: dict = js
        self.extensions: Dict[str, Any] = {}
        """Dictionary object with extension-specific objects."""
        if (js and "extensions" in js):
            self.extensions: Dict[str, Any] = js["extensions"]

        self.extras: Dict[str, Any] = {}
        """Application-specific data."""
        if (js and "extras" in js):
            self.extras: Dict[str, Any] = js["extras"]

        self.name: str = ""
        """The user-defined name of this object."""
        if (js and "name" in js):
            self.name: str = js["name"]

        self.channels: List[AnimationChannel] = []
        """Targets an animation's sampler at a node's property."""
        if (js and "channels" in js):
            self.channels: List[AnimationChannel] = [
                AnimationChannel(x) for x in js["channels"]]

        self.samplers: List[AnimationSampler] = []
        """Combines input and output accessors with an interpolation algorithm to define a keyframe graph (but not its target)."""
        if (js and "samplers" in js):
            self.samplers: List[AnimationSampler] = [
                AnimationSampler(x) for x in js["samplers"]]


class Asset:
    """Metadata about the glTF asset."""

    def __init__(self, js: dict = None)->None:
        self.js: dict = js
        self.extensions: Dict[str, Any] = {}
        """Dictionary object with extension-specific objects."""
        if (js and "extensions" in js):
            self.extensions: Dict[str, Any] = js["extensions"]

        self.extras: Dict[str, Any] = {}
        """Application-specific data."""
        if (js and "extras" in js):
            self.extras: Dict[str, Any] = js["extras"]

        self.copyright: str = ""
        """A copyright message suitable for display to credit the content creator."""
        if (js and "copyright" in js):
            self.copyright: str = js["copyright"]

        self.generator: str = ""
        """Tool that generated this glTF model.  Useful for debugging."""
        if (js and "generator" in js):
            self.generator: str = js["generator"]

        self.version: str = ""
        """The glTF version that this asset targets."""
        if (js and "version" in js):
            self.version: str = js["version"]

        self.minVersion: str = ""
        """The minimum glTF version that this asset targets."""
        if (js and "minVersion" in js):
            self.minVersion: str = js["minVersion"]


class Buffer:
    """A buffer points to binary geometry, animation, or skins."""

    def __init__(self, js: dict = None)->None:
        self.js: dict = js
        self.extensions: Dict[str, Any] = {}
        """Dictionary object with extension-specific objects."""
        if (js and "extensions" in js):
            self.extensions: Dict[str, Any] = js["extensions"]

        self.extras: Dict[str, Any] = {}
        """Application-specific data."""
        if (js and "extras" in js):
            self.extras: Dict[str, Any] = js["extras"]

        self.name: str = ""
        """The user-defined name of this object."""
        if (js and "name" in js):
            self.name: str = js["name"]

        self.uri: str = ""
        """The uri of the buffer."""
        if (js and "uri" in js):
            self.uri: str = js["uri"]

        self.byteLength: int = -1
        """The length of the buffer in bytes."""
        if (js and "byteLength" in js):
            self.byteLength: int = js["byteLength"]


class BufferView_target(Enum):
    """The target that the GPU buffer should be bound to."""
    ARRAY_BUFFER = 34962
    ELEMENT_ARRAY_BUFFER = 34963


class BufferView:
    """A view into a buffer generally representing a subset of the buffer."""

    def __init__(self, js: dict = None)->None:
        self.js: dict = js
        self.extensions: Dict[str, Any] = {}
        """Dictionary object with extension-specific objects."""
        if (js and "extensions" in js):
            self.extensions: Dict[str, Any] = js["extensions"]

        self.extras: Dict[str, Any] = {}
        """Application-specific data."""
        if (js and "extras" in js):
            self.extras: Dict[str, Any] = js["extras"]

        self.name: str = ""
        """The user-defined name of this object."""
        if (js and "name" in js):
            self.name: str = js["name"]

        self.buffer: int = -1
        """The index of the buffer."""
        if (js and "buffer" in js):
            self.buffer: int = js["buffer"]

        self.byteOffset: int = 0
        """The offset into the buffer in bytes."""
        if (js and "byteOffset" in js):
            self.byteOffset: int = js["byteOffset"]

        self.byteLength: int = -1
        """The length of the bufferView in bytes."""
        if (js and "byteLength" in js):
            self.byteLength: int = js["byteLength"]

        self.byteStride: int = -1
        """The stride, in bytes."""
        if (js and "byteStride" in js):
            self.byteStride: int = js["byteStride"]

        self.target: BufferView_target = None
        """The target that the GPU buffer should be bound to."""
        if (js and "target" in js):
            self.target: BufferView_target = BufferView_target(js["target"])


class CameraOrthographic:
    """An orthographic camera containing properties to create an orthographic projection matrix."""

    def __init__(self, js: dict = None)->None:
        self.js: dict = js
        self.extensions: Dict[str, Any] = {}
        """Dictionary object with extension-specific objects."""
        if (js and "extensions" in js):
            self.extensions: Dict[str, Any] = js["extensions"]

        self.extras: Dict[str, Any] = {}
        """Application-specific data."""
        if (js and "extras" in js):
            self.extras: Dict[str, Any] = js["extras"]

        self.xmag: float = float("nan")
        """The floating-point horizontal magnification of the view. Must not be zero."""
        if (js and "xmag" in js):
            self.xmag: float = js["xmag"]

        self.ymag: float = float("nan")
        """The floating-point vertical magnification of the view. Must not be zero."""
        if (js and "ymag" in js):
            self.ymag: float = js["ymag"]

        self.zfar: float = float("nan")
        """The floating-point distance to the far clipping plane. `zfar` must be greater than `znear`."""
        if (js and "zfar" in js):
            self.zfar: float = js["zfar"]

        self.znear: float = float("nan")
        """The floating-point distance to the near clipping plane."""
        if (js and "znear" in js):
            self.znear: float = js["znear"]


class CameraPerspective:
    """A perspective camera containing properties to create a perspective projection matrix."""

    def __init__(self, js: dict = None)->None:
        self.js: dict = js
        self.extensions: Dict[str, Any] = {}
        """Dictionary object with extension-specific objects."""
        if (js and "extensions" in js):
            self.extensions: Dict[str, Any] = js["extensions"]

        self.extras: Dict[str, Any] = {}
        """Application-specific data."""
        if (js and "extras" in js):
            self.extras: Dict[str, Any] = js["extras"]

        self.aspectRatio: float = float("nan")
        """The floating-point aspect ratio of the field of view."""
        if (js and "aspectRatio" in js):
            self.aspectRatio: float = js["aspectRatio"]

        self.yfov: float = float("nan")
        """The floating-point vertical field of view in radians."""
        if (js and "yfov" in js):
            self.yfov: float = js["yfov"]

        self.zfar: float = float("nan")
        """The floating-point distance to the far clipping plane."""
        if (js and "zfar" in js):
            self.zfar: float = js["zfar"]

        self.znear: float = float("nan")
        """The floating-point distance to the near clipping plane."""
        if (js and "znear" in js):
            self.znear: float = js["znear"]


class Camera_type(Enum):
    """Specifies if the camera uses a perspective or orthographic projection."""
    perspective = "perspective"
    orthographic = "orthographic"


class Camera:
    """A camera's projection.  A node can reference a camera to apply a transform to place the camera in the scene."""

    def __init__(self, js: dict = None)->None:
        self.js: dict = js
        self.extensions: Dict[str, Any] = {}
        """Dictionary object with extension-specific objects."""
        if (js and "extensions" in js):
            self.extensions: Dict[str, Any] = js["extensions"]

        self.extras: Dict[str, Any] = {}
        """Application-specific data."""
        if (js and "extras" in js):
            self.extras: Dict[str, Any] = js["extras"]

        self.name: str = ""
        """The user-defined name of this object."""
        if (js and "name" in js):
            self.name: str = js["name"]

        self.orthographic: CameraOrthographic = None
        """An orthographic camera containing properties to create an orthographic projection matrix."""
        if (js and "orthographic" in js):
            self.orthographic: CameraOrthographic = CameraOrthographic(
                js["orthographic"])

        self.perspective: CameraPerspective = None
        """A perspective camera containing properties to create a perspective projection matrix."""
        if (js and "perspective" in js):
            self.perspective: CameraPerspective = CameraPerspective(
                js["perspective"])

        self.type: Camera_type = None
        """Specifies if the camera uses a perspective or orthographic projection."""
        if (js and "type" in js):
            self.type: Camera_type = Camera_type(js["type"])


class Image_mimeType(Enum):
    """The image's MIME type. Required if `bufferView` is defined."""
    image_jpeg = "image/jpeg"
    image_png = "image/png"


class Image:
    """Image data used to create a texture. Image can be referenced by URI or `bufferView` index. `mimeType` is required in the latter case."""

    def __init__(self, js: dict = None)->None:
        self.js: dict = js
        self.extensions: Dict[str, Any] = {}
        """Dictionary object with extension-specific objects."""
        if (js and "extensions" in js):
            self.extensions: Dict[str, Any] = js["extensions"]

        self.extras: Dict[str, Any] = {}
        """Application-specific data."""
        if (js and "extras" in js):
            self.extras: Dict[str, Any] = js["extras"]

        self.name: str = ""
        """The user-defined name of this object."""
        if (js and "name" in js):
            self.name: str = js["name"]

        self.uri: str = ""
        """The uri of the image."""
        if (js and "uri" in js):
            self.uri: str = js["uri"]

        self.mimeType: Image_mimeType = None
        """The image's MIME type. Required if `bufferView` is defined."""
        if (js and "mimeType" in js):
            self.mimeType: Image_mimeType = Image_mimeType(js["mimeType"])

        self.bufferView: int = -1
        """The index of the bufferView that contains the image. Use this instead of the image's uri property."""
        if (js and "bufferView" in js):
            self.bufferView: int = js["bufferView"]


class TextureInfo:
    """The base color texture."""

    def __init__(self, js: dict = None)->None:
        self.js: dict = js
        self.extensions: Dict[str, Any] = {}
        """Dictionary object with extension-specific objects."""
        if (js and "extensions" in js):
            self.extensions: Dict[str, Any] = js["extensions"]

        self.extras: Dict[str, Any] = {}
        """Application-specific data."""
        if (js and "extras" in js):
            self.extras: Dict[str, Any] = js["extras"]

        self.index: int = -1
        """The index of the texture."""
        if (js and "index" in js):
            self.index: int = js["index"]

        self.texCoord: int = 0
        """The set index of texture's TEXCOORD attribute used for texture coordinate mapping."""
        if (js and "texCoord" in js):
            self.texCoord: int = js["texCoord"]


class MaterialPBRMetallicRoughness:
    """A set of parameter values that are used to define the metallic-roughness material model from Physically-Based Rendering (PBR) methodology. When not specified, all the default values of `pbrMetallicRoughness` apply."""

    def __init__(self, js: dict = None)->None:
        self.js: dict = js
        self.extensions: Dict[str, Any] = {}
        """Dictionary object with extension-specific objects."""
        if (js and "extensions" in js):
            self.extensions: Dict[str, Any] = js["extensions"]

        self.extras: Dict[str, Any] = {}
        """Application-specific data."""
        if (js and "extras" in js):
            self.extras: Dict[str, Any] = js["extras"]

        self.baseColorFactor: List[float] = []
        if (js and "baseColorFactor" in js):
            self.baseColorFactor: List[float] = js["baseColorFactor"]

        self.baseColorTexture: TextureInfo = None
        """The base color texture."""
        if (js and "baseColorTexture" in js):
            self.baseColorTexture: TextureInfo = TextureInfo(
                js["baseColorTexture"])

        self.metallicFactor: float = 1.0
        """The metalness of the material."""
        if (js and "metallicFactor" in js):
            self.metallicFactor: float = js["metallicFactor"]

        self.roughnessFactor: float = 1.0
        """The roughness of the material."""
        if (js and "roughnessFactor" in js):
            self.roughnessFactor: float = js["roughnessFactor"]

        self.metallicRoughnessTexture: TextureInfo = None
        """The metallic-roughness texture."""
        if (js and "metallicRoughnessTexture" in js):
            self.metallicRoughnessTexture: TextureInfo = TextureInfo(
                js["metallicRoughnessTexture"])


class MaterialNormalTextureInfo:
    """The normal map texture."""

    def __init__(self, js: dict = None)->None:
        self.js: dict = js
        self.extensions: Dict[str, Any] = {}
        """Dictionary object with extension-specific objects."""
        if (js and "extensions" in js):
            self.extensions: Dict[str, Any] = js["extensions"]

        self.extras: Dict[str, Any] = {}
        """Application-specific data."""
        if (js and "extras" in js):
            self.extras: Dict[str, Any] = js["extras"]

        self.index: int = -1
        """The index of the texture."""
        if (js and "index" in js):
            self.index: int = js["index"]

        self.texCoord: int = 0
        """The set index of texture's TEXCOORD attribute used for texture coordinate mapping."""
        if (js and "texCoord" in js):
            self.texCoord: int = js["texCoord"]

        self.scale: float = 1.0
        """The scalar multiplier applied to each normal vector of the normal texture."""
        if (js and "scale" in js):
            self.scale: float = js["scale"]


class MaterialOcclusionTextureInfo:
    """The occlusion map texture."""

    def __init__(self, js: dict = None)->None:
        self.js: dict = js
        self.extensions: Dict[str, Any] = {}
        """Dictionary object with extension-specific objects."""
        if (js and "extensions" in js):
            self.extensions: Dict[str, Any] = js["extensions"]

        self.extras: Dict[str, Any] = {}
        """Application-specific data."""
        if (js and "extras" in js):
            self.extras: Dict[str, Any] = js["extras"]

        self.index: int = -1
        """The index of the texture."""
        if (js and "index" in js):
            self.index: int = js["index"]

        self.texCoord: int = 0
        """The set index of texture's TEXCOORD attribute used for texture coordinate mapping."""
        if (js and "texCoord" in js):
            self.texCoord: int = js["texCoord"]

        self.strength: float = 1.0
        """A scalar multiplier controlling the amount of occlusion applied."""
        if (js and "strength" in js):
            self.strength: float = js["strength"]


class Material_alphaMode(Enum):
    """The alpha rendering mode of the material."""
    OPAQUE = "OPAQUE"
    MASK = "MASK"
    BLEND = "BLEND"


class Material:
    """The material appearance of a primitive."""

    def __init__(self, js: dict = None)->None:
        self.js: dict = js
        self.extensions: Dict[str, Any] = {}
        """Dictionary object with extension-specific objects."""
        if (js and "extensions" in js):
            self.extensions: Dict[str, Any] = js["extensions"]

        self.extras: Dict[str, Any] = {}
        """Application-specific data."""
        if (js and "extras" in js):
            self.extras: Dict[str, Any] = js["extras"]

        self.name: str = ""
        """The user-defined name of this object."""
        if (js and "name" in js):
            self.name: str = js["name"]

        self.pbrMetallicRoughness: MaterialPBRMetallicRoughness = None
        """A set of parameter values that are used to define the metallic-roughness material model from Physically-Based Rendering (PBR) methodology. When not specified, all the default values of `pbrMetallicRoughness` apply."""
        if (js and "pbrMetallicRoughness" in js):
            self.pbrMetallicRoughness: MaterialPBRMetallicRoughness = MaterialPBRMetallicRoughness(
                js["pbrMetallicRoughness"])

        self.normalTexture: MaterialNormalTextureInfo = None
        """The normal map texture."""
        if (js and "normalTexture" in js):
            self.normalTexture: MaterialNormalTextureInfo = MaterialNormalTextureInfo(
                js["normalTexture"])

        self.occlusionTexture: MaterialOcclusionTextureInfo = None
        """The occlusion map texture."""
        if (js and "occlusionTexture" in js):
            self.occlusionTexture: MaterialOcclusionTextureInfo = MaterialOcclusionTextureInfo(
                js["occlusionTexture"])

        self.emissiveTexture: TextureInfo = None
        """The emissive map texture."""
        if (js and "emissiveTexture" in js):
            self.emissiveTexture: TextureInfo = TextureInfo(
                js["emissiveTexture"])

        self.emissiveFactor: List[float] = []
        if (js and "emissiveFactor" in js):
            self.emissiveFactor: List[float] = js["emissiveFactor"]

        self.alphaMode: Material_alphaMode = Material_alphaMode("OPAQUE")
        """The alpha rendering mode of the material."""
        if (js and "alphaMode" in js):
            self.alphaMode: Material_alphaMode = Material_alphaMode(
                js["alphaMode"])

        self.alphaCutoff: float = 0.5
        """The alpha cutoff value of the material."""
        if (js and "alphaCutoff" in js):
            self.alphaCutoff: float = js["alphaCutoff"]

        self.doubleSided: bool = False
        """Specifies whether the material is double sided."""
        if (js and "doubleSided" in js):
            self.doubleSided: bool = js["doubleSided"]


class MeshPrimitive_mode(Enum):
    """The type of primitives to render."""
    POINTS = 0
    LINES = 1
    LINE_LOOP = 2
    LINE_STRIP = 3
    TRIANGLES = 4
    TRIANGLE_STRIP = 5
    TRIANGLE_FAN = 6


class MeshPrimitive:
    """Geometry to be rendered with the given material."""

    def __init__(self, js: dict = None)->None:
        self.js: dict = js
        self.extensions: Dict[str, Any] = {}
        """Dictionary object with extension-specific objects."""
        if (js and "extensions" in js):
            self.extensions: Dict[str, Any] = js["extensions"]

        self.extras: Dict[str, Any] = {}
        """Application-specific data."""
        if (js and "extras" in js):
            self.extras: Dict[str, Any] = js["extras"]

        self.attributes: Dict[str, int] = {}
        """A dictionary object, where each key corresponds to mesh attribute semantic and each value is the index of the accessor containing attribute's data."""
        if (js and "attributes" in js):
            self.attributes: Dict[str, int] = js["attributes"]

        self.indices: int = -1
        """The index of the accessor that contains the indices."""
        if (js and "indices" in js):
            self.indices: int = js["indices"]

        self.material: int = -1
        """The index of the material to apply to this primitive when rendering."""
        if (js and "material" in js):
            self.material: int = js["material"]

        self.mode: MeshPrimitive_mode = MeshPrimitive_mode(4)
        """The type of primitives to render."""
        if (js and "mode" in js):
            self.mode: MeshPrimitive_mode = MeshPrimitive_mode(js["mode"])

        self.targets: List[Dict[str, int]] = []
        """A dictionary object specifying attributes displacements in a Morph Target, where each key corresponds to one of the three supported attribute semantic (`POSITION`, `NORMAL`, or `TANGENT`) and each value is the index of the accessor containing the attribute displacements' data."""
        if (js and "targets" in js):
            self.targets: List[Dict[str, int]] = js["targets"]


class Mesh:
    """A set of primitives to be rendered.  A node can contain one mesh.  A node's transform places the mesh in the scene."""

    def __init__(self, js: dict = None)->None:
        self.js: dict = js
        self.extensions: Dict[str, Any] = {}
        """Dictionary object with extension-specific objects."""
        if (js and "extensions" in js):
            self.extensions: Dict[str, Any] = js["extensions"]

        self.extras: Dict[str, Any] = {}
        """Application-specific data."""
        if (js and "extras" in js):
            self.extras: Dict[str, Any] = js["extras"]

        self.name: str = ""
        """The user-defined name of this object."""
        if (js and "name" in js):
            self.name: str = js["name"]

        self.primitives: List[MeshPrimitive] = []
        """Geometry to be rendered with the given material."""
        if (js and "primitives" in js):
            self.primitives: List[MeshPrimitive] = [
                MeshPrimitive(x) for x in js["primitives"]]

        self.weights: List[float] = []
        if (js and "weights" in js):
            self.weights: List[float] = js["weights"]


class Node:
    """A node in the node hierarchy.  When the node contains `skin`, all `mesh.primitives` must contain `JOINTS_0` and `WEIGHTS_0` attributes.  A node can have either a `matrix` or any combination of `translation`/`rotation`/`scale` (TRS) properties. TRS properties are converted to matrices and postmultiplied in the `T * R * S` order to compose the transformation matrix; first the scale is applied to the vertices, then the rotation, and then the translation. If none are provided, the transform is the identity. When a node is targeted for animation (referenced by an animation.channel.target), only TRS properties may be present; `matrix` will not be present."""

    def __init__(self, js: dict = None)->None:
        self.js: dict = js
        self.extensions: Dict[str, Any] = {}
        """Dictionary object with extension-specific objects."""
        if (js and "extensions" in js):
            self.extensions: Dict[str, Any] = js["extensions"]

        self.extras: Dict[str, Any] = {}
        """Application-specific data."""
        if (js and "extras" in js):
            self.extras: Dict[str, Any] = js["extras"]

        self.name: str = ""
        """The user-defined name of this object."""
        if (js and "name" in js):
            self.name: str = js["name"]

        self.camera: int = -1
        """The index of the camera referenced by this node."""
        if (js and "camera" in js):
            self.camera: int = js["camera"]

        self.children: List[int] = []
        if (js and "children" in js):
            self.children: List[int] = js["children"]

        self.skin: int = -1
        """The index of the skin referenced by this node."""
        if (js and "skin" in js):
            self.skin: int = js["skin"]

        self.matrix: List[float] = []
        if (js and "matrix" in js):
            self.matrix: List[float] = js["matrix"]

        self.mesh: int = -1
        """The index of the mesh in this node."""
        if (js and "mesh" in js):
            self.mesh: int = js["mesh"]

        self.rotation: List[float] = []
        if (js and "rotation" in js):
            self.rotation: List[float] = js["rotation"]

        self.scale: List[float] = []
        if (js and "scale" in js):
            self.scale: List[float] = js["scale"]

        self.translation: List[float] = []
        if (js and "translation" in js):
            self.translation: List[float] = js["translation"]

        self.weights: List[float] = []
        if (js and "weights" in js):
            self.weights: List[float] = js["weights"]


class Sampler_magFilter(Enum):
    """Magnification filter."""
    NEAREST = 9728
    LINEAR = 9729


class Sampler_minFilter(Enum):
    """Minification filter."""
    NEAREST = 9728
    LINEAR = 9729
    NEAREST_MIPMAP_NEAREST = 9984
    LINEAR_MIPMAP_NEAREST = 9985
    NEAREST_MIPMAP_LINEAR = 9986
    LINEAR_MIPMAP_LINEAR = 9987


class Sampler_wrapS(Enum):
    """s wrapping mode."""
    CLAMP_TO_EDGE = 33071
    MIRRORED_REPEAT = 33648
    REPEAT = 10497


class Sampler_wrapT(Enum):
    """t wrapping mode."""
    CLAMP_TO_EDGE = 33071
    MIRRORED_REPEAT = 33648
    REPEAT = 10497


class Sampler:
    """Texture sampler properties for filtering and wrapping modes."""

    def __init__(self, js: dict = None)->None:
        self.js: dict = js
        self.extensions: Dict[str, Any] = {}
        """Dictionary object with extension-specific objects."""
        if (js and "extensions" in js):
            self.extensions: Dict[str, Any] = js["extensions"]

        self.extras: Dict[str, Any] = {}
        """Application-specific data."""
        if (js and "extras" in js):
            self.extras: Dict[str, Any] = js["extras"]

        self.name: str = ""
        """The user-defined name of this object."""
        if (js and "name" in js):
            self.name: str = js["name"]

        self.magFilter: Sampler_magFilter = None
        """Magnification filter."""
        if (js and "magFilter" in js):
            self.magFilter: Sampler_magFilter = Sampler_magFilter(
                js["magFilter"])

        self.minFilter: Sampler_minFilter = None
        """Minification filter."""
        if (js and "minFilter" in js):
            self.minFilter: Sampler_minFilter = Sampler_minFilter(
                js["minFilter"])

        self.wrapS: Sampler_wrapS = Sampler_wrapS(10497)
        """s wrapping mode."""
        if (js and "wrapS" in js):
            self.wrapS: Sampler_wrapS = Sampler_wrapS(js["wrapS"])

        self.wrapT: Sampler_wrapT = Sampler_wrapT(10497)
        """t wrapping mode."""
        if (js and "wrapT" in js):
            self.wrapT: Sampler_wrapT = Sampler_wrapT(js["wrapT"])


class Scene:
    """The root nodes of a scene."""

    def __init__(self, js: dict = None)->None:
        self.js: dict = js
        self.extensions: Dict[str, Any] = {}
        """Dictionary object with extension-specific objects."""
        if (js and "extensions" in js):
            self.extensions: Dict[str, Any] = js["extensions"]

        self.extras: Dict[str, Any] = {}
        """Application-specific data."""
        if (js and "extras" in js):
            self.extras: Dict[str, Any] = js["extras"]

        self.name: str = ""
        """The user-defined name of this object."""
        if (js and "name" in js):
            self.name: str = js["name"]

        self.nodes: List[int] = []
        if (js and "nodes" in js):
            self.nodes: List[int] = js["nodes"]


class Skin:
    """Joints and matrices defining a skin."""

    def __init__(self, js: dict = None)->None:
        self.js: dict = js
        self.extensions: Dict[str, Any] = {}
        """Dictionary object with extension-specific objects."""
        if (js and "extensions" in js):
            self.extensions: Dict[str, Any] = js["extensions"]

        self.extras: Dict[str, Any] = {}
        """Application-specific data."""
        if (js and "extras" in js):
            self.extras: Dict[str, Any] = js["extras"]

        self.name: str = ""
        """The user-defined name of this object."""
        if (js and "name" in js):
            self.name: str = js["name"]

        self.inverseBindMatrices: int = -1
        """The index of the accessor containing the floating-point 4x4 inverse-bind matrices.  The default is that each matrix is a 4x4 identity matrix, which implies that inverse-bind matrices were pre-applied."""
        if (js and "inverseBindMatrices" in js):
            self.inverseBindMatrices: int = js["inverseBindMatrices"]

        self.skeleton: int = -1
        """The index of the node used as a skeleton root. When undefined, joints transforms resolve to scene root."""
        if (js and "skeleton" in js):
            self.skeleton: int = js["skeleton"]

        self.joints: List[int] = []
        if (js and "joints" in js):
            self.joints: List[int] = js["joints"]


class Texture:
    """A texture and its sampler."""

    def __init__(self, js: dict = None)->None:
        self.js: dict = js
        self.extensions: Dict[str, Any] = {}
        """Dictionary object with extension-specific objects."""
        if (js and "extensions" in js):
            self.extensions: Dict[str, Any] = js["extensions"]

        self.extras: Dict[str, Any] = {}
        """Application-specific data."""
        if (js and "extras" in js):
            self.extras: Dict[str, Any] = js["extras"]

        self.name: str = ""
        """The user-defined name of this object."""
        if (js and "name" in js):
            self.name: str = js["name"]

        self.sampler: int = -1
        """The index of the sampler used by this texture. When undefined, a sampler with repeat wrapping and auto filtering should be used."""
        if (js and "sampler" in js):
            self.sampler: int = js["sampler"]

        self.source: int = -1
        """The index of the image used by this texture."""
        if (js and "source" in js):
            self.source: int = js["source"]


class glTF:
    """The root object for a glTF asset."""

    def __init__(self, js: dict = None)->None:
        self.js: dict = js
        self.extensions: Dict[str, Any] = {}
        """Dictionary object with extension-specific objects."""
        if (js and "extensions" in js):
            self.extensions: Dict[str, Any] = js["extensions"]

        self.extras: Dict[str, Any] = {}
        """Application-specific data."""
        if (js and "extras" in js):
            self.extras: Dict[str, Any] = js["extras"]

        self.extensionsUsed: List[str] = []
        if (js and "extensionsUsed" in js):
            self.extensionsUsed: List[str] = js["extensionsUsed"]

        self.extensionsRequired: List[str] = []
        if (js and "extensionsRequired" in js):
            self.extensionsRequired: List[str] = js["extensionsRequired"]

        self.accessors: List[Accessor] = []
        """A typed view into a bufferView.  A bufferView contains raw binary data.  An accessor provides a typed view into a bufferView or a subset of a bufferView similar to how WebGL's `vertexAttribPointer()` defines an attribute in a buffer."""
        if (js and "accessors" in js):
            self.accessors: List[Accessor] = [
                Accessor(x) for x in js["accessors"]]

        self.animations: List[Animation] = []
        """A keyframe animation."""
        if (js and "animations" in js):
            self.animations: List[Animation] = [
                Animation(x) for x in js["animations"]]

        self.asset: Asset = None
        """Metadata about the glTF asset."""
        if (js and "asset" in js):
            self.asset: Asset = Asset(js["asset"])

        self.buffers: List[Buffer] = []
        """A buffer points to binary geometry, animation, or skins."""
        if (js and "buffers" in js):
            self.buffers: List[Buffer] = [Buffer(x) for x in js["buffers"]]

        self.bufferViews: List[BufferView] = []
        """A view into a buffer generally representing a subset of the buffer."""
        if (js and "bufferViews" in js):
            self.bufferViews: List[BufferView] = [
                BufferView(x) for x in js["bufferViews"]]

        self.cameras: List[Camera] = []
        """A camera's projection.  A node can reference a camera to apply a transform to place the camera in the scene."""
        if (js and "cameras" in js):
            self.cameras: List[Camera] = [Camera(x) for x in js["cameras"]]

        self.images: List[Image] = []
        """Image data used to create a texture. Image can be referenced by URI or `bufferView` index. `mimeType` is required in the latter case."""
        if (js and "images" in js):
            self.images: List[Image] = [Image(x) for x in js["images"]]

        self.materials: List[Material] = []
        """The material appearance of a primitive."""
        if (js and "materials" in js):
            self.materials: List[Material] = [
                Material(x) for x in js["materials"]]

        self.meshes: List[Mesh] = []
        """A set of primitives to be rendered.  A node can contain one mesh.  A node's transform places the mesh in the scene."""
        if (js and "meshes" in js):
            self.meshes: List[Mesh] = [Mesh(x) for x in js["meshes"]]

        self.nodes: List[Node] = []
        """A node in the node hierarchy.  When the node contains `skin`, all `mesh.primitives` must contain `JOINTS_0` and `WEIGHTS_0` attributes.  A node can have either a `matrix` or any combination of `translation`/`rotation`/`scale` (TRS) properties. TRS properties are converted to matrices and postmultiplied in the `T * R * S` order to compose the transformation matrix; first the scale is applied to the vertices, then the rotation, and then the translation. If none are provided, the transform is the identity. When a node is targeted for animation (referenced by an animation.channel.target), only TRS properties may be present; `matrix` will not be present."""
        if (js and "nodes" in js):
            self.nodes: List[Node] = [Node(x) for x in js["nodes"]]

        self.samplers: List[Sampler] = []
        """Texture sampler properties for filtering and wrapping modes."""
        if (js and "samplers" in js):
            self.samplers: List[Sampler] = [Sampler(x) for x in js["samplers"]]

        self.scene: int = -1
        """The index of the default scene."""
        if (js and "scene" in js):
            self.scene: int = js["scene"]

        self.scenes: List[Scene] = []
        """The root nodes of a scene."""
        if (js and "scenes" in js):
            self.scenes: List[Scene] = [Scene(x) for x in js["scenes"]]

        self.skins: List[Skin] = []
        """Joints and matrices defining a skin."""
        if (js and "skins" in js):
            self.skins: List[Skin] = [Skin(x) for x in js["skins"]]

        self.textures: List[Texture] = []
        """A texture and its sampler."""
        if (js and "textures" in js):
            self.textures: List[Texture] = [Texture(x) for x in js["textures"]]


def from_json(js: dict)->glTF:
    return glTF(js)
