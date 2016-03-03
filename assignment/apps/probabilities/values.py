from .entities import Person


class Probability:
    __slots__ = ('person', 'probability')

    def __init__(self, person: Person, probability: float):
        self.person = person
        self.probability = probability
