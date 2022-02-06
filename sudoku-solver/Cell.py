from CellContainer import CellContainer


class Cell:

    def __init__(self, row, col, box, val):
        self.row: CellContainer = row
        self.col: CellContainer = col
        self.box: CellContainer = box
        self.val = val

    def hasValue(self) -> bool:
        return bool(self.val)

    def setValue(self, val) -> None:
        self.val = val

    def intersecPossibleValuesForRowColAndBox(self) -> set:
        return self.row.missingNumbers() & self.col.missingNumbers() & self.box.missingNumbers()
