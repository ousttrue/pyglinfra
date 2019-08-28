import ctypes
import math


class Mat4(ctypes.Structure):
    _fields_ = [("_11", ctypes.c_float), ("_12", ctypes.c_float),
                ("_13", ctypes.c_float), ("_14", ctypes.c_float),
                ("_21", ctypes.c_float), ("_22", ctypes.c_float),
                ("_23", ctypes.c_float), ("_24", ctypes.c_float),
                ("_31", ctypes.c_float), ("_32", ctypes.c_float),
                ("_33", ctypes.c_float), ("_34", ctypes.c_float),
                ("_41", ctypes.c_float), ("_42", ctypes.c_float),
                ("_43", ctypes.c_float), ("_44", ctypes.c_float)]

    def __str__(self) -> str:
        return f'[{self._11}, {self._12}, {self._13}, {self._14}]' + f'[{self._21}, {self._22}, {self._23}, {self._24}]' + f'[{self._31}, {self._32}, {self._33}, {self._34}]' + f'[{self._41}, {self._42}, {self._43}, {self._44}]'

    def to_array(self):
        return (ctypes.c_float * 16).from_buffer(self)

    def mul(self, lhs, rhs) -> None:
        self._11 = lhs._11 * rhs._11 + lhs._12 * rhs._21 + lhs._13 * rhs._31 + lhs._14 * rhs._41
        self._12 = lhs._11 * rhs._12 + lhs._12 * rhs._22 + lhs._13 * rhs._32 + lhs._14 * rhs._42
        self._13 = lhs._11 * rhs._13 + lhs._12 * rhs._23 + lhs._13 * rhs._33 + lhs._14 * rhs._43
        self._14 = lhs._11 * rhs._14 + lhs._12 * rhs._24 + lhs._13 * rhs._34 + lhs._14 * rhs._44

        self._21 = lhs._21 * rhs._11 + lhs._22 * rhs._21 + lhs._23 * rhs._31 + lhs._24 * rhs._41
        self._22 = lhs._21 * rhs._12 + lhs._22 * rhs._22 + lhs._23 * rhs._32 + lhs._24 * rhs._42
        self._23 = lhs._21 * rhs._13 + lhs._22 * rhs._23 + lhs._23 * rhs._33 + lhs._24 * rhs._43
        self._24 = lhs._21 * rhs._14 + lhs._22 * rhs._24 + lhs._23 * rhs._34 + lhs._24 * rhs._44

        self._31 = lhs._31 * rhs._11 + lhs._32 * rhs._21 + lhs._33 * rhs._31 + lhs._34 * rhs._41
        self._32 = lhs._31 * rhs._12 + lhs._32 * rhs._22 + lhs._33 * rhs._32 + lhs._34 * rhs._42
        self._33 = lhs._31 * rhs._13 + lhs._32 * rhs._23 + lhs._33 * rhs._33 + lhs._34 * rhs._43
        self._34 = lhs._31 * rhs._14 + lhs._32 * rhs._24 + lhs._33 * rhs._34 + lhs._34 * rhs._44

        self._41 = lhs._41 * rhs._11 + lhs._42 * rhs._21 + lhs._43 * rhs._31 + lhs._44 * rhs._41
        self._42 = lhs._41 * rhs._12 + lhs._42 * rhs._22 + lhs._43 * rhs._32 + lhs._44 * rhs._42
        self._43 = lhs._41 * rhs._13 + lhs._42 * rhs._23 + lhs._43 * rhs._33 + lhs._44 * rhs._43
        self._44 = lhs._41 * rhs._14 + lhs._42 * rhs._24 + lhs._43 * rhs._34 + lhs._44 * rhs._44

    def perspective(self, fov_y: float, aspect: float, z_near: float,
                    z_far: float) -> None:
        fov_y *= 0.5
        cot = 1 / math.tan(fov_y)
        self._11 = cot / aspect
        self._22 = cot
        self._33 = -(z_far + z_near) / (z_far - z_near)
        if False:
            self._43 = -2 * z_far * z_near / (z_far - z_near)
            self._34 = -1
        else:
            self._34 = -2 * z_far * z_near / (z_far - z_near)
            self._43 = -1

    @classmethod
    def new_identity(cls):
        return cls(
            1,
            0,
            0,
            0,  #
            0,
            1,
            0,
            0,  #
            0,
            0,
            1,
            0,  #
            0,
            0,
            0,
            1  #
        )

    @classmethod
    def new_translate(cls, x, y, z):
        return cls(
            1,
            0,
            0,
            0,  #
            0,
            1,
            0,
            0,  #
            0,
            0,
            1,
            0,  #
            x,
            y,
            z,
            1  #
        )

    @classmethod
    def new_rotate_y(cls, rad):
        s = math.sin(rad)
        c = math.cos(rad)
        return cls(
            c,
            0,
            s,
            0,  #
            0,
            1,
            0,
            0,  #
            -s,
            0,
            c,
            0,  #
            0,
            0,
            0,
            1  #
        )

    @classmethod
    def new_rotate_x(cls, rad):
        s = math.sin(rad)
        c = math.cos(rad)
        return cls(
            1,
            0,
            0,
            0,  #
            0,
            c,
            -s,
            0,  #
            0,
            s,
            c,
            0,  #
            0,
            0,
            0,
            1  #
        )
