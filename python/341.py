from typing import List


class NestedInteger:
    def isInteger(self) -> bool: pass

    def getInteger(self) -> int: pass

    def getList(self) -> [NestedInteger]: pass


class NestedIterator:
    def __init__(self, nestedList: List[NestedInteger]):
        self.l = []
        self.addInteger(nestedList)

    def next(self) -> int:
        return self.l.pop(0)

    def hasNext(self) -> bool:
        return len(self.l) != 0

    def addInteger(self, nestedList: List[NestedInteger]) -> None:
        for ni in nestedList:
            if ni.isInteger():
                self.l.append(ni.getInteger())
            else:
                self.addInteger(ni.getList())
