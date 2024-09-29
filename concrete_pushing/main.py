class Concrete:
    def __init__(self, concrete_class: float, ybi: float) -> None:
        self.concrete_class = concrete_class
        self.ybi = ybi


class Geometry:
    def __init__(self, acy: float, bcx: float, h: float, a: float) -> None:
        self.acy = acy
        self.bcx = bcx
        self.h = h
        self.a = a


class Force:
    def __init__(self, force: float) -> None:
        self.force = force


class Moment:
    def __init__(self, mx: float, my: float) -> None:
        self.mx = mx
        self.my = my


class OnlyForce(Force, Geometry, Concrete):
    def __init__(self, force: float, acy: float, bcx: float, h: float, a: float, concrete_class: float, ybi: float) -> None:
        # super(Force, self).__init__(force)
        # super(Geometry, self).__init__(acy, bcx, h, a)
        # super(Force, self).__init__(concrete_class, ybi)
        Force.__init__(self, force)
        Geometry.__init__(self, acy, bcx, h, a)
        Concrete.__init__(self, concrete_class, ybi)
