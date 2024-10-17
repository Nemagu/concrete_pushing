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


class SystemMeasurement:
    def __init__(self, system_measurement: str = 'СИ') -> None:
        """
        Аргументы:\n
        system_measurement - система измерения. По умолчанию СИ, доступна
        СГС.
        """
        self.system_measurement = system_measurement
        self.validation_data()

    def validation_data(self) -> None:
        if (self.__dict__.get('system_measurement')
                not in SYSTEMS_MEASUREMENT.keys()):
            raise KeyError('Такая система измерения не поддерживается.')


class ValueUnit:
    def __init__(self, value_unit: float = 0.000001) -> None:
        """
        Аргументы:\n
        value_unit - коэффициент преобразования единиц: 0.001 - кило,
        0.000001 - мега.
        """
        self.value_unit = value_unit
        self.validation_data()

    def validation_data(self) -> None:
        pass


class ConcreteSpecification(SystemMeasurement, ValueUnit):
    def __init__(self, concrete_class: str) -> None:
        """
        Аргументы:\n
        concrete_class - класс бетона в виде строки \'B20\'.
        """
        self.concrete_class = concrete_class
        self.validation_data()
        self._set_rbtn()

    def validation_data(self) -> None:
        if self.concrete_class not in CONCRETE_CLASSES:
            raise KeyError('Такой класс бетона не найден.')

    def _set_rbtn(self) -> None:
        self._rbtn = CONCRETE_NORMAL_AXIAL_COMPRESSION.get(
            self.concrete_class
        )

    def get_rbtn(self) -> float:
        """
        Получение нормативного осевого растяжения.
        """
        return self._rbtn

    def get_rbt(self, ybi: float = 0.9) -> float:
        """
        Получение расчетного осевого растяжения.\n
        Аргументы:\n
        ybi - коэффициент условий работы бетона.
        """
        return self.get_rbtn() * ybi


class ReinforcementSpecification:
    def __init__(self, reinforcement_class: str) -> None:
        """
        Аргументы:\n
        reinforcement_class - класс арматуры в виде строки \'A240\'.
        """
        self.reinforcement_class = reinforcement_class
        self.validation_data()
        self._set_rs()

    def validation_data(self) -> None:
        if self.reinforcement_class not in REINFORCEMENT_CLASSES:
            raise KeyError('Такой класс арматуры не найден.')

    def _set_rs(self) -> None:
        self._rs = REINFORCEMENT_NORMAL_STRETCHING.get(
            self.reinforcement_class
        )

    def get_rs(self) -> float:
        """
        Получение нормативного продольного растяжения.
        """
        return self._rs

    def get_rsw(self, ybi: float = 1.0) -> float:
        """
        Получение расчетного осевого растяжения.\n
        Аргументы:\n
        ybi - коэффициент условий работы арматуры.
        """
        return self.get_rs() * ybi
