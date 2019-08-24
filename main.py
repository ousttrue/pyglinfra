import argparse
import pathlib
from OpenGL.GL import (glViewport, glClearColor, GL_COLOR_BUFFER_BIT,
                       GL_DEPTH_BUFFER_BIT, glClear, glFlush)

import glglue.wgl

import gltf
import scenedescription
import globjects


class Controller:
    def __init__(self) -> None:
        self.scene = scenedescription.Scene()
        self.renderer = globjects.Renderer()

    def onResize(self, w: int, h: int) -> None:
        ''' when OpenGL window is resized. '''
        glViewport(0, 0, w, h)

    def onLeftDown(self, x: int, y: int) -> None:
        ''' mouse input '''
        pass

    def onLeftUp(self, x: int, y: int) -> None:
        ''' mouse input '''
        pass

    def onMiddleDown(self, x: int, y: int) -> None:
        ''' mouse input '''
        pass

    def onMiddleUp(self, x: int, y: int) -> None:
        ''' mouse input '''
        pass

    def onRightDown(self, x: int, y: int) -> None:
        ''' mouse input '''
        pass

    def onRightUp(self, x: int, y: int) -> None:
        ''' mouse input '''
        pass

    def onMotion(self, x: int, y: int) -> None:
        ''' mouse input '''
        pass

    def onWheel(self, d: int) -> None:
        ''' mouse input '''
        pass

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

        self.renderer.draw(self.scene)

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
