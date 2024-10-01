class ConcreteConsts:
    __RBTNB10 = 0.85
    __RBTNB15 = 1.1
    __RBTNB20 = 1.35
    __RBTNB25 = 1.55
    __RBTNB30 = 1.75
    __RBTNB35 = 1.95
    __RBTNB40 = 2.1
    __RBTNB45 = 2.25
    __RBTNB50 = 2.45
    __RBTNB55 = 2.6
    __RBTNB60 = 2.75
    
    @classmethod
    def get_rbtn(cls, concrete_class: str=None) -> float:
        """
        Получение нормативного осевого растяжения.\n
        Аргументы:\n
        concrete_class - класс бетона в виде строки \'B20\'.
        """
        rbtn = getattr(cls, f'__RBTN{concrete_class}', None)
        if rbtn is None:
            raise KeyError(f'Такого класса бетона нет: {concrete_class}')
        return rbtn
    
    @classmethod
    def get_rbt(cls, concrete_class: str, ybi: float) -> float:
        """
        Получение расчетного осевого растяжения.\n
        Аргументы:\n
        concrete_class - класс бетона в виде строки \'B20\';\n
        ybi - коэффициент условий работы бетона.
        """
        return cls.get_rbtn(concrete_class=concrete_class) * ybi


class ReinforcementConsts:
    __RSA240 = 215
    __RSA300 = 270
    __RSA400 = 355
    __RSA500 = 435
    
    @classmethod
    def get_rs(cls, reinforcement_class: str) -> float:
        """
        Получение нормативного продольного растяжения.\n
        Аргументы:\n
        reinforcement_class - класс арматуры в виде строки \'A240\'.
        """
        rs = getattr(cls, f'__RS{reinforcement_class}', None)
        if rs is None:
            raise KeyError(f'Такого класса арматуры нет: {reinforcement_class}')
        return rs
    
    @classmethod
    def get_rsw(cls, reinforcement_class: str, ybi: float = 0.8) -> float:
        """
        Получение расчетного осевого растяжения.\n
        Аргументы:\n
        reinforcement_class - класс арматуры в виде строки \'A240\';\n
        ybi - коэффициент условий работы арматуры.
        """
        return cls.get_rs(reinforcement_class=reinforcement_class) * ybi
        