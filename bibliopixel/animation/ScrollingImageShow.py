from bibliopixel.animation.matrix import Matrix
from bibliopixel.util.image import load_image
import os


# Scroll a bmp across the screen
class ScrollingImageShow(Matrix):

    def __init__(self, layout, imagePath=None, offset=(0, 0), **kwds):
        super().__init__(layout, **kwds)
        if imagePath is None:
            cur_dir = os.path.dirname(os.path.realpath(__file__))
            imagePath = os.path.abspath(os.path.join(cur_dir, '../../Graphics/ml_logo.bmp'))
        self.img = imagePath
        self.offset = offset
        self.xPos = offset[0] - 100
        print(self.xPos)
        self.orig_xPos = offset[0]

        # todo: pixilwidth, frames, speed, direction, bounce? (for santa)

    def step(self, amt=2):
        self.layout.all_off()
        self.offset = (self.xPos, 0)
        # print(self.offset)
        self.layout.setTexture(load_image.loadImage(self.layout, imagePath=self.img, offset=self.offset))
        self.layout.fillScreen()
        self.xPos += amt
        if self.xPos >= self.width:
            self.xPos = self.orig_xPos - 100
