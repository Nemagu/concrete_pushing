from .consts import SystemMeasurement, ValueUnit
from .entities import Concrete, Geometry


class Generic:
    def __init__(
        self,
        data: dict[str, float],
        acy: float,
        bcx: float,
        h: float,
        a: float,
        concrete_class: float,
        ybi: float,
        system_measurement: str = 'СИ',
        value_unit: float = 0.000001,
    ) -> None:
        """
        Аргументы:\n
        data - необходимые изменяемы данные для расчета;\n
        acy - ширина зоны приложения нагрузки;\n
        bcx - высота зоны приложения нагрузки;\n
        h - высота сечения;\n
        a - защитный слой бетона растянутой зоны;\n
        concrete_class - класс бетона в виде строки \'B20\';\n
        ybi - коэффициент условий работы бетона;\n
        system_measurement - система измерения. По умолчанию СИ, доступна
        СГС;\n
        value_unit - коэффициент преобразования единиц: 0.001 - кило,
        0.000001 - мега.
        """
        self.geometry = Geometry(acy, bcx, h, a)
        self.concrete = Concrete(concrete_class, ybi)
        self.system_measurememt = SystemMeasurement(system_measurement)
        self.value_unit = ValueUnit(value_unit)
        self.__init_mixin(data)

    def __init_mixin(self, data: dict) -> None:
        return None

    def get_h0(self):
        if hasattr(self, 'h0'):
            return self.geometry.h0

        self.geometry.h0 = (self.geometry.h - self.geometry.a)
        return self.geometry.h0

    def get_u(self):
        if hasattr(self, 'u'):
            return self.geometry.u

        self.geometry.u = (
            self.geometry.acy + self.geometry.bcx + self.get_h0() * 2
        ) * 2
        return self.geometry.u

    def get_ab(self):
        if hasattr(self, 'ab'):
            return self.geometry.ab
