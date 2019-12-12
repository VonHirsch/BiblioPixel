import copy
from . import parallel
from .. util import color_list


class Mixer(parallel.Parallel):
    def __init__(self, *args, levels=None, master=1, **kwds):
        self.master = master

        super().__init__(*args, **kwds)
        self.mixer = color_list.Mixer(
            self.color_list,
            [a.color_list for a in self.animations],
            levels)

    @property
    def levels(self):
        return self.mixer.levels

    # todo: remove these horrible hacks to get an animations by index in the mixer
    @property
    def animation_index_0(self):
        return self.animations[0]

    @property
    def animation_index_1(self):
        return self.animations[1]

    @property
    def animation_index_2(self):
        return self.animations[2]

    @property
    def animation_index_3(self):
        return self.animations[3]

    @property
    def animation_index_4(self):
        return self.animations[4]

    @levels.setter
    def levels(self, levels):
        self.mixer.levels[:] = levels

    def step(self, amt=1):
        super().step(amt)
        self.mixer.clear()
        self.mixer.mix(self.master)
