from CellContainer import CellContainer


class Cell:

    def __init__(self, row, col, box, val):
        self.row: CellContainer = row
        self.col: CellContainer = col
        self.box: CellContainer = box
        self.val = val
        self.possibleValues = set([1, 2, 3, 4, 5, 6, 7, 8, 9])

    def hasValue(self) -> bool:
        return bool(self.val)

    def setValue(self, val) -> None:
        self.val = val
        self.possibleValues = set([val])

    def intersecPossibleValuesForRowColAndBox(self) -> set:
        return self.row.missingNumbers() & self.col.missingNumbers() & self.box.missingNumbers()

    def updatePossibleValuesForIntersectionOfRowColAndBox(self) -> None:
        self.possibleValues = self.row.missingNumbers() & self.col.missingNumbers()\
            & self.box.missingNumbers()
