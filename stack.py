from typing import TypeVar, Generic
T = TypeVar("T")

class Stack(Generic[T]):
    def __init__(self, items = [T]):
        self.items = items

    def push(self, item : T):
        self.items.append(item)

    def pop(self):
        print(self.items[-1])
        self.items.pop[-1]
