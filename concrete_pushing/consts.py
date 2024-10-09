SYSTEMS_MEASUREMENT: dict[str, float] = {
    'СИ': 1.0,
    'СГС': 0.10197162129779283,
}

CONCRETE_CLASSES: tuple[str] = (
    'B10',
    'B15',
    'B20',
    'B25',
    'B30',
    'B35',
    'B40',
    'B45',
    'B50',
    'B55',
    'B60',
)

REINFORCEMENT_CLASSES: tuple[str] = (
    'A240',
    'A300',
    'A400',
    'A500',
    'A600',
    'A800',
    'A1000',
    'B500',
)

CONCRETE_NORMAL_AXIAL_COMPRESSION: dict[str, int] = {
    'B10': 850000,
    'B15': 1100000,
    'B20': 1350000,
    'B25': 1550000,
    'B30': 1750000,
    'B35': 1950000,
    'B40': 2100000,
    'B45': 2250000,
    'B50': 2450000,
    'B55': 2600000,
    'B60': 2750000,
}

REINFORCEMENT_NORMAL_STRETCHING: dict[str, int] = {
    'A240': 210000000,
    'A300': 270000000,
    'A400': 350000000,
    'A500': 435000000,
    'A600': 520000000,
    'A800': 695000000,
    'A1000': 870000000,
    'B500': 435000000,
}


class ConcreteConsts:
    def __init__(
        self,
        concrete_class: str,
        system_measurement: str = 'СИ',
        value_unit: float = 0.000001,
    ):
        """
        Аргументы:\n
        concrete_class - класс бетона в виде строки \'B20\';\n
        system_measurement - система измерения. По умолчанию СИ, доступна
        СГС;\n
        value_unit - коэффициент преобразования единиц: 0.001 - кило,
        0.000001 - мега.
        """
        self.system_measurement = system_measurement
        self.concrete_class = concrete_class
        self.value_unit = value_unit
        self.data_validation()
        self._set_rbtn()

    def data_validation(self):
        if self.__dict__.get('concrete_class') not in CONCRETE_CLASSES:
            raise KeyError('Такой класс бетона не найден.')

        if (self.__dict__.get('system_measurement')
                not in SYSTEMS_MEASUREMENT.keys()):
            raise KeyError('Такая система измерения не поддерживается.')

    def _set_rbtn(self):
        self._rbtn = CONCRETE_NORMAL_AXIAL_COMPRESSION.get(
            self.concrete_class
        )

    def get_rbtn(self) -> float:
        """
        Получение нормативного осевого растяжения.
        """
        return self._rbtn * self.value_unit

    def get_rbt(self, ybi: float = 0.9) -> float:
        """
        Получение расчетного осевого растяжения.\n
        Аргументы:\n
        ybi - коэффициент условий работы бетона.
        """
        return self.get_rbtn() * ybi


class ReinforcementConsts:
    def __init__(
        self,
        reinforcement_class: str,
        unit_measurement: str = 'СИ',
        value_unit: float = 0.000001,
    ):
        """
        Аргументы:\n
        reinforcement_class - класс арматуры в виде строки \'A240\';\n
        unit_measurement - система измерения. По умолчанию СИ, доступна СГС;\n
        value_unit - коэффициент преобразования единиц: 0.001 - кило,
        0.000001 - мега.
        """
        self.reinforcement_class = reinforcement_class
        self.value_unit = value_unit
        self.data_validation()
        self._set_rs()

    def data_validation(self):
        if self.__dict__.get('concrete_class') not in REINFORCEMENT_CLASSES:
            raise KeyError('Такой класс арматуры не найден.')

        if (self.__dict__.get('system_measurement')
                not in SYSTEMS_MEASUREMENT.keys()):
            raise KeyError('Такая система измерения не поддерживается.')

    def _set_rs(self):
        self._rs = REINFORCEMENT_NORMAL_STRETCHING.get(
            self.reinforcement_class
        )

    def get_rs(self) -> float:
        """
        Получение нормативного продольного растяжения.
        """
        return self._rs * self.value_unit

    def get_rsw(self, ybi: float = 1.0) -> float:
        """
        Получение расчетного осевого растяжения.\n
        Аргументы:\n
        ybi - коэффициент условий работы арматуры.
        """
        return self.get_rs() * ybi
