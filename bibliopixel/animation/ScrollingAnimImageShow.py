from bibliopixel.animation.matrix import Matrix
from bibliopixel.util.image import load_image
import os
from var_dump import var_dump


# Scroll a set of bmp images across the screen to simulate animation
class ScrollingAnimImageShow(Matrix):

    def __init__(self, layout, image_width, repeat_frames, xstep, images=None, offset=(0, 0), **kwds):
        super().__init__(layout, **kwds)
        self.img = images
        self.frames = len(images)
        self.image_width = image_width
        self.repeat_frames = repeat_frames
        self.xstep = xstep
        self.offset = offset
        self.xPos = offset[0] - self.image_width
        self.orig_xPos = offset[0]
        self.tick = 0
        self.frame_show_counter = 0

        # todo: direction, bounce? (for santa)

    def pre_run(self):
        self.xPos = self.orig_xPos - self.image_width
        self.tick = 0
        self.frame_show_counter = 0

    def step(self, amt=1):
        self.layout.all_off()
        self.offset = (self.xPos, 0)
        self.layout.setTexture(load_image.loadImage(self.layout, imagePath=self.img[self.tick % self.frames], offset=self.offset))
        self.layout.fillScreen()
        self.xPos += self.xstep
        if self.xPos >= self.width:
            self.xPos = self.orig_xPos - self.image_width

        # show the same frame frame_show_counter times
        if self.frame_show_counter < self.repeat_frames:
            self.frame_show_counter += 1
        else:
            self.frame_show_counter = 0
            self.tick += 1

