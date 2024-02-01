from dataclasses import dataclass, field
from typing import List, Dict, Set


def init_sizes():
    return {'s', 'm', 'l'}


@dataclass
class Trial:
    is_valid: bool
    numbers: List[int]
    grade: Dict[str, int]  # key de tip str si valoare de tip int
    sizes: Set = field(default_factory=init_sizes,
                       init=False)  # acest atribut nu apare la constructor si foloseste functia init_sizes ca sa ia valoarea implicita


t = Trial(False, [1, 2, 3], {'Andrei': 10, 'Ana': 9})
print(t)
