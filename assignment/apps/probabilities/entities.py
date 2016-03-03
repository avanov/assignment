from typing import Optional, List
from assignment.server.entities import BaseEntity


class Person(BaseEntity):
    FIELDS = ('id', 'name', 'traits')

    def __init__(self,
                 name: str,
                 traits: List[int],
                 id: Optional[int] = None):
        super(Person, self).__init__(
            name=name,
            traits=traits,
            id=id
        )

class Trait(BaseEntity):
    FIELDS = ('id', 'name')

    def __init__(self,
                 name: str,
                 id: Optional[int] = None):
        super(Trait, self).__init__(name=name, id=id)

