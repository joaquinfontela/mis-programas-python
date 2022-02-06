class CellContainer:

    def __init__(self):
        self.cells = []

    def addCell(self, cell) -> None:
        self.cells.append(cell)

    def missingNumbers(self) -> set:
        return set([1, 2, 3, 4, 5, 6, 7, 8, 9]) - set([cell.val for cell in self.cells])
