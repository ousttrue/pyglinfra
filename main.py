import argparse
import pathlib
from OpenGL.GL import (glViewport, glClearColor, GL_COLOR_BUFFER_BIT,
                       GL_DEPTH_BUFFER_BIT, glClear, glFlush)

import glglue.wgl

import glb
import gltftypes
import scenedescription
import globjects


class Controller:
    def __init__(self) -> None:
        self.scene = scenedescription.Scene()
        self.model: globjects.Model = None

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
        if not self.model:
            self.model = globjects.create_triangle()

        glClearColor(0.0, 0.0, 1.0, 0.0)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        self.model.draw()

        glFlush()

    def load(self, gltf: gltftypes.glTF, bin: bytes):
        self.scene.load(gltf, bin)


def main() -> None:
    parser = argparse.ArgumentParser(description='gltf viewer.')
    parser.add_argument('--src')

    args = parser.parse_args()
    src = pathlib.Path(args.src)

    if not src.exists():
        raise Exception(f'{src} is not exists')

    parsed = glb.parse_glb(src.read_bytes())

    controller = Controller()
    controller.load(*parsed)

    glglue.wgl.mainloop(controller)


if __name__ == '__main__':
    main()
