import argparse
import pathlib
import math
from OpenGL.GL import (glViewport, glClearColor, GL_COLOR_BUFFER_BIT,
                       GL_DEPTH_BUFFER_BIT, glClear, glFlush)

import glglue.wgl

import gltf
import scenedescription
import globjects

import ctypesmath


class Perspective:
    def __init__(self) -> None:
        self.matrix = ctypesmath.Mat4.new_identity()
        self.fov_y = math.pi * 30 / 180
        self.aspect = 1
        self.z_near = 0.1
        self.z_far = 50
        self.update_matrix()

    def update_matrix(self) -> None:
        self.matrix.perspective(self.fov_y, self.aspect, self.z_near,
                                self.z_far)


class Orbit:
    def __init__(self) -> None:
        self.matrix = ctypesmath.Mat4.new_identity()
        self.x = 0
        self.y = 0
        self.distance = 2
        self.yaw = 0
        self.pitch = 0
        self.update_matrix()

    def update_matrix(self) -> None:
        t = ctypesmath.Mat4.new_translate(self.x, self.y, -self.distance)
        yaw = ctypesmath.Mat4.new_rotate_y(self.yaw)
        pitch = ctypesmath.Mat4.new_rotate_x(self.pitch)
        self.matrix = yaw * pitch * t


class Controller:
    def __init__(self) -> None:
        self.scene = scenedescription.Scene()
        self.renderer = globjects.Renderer()
        self.projection = Perspective()
        self.view = Orbit()

        self.x = 0
        self.y = 0
        self.left = False
        self.middle = False
        self.right = False

        self.width = 600
        self.height = 400

    def onResize(self, w: int, h: int) -> None:
        ''' when OpenGL window is resized. '''
        glViewport(0, 0, w, h)
        self.width = w
        self.height = h
        self.projection.aspect = w / h
        self.projection.update_matrix()

    def onLeftDown(self, x: int, y: int) -> None:
        ''' mouse input '''
        self.left = True
        self.x = x
        self.y = y

    def onLeftUp(self, x: int, y: int) -> None:
        ''' mouse input '''
        self.left = False

    def onMiddleDown(self, x: int, y: int) -> None:
        ''' mouse input '''
        self.middle = True
        self.x = x
        self.y = y

    def onMiddleUp(self, x: int, y: int) -> None:
        ''' mouse input '''
        self.middle = False

    def onRightDown(self, x: int, y: int) -> None:
        ''' mouse input '''
        self.right = True
        self.x = x
        self.y = y

    def onRightUp(self, x: int, y: int) -> None:
        ''' mouse input '''
        self.right = False

    def onMotion(self, x: int, y: int) -> None:
        ''' mouse input '''
        dx = x - self.x
        self.x = x
        dy = y - self.y
        self.y = y

        if self.right:
            self.view.yaw += dx * 0.01
            self.view.pitch += dy * 0.01
            self.view.update_matrix()

        if self.middle:
            plane_height = math.tan(
                self.projection.fov_y * 0.5) * self.view.distance * 2
            self.view.x += dx / self.height * plane_height
            self.view.y -= dy / self.height * plane_height
            self.view.update_matrix()

    def onWheel(self, d: int) -> None:
        ''' mouse input '''
        if d > 0:
            self.view.distance *= 1.1
            self.view.update_matrix()
        elif d < 0:
            self.view.distance *= 0.9
            self.view.update_matrix()

    def onKeyDown(self, keycode: int) -> None:
        ''' keyboard input'''
        pass

    def onUpdate(self, d: int) -> None:
        ''' each frame. milliseconds '''
        pass

    def draw(self) -> None:
        ''' each frame'''
        glClearColor(0.0, 0.0, 1.0, 0.0)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        self.renderer.draw(self.scene, self.projection.matrix,
                           self.view.matrix)

        glFlush()

    def load(self, data: gltf.GltfManipulator):
        self.scene.load(data)


def main() -> None:
    parser = argparse.ArgumentParser(description='gltf viewer.')
    parser.add_argument('--src')

    args = parser.parse_args()
    src = pathlib.Path(args.src)

    if not src.exists():
        raise Exception(f'{src} is not exists')

    data = gltf.load(src.read_bytes())

    controller = Controller()
    controller.load(data)

    glglue.wgl.mainloop(controller)


if __name__ == '__main__':
    main()
