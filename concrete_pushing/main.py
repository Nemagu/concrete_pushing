from .consts import ConcreteSpecification, ReinforcementSpecification, SystemMeasurement, ValueUnit
from .mixins import ForceMixin, ReinforcementMixin
from .generics import Generic


class OnlyForce(ForceMixin, Generic):
    pass
#     def __init__(
#         self,
#         f: float,
#         acy: float,
#         bcx: float,
#         h: float,
#         a: float,
#         concrete_class: float,
#         ybi: float,
#         system_measurement: str = 'СИ',
#         value_unit: float = 0.000001,
#     ) -> None:
#         """
#         Аргументы:\n
#         f - сосредоточеная сила от внешней нагрузки;\n
#         acy - ширина зоны приложения нагрузки;\n
#         bcx - высота зоны приложения нагрузки;\n
#         h - высота сечения;\n
#         a - защитный слой бетона растянутой зоны;\n
#         concrete_class - класс бетона в виде строки \'B20\';\n
#         ybi - коэффициент условий работы бетона;\n
#         system_measurement - система измерения. По умолчанию СИ, доступна
#         СГС;\n
#         value_unit - коэффициент преобразования единиц: 0.001 - кило,
#         0.000001 - мега.
#         """
#         super().__init__(
#             acy,
#             bcx,
#             h,
#             a,
#             concrete_class,
#             ybi,
#             system_measurement,
#             value_unit,
#         )
#         self.__init_load({'f': f})


class OnlyForceWithReinforcement(ReinforcementMixin, OnlyForce):
    pass
    # def __init__(
    #     self,
    #     f: float,
    #     acy: float,
    #     bcx: float,
    #     h: float,
    #     a: float,
    #     concrete_class: float,
    #     ybi: float,
    #     reinforcement_class: str,
    #     asw: float,
    #     sw: float,
    #     system_measurement: str = 'СИ',
    #     value_unit: float = 0.000001,
    # ) -> None:
    #     """
    #     Аргументы:\n
    #     f - сосредоточеная сила от внешней нагрузки;\n
    #     acy - ширина зоны приложения нагрузки;\n
    #     bcx - высота зоны приложения нагрузки;\n
    #     h - высота сечения;\n
    #     a - защитный слой бетона растянутой зоны;\n
    #     concrete_class - класс бетона в виде строки \'B20\';\n
    #     ybi - коэффициент условий работы бетона;\n
    #     reinforcement_class - класс арматуры в виде строки \'A240\';\n
    #     asw - площадь поперечной арматуры с шагом sw;\n
    #     sw - шаг поперечной арматуры;\n
    #     system_measurement - система измерения. По умолчанию СИ, доступна
    #     СГС;\n
    #     value_unit - коэффициент преобразования единиц: 0.001 - кило,
    #     0.000001 - мега.
    #     """
    #     OnlyForce.__init__(
    #         f,
    #         acy,
    #         bcx,
    #         h,
    #         a,
    #         concrete_class,
    #         ybi,
    #         system_measurement,
    #         value_unit,
    #     )
    #     Reinforcement.__init__(self, reinforcement_class, asw, sw)

    # def get_qsw(self):
    #     if hasattr(self, 'qsw'):
    #         return self.qsw

    #     self.qsw = self.get_rsw(self.ybi) * self.asw / self.sw
    #     return self.qsw

    # def get_fswult(self):
    #     if hasattr(self, 'fswult'):
    #         return self.fswult

    #     self.fswult = 0.8 * self.get_qsw() * self.get_u()
    #     return self.fswult

    # def get_fult(self):
    #     super().get_fult()
    #     self.get_fswult()
    #     if self.fswult < (self.fbult * 0.25):
    #         return self.fbult
    #     fult = self.fswult + self.fbult
    #     if fult > (self.fbult * 2):
    #         return self.fbult * 2
    #     return fult
