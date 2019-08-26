import ctypes


class Mat4(ctypes.Structure):
    _fields_ = [
        ("_11", ctypes.c_float),
        ("_12", ctypes.c_float),
        ("_13", ctypes.c_float),
        ("_14", ctypes.c_float),
        ("_21", ctypes.c_float),
        ("_22", ctypes.c_float),
        ("_23", ctypes.c_float),
        ("_24", ctypes.c_float),
        ("_31", ctypes.c_float),
        ("_32", ctypes.c_float),
        ("_33", ctypes.c_float),
        ("_34", ctypes.c_float),
        ("_41", ctypes.c_float),
        ("_42", ctypes.c_float),
        ("_43", ctypes.c_float),
        ("_44", ctypes.c_float)
    ]

    def to_array(self):
        return (ctypes.c_float * 16).from_buffer(self)

    @classmethod
    def identity(cls):
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
