from .consts import ConcreteSpecification, ReinforcementSpecification


class Concrete(ConcreteSpecification):
    def __init__(
        self,
        concrete_class: float,
        ybi: float,
    ) -> None:
        """
        Аргументы:\n
        concrete_class - класс бетона в виде строки \'B20\';\n
        ybi - коэффициент условий работы бетона.
        """
        super().__init__(concrete_class)
        self.ybi = ybi


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


class Reinforcement(ReinforcementSpecification):
    def __init__(
        self,
        reinforcement_class: str,
        asw: float,
        sw: float,
    ) -> None:
        """
        Аргументы:\n
        reinforcement_class - класс арматуры в виде строки \'A240\';\n
        asw - площадь поперечной арматуры с шагом sw;\n
        sw - шаг поперечной арматуры.
        """
        super().__init__(reinforcement_class)
        self.asw = asw
        self.sw = sw
