from typing import Optional, List
from assignment.server.entities import BaseEntity


class Person(BaseEntity):

    def __init__(self,
                 traits: List[int],
                 id: Optional[int] = None):
        super(BaseEntity, self).__init__(traits=traits,
                                         id=id)

class Trait(BaseEntity):
    pass
