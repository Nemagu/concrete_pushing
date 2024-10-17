from .entities import Force, Moment, Reinforcement


class ForceMixin:
    def __init_mixin(self, data):
        super().__init_mixin(data)
        self.force = Force(data.get('f'))

    def get_fbult(self):
        if hasattr(self, 'fbult'):
            return self.force.fbult

        self.force.fbult = self.get_rbt(self.ybi) * self.get_ab()
        return self.force.fbult

    def get_fult(self):
        return self.get_fbult()

    def calculation_result(self):
        return self.force.f <= self.get_fult()


class ReinforcementMixin:
    def __init_mixin(self, data):
        super().__init_mixin(data)
        self.reinforcement = Reinforcement(
            reinforcement_class=data.get('reinforcement_class'),
            asw=data.get('asw'),
            sw=data.get('sw'),
        )

    def get_qsw(self):
        if hasattr(self, 'qsw'):
            return self.reinforcement.qsw

        self.reinforcement.qsw = (
            self.get_rsw(self.ybi) * self.reinforcement.asw
            / self.reinforcement.sw
        )
        return self.reinforcement.qsw

    def get_fswult(self):
        if hasattr(self, 'fswult'):
            return self.reinforcement.fswult

        self.reinforcement.fswult = 0.8 * self.get_qsw() * self.get_u()
        return self.reinforcement.fswult

    def get_fult(self):
        if self.get_fswult() < (self.get_fbult() * 0.25):
            return self.fbult
        fult = self.get_fswult() + self.get_fbult()
        if fult > (self.get_fbult() * 2):
            return self.get_fbult() * 2
        return fult
