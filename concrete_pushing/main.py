from .consts import ConcreteConsts, ReinforcementConsts


class Concrete:
    def __init__(self, concrete_class: float, ybi: float) -> None:
        """
        Аргументы:\n
        concrete_class - класс бетона в виде строки \'B20\';\n
        ybi - коэффициент условий работы бетона.
        """
        self.concrete_class = concrete_class
        self.ybi = ybi


class Reinforcement:
    def __init__(self, reinforcement_class: str, asw: float, sw: float) -> None:
        """
        Аргументы:\n
        reinforcement_class - класс арматуры в виде строки \'A240\';\n
        asw - площадь поперечной арматуры с шагом sw;\n
        sw - шаг поперечной арматуры.
        """
        self.reinforcement_class = reinforcement_class
        self.asw = asw
        self.sw = sw


class Geometry:
    def __init__(self, acy: float, bcx: float, h: float, a: float) -> None:
        """
        Аргументы:\n
        acy - ширина зоны приложения нагрузки;\n
        bcx - высота зоны приложения нагрузки;\n
        h - высота сечения;\n
        a - защитный слой бетона растянутой зоны.
        """
        self.acy = acy
        self.bcx = bcx
        self.h = h
        self.a = a


class Force:
    def __init__(self, f: float) -> None:
        """
        Аргументы:\n
        f - сосредоточеная сила от внешней нагрузки.
        """
        self.f = f


class Moment:
    def __init__(self, mx: float, my: float) -> None:
        """
        Аргументы:\n
        mx - момент вдоль оси x:\n
        my - момент вдоль оси y.
        """
        self.mx = mx
        self.my = my


class OnlyForce(Force, Geometry, Concrete):
    def __init__(
        self,
        f: float,
        acy: float,
        bcx: float,
        h: float,
        a: float,
        concrete_class: float,
        ybi: float,
    ) -> None:
        """
        Аргументы:\n
        f - сосредоточеная сила от внешней нагрузки;\n
        acy - ширина зоны приложения нагрузки;\n
        bcx - высота зоны приложения нагрузки;\n
        h - высота сечения;\n
        a - защитный слой бетона растянутой зоны;\n
        concrete_class - класс бетона в виде строки \'B20\';\n
        ybi - коэффициент условий работы бетона.
        """
        Force.__init__(self, f)
        Geometry.__init__(self, acy, bcx, h, a)
        Concrete.__init__(self, concrete_class, ybi)

    def get_h0(self):
        if hasattr(self, 'h0'):
            return self.h0

        self.h0 = (self.h - self.a)
        return self.h0

    def get_u(self):
        if hasattr(self, 'u'):
            return self.u

        self.u = (self.acy + self.bcx + self.get_h0() * 2) * 2
        return self.u

    def get_ab(self):
        if hasattr(self, 'ab'):
            return self.ab

        self.ab = self.get_u() * self.get_h0()
        return self.ab

    def get_fbult(self):
        if hasattr(self, 'fbult'):
            return self.fbult

        self.fbult = ConcreteConsts.get_rbt(
            self.concrete_class, self.ybi
        ) * self.get_ab()
        return self.fbult

    def calculation_result(self):
        return self.f <= self.get_fbult()


class OnlyForceWithReinforcement(Reinforcement, OnlyForce):
    def __init__(
        self,
        f: float,
        acy: float,
        bcx: float,
        h: float,
        a: float,
        concrete_class: float,
        ybi: float,
        reinforcement_class: str,
        asw: float,
        sw: float,
    ) -> None:
        """
        Аргументы:\n
        f - сосредоточеная сила от внешней нагрузки;\n
        acy - ширина зоны приложения нагрузки;\n
        bcx - высота зоны приложения нагрузки;\n
        h - высота сечения;\n
        a - защитный слой бетона растянутой зоны;\n
        concrete_class - класс бетона в виде строки \'B20\';\n
        ybi - коэффициент условий работы бетона;\n
        reinforcement_class - класс арматуры в виде строки \'A240\';\n
        asw - площадь поперечной арматуры с шагом sw;\n
        sw - шаг поперечной арматуры.
        """
        super().__init__(f, acy, bcx, h, a, concrete_class, ybi)
        Reinforcement.__init__(self, reinforcement_class, asw, sw)

    def get_qsw(self):
        if hasattr(self, 'qsw'):
            return self.qsw

        self.qsw = (ReinforcementConsts.get_rsw(
            self.reinforcement_class
        ) * self.asw / self.sw)
        return self.qsw

    def get_fswult(self):
        if hasattr(self, 'fswult'):
            return self.fswult

        self.fswult = 0.8 * self.get_qsw() * self.get_u()
        return self.fswult
