import unittest
import pathlib
import math
import sys
HERE = pathlib.Path(__file__).absolute().parent
sys.path.append(str(HERE.parent))
import ctypesmath


class TestCtypeMatn(unittest.TestCase):
    def test_translation(self):
        l = ctypesmath.Mat4.new_translate(1, 2, 3)
        r = ctypesmath.Mat4.new_translate(1, 2, 3)
        m = l * r
        self.assertEqual(2, m._41)
        self.assertEqual(4, m._42)
        self.assertEqual(6, m._43)
        v = ctypesmath.Vec4(1, 2, 3, 1) * m
        self.assertEqual(3, v.x)
        self.assertEqual(6, v.y)
        self.assertEqual(9, v.z)
        self.assertEqual(1, v.w)

    def test_projection(self):
        z_near = 0.1
        z_far = 10
        proj = ctypesmath.Mat4.new_perspective(30 / 180 * math.pi, 1, z_near,
                                               z_far)

        p_near = ctypesmath.Vec4(0, 0, -z_near, 1)  # view coordinate
        v_near = p_near * proj
        d_near = v_near.z / v_near.w
        self.assertAlmostEqual(-1, d_near, places=6)

        p_far = ctypesmath.Vec4(0, 0, -z_far, 1)  # view coordinate
        v_far = p_far * proj
        d_far = v_far.z / v_far.w
        self.assertAlmostEqual(1, d_far, places=6)

    def test_far(self):
        p = ctypesmath.Mat4.new_perspective(30 / 180 * math.pi, 1, 0.1, 10)
        v = ctypesmath.Vec4(0, 0, -10, 1) * p
        d = v.z / v.w
        self.assertAlmostEqual(1, d, places=1)


if __name__ == '__main__':
    unittest.main()
