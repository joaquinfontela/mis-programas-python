from Cell import Cell
from CellContainer import CellContainer
from time import sleep
from termcolor import colored


class SimpleSudokuSolver:

    def __init__(self):
        self.cells = []
        self.rows = [CellContainer() for i in range(9)]
        self.cols = [CellContainer() for i in range(9)]
        self.boxes = [CellContainer() for i in range(9)]
        self.currentStartCellNumber = 0
        self.lastCellUpdated = None

    def setSudoku(self, matrix) -> None:
        # TODO: matrix validations.
        for row_idx, row in enumerate(matrix):
            for col_idx, cell_value in enumerate(row):
                row = self.rows[row_idx]
                col = self.cols[col_idx]
                box_idx = self.getBoxIdxByRowAndCol(row_idx, col_idx)
                box = self.boxes[box_idx]
                cell = Cell(row, col, box, cell_value if cell_value else None)
                row.addCell(cell)
                col.addCell(cell)
                box.addCell(cell)
                self.cells.append(cell)

    def solve(self) -> None:
        self.printSudoku()
        print("")
        self.setPossibleValuesToCells()
        while not self.solved():
            sleep(0.5)
            currentCellNumber = self.currentStartCellNumber
            while not self.unsolvable(currentCellNumber):
                cell = self.cells[currentCellNumber]
                if not cell.hasValue() and self.completeCell(cell):
                    self.lastCellUpdated = currentCellNumber
                    self.currentStartCellNumber = self.getNewCellNumber(
                        currentCellNumber)
                    self.printSudoku()
                    print("")
                    break
                currentCellNumber = self.getNewCellNumber(currentCellNumber)

    def setPossibleValuesToCells(self):
        for cell in self.cells:
            cell.updatePossibleValuesForIntersectionOfRowColAndBox()

    def completeCell(self, cell) -> bool:
        intersecPossibleValues = cell.intersecPossibleValuesForRowColAndBox()
        if len(intersecPossibleValues) == 1:
            cell.setValue(list(intersecPossibleValues)[0])
            return True
        return False

    def getBoxIdxByRowAndCol(self, row, col) -> int:
        if row in [0, 1, 2]:
            if col in [0, 1, 2]:
                return 0
            elif col in [3, 4, 5]:
                return 1
            else:
                return 2
        elif row in [3, 4, 5]:
            if col in [0, 1, 2]:
                return 3
            elif col in [3, 4, 5]:
                return 4
            else:
                return 5
        else:
            if col in [0, 1, 2]:
                return 6
            elif col in [3, 4, 5]:
                return 7
            else:
                return 8

    def printSudoku(self) -> None:
        for cell_idx, cell in enumerate(self.cells):
            if cell_idx % 9 == 0:
                print("")
                print("|---|---|---|---|---|---|---|---|---|")
                print("|", end="")
            if cell_idx == self.lastCellUpdated:
                print(colored(" " + str(cell.val), "green"), end="")
            else:
                print(" " + str(cell.val) if cell.val else "  ", end="")
            print(" |", end="")
        print("\n|---|---|---|---|---|---|---|---|---|")

    def getNewCellNumber(self, currentCellNumber):
        if currentCellNumber == 80:
            return 0
        return currentCellNumber + 1

    def solved(self) -> bool:
        return False not in [cell.hasValue() for cell in self.cells]

    def unsolvable(self, currentCellNumber):
        return (self.currentStartCellNumber - 1 == currentCellNumber) or (
            self.currentStartCellNumber == 0 and currentCellNumber == 80)

    def getSudokuMatrix(self):
        matrix = []
        for row in self.rows:
            r = []
            for cell in row.cells:
                r.append(cell.val)
            matrix.append(r)
        return matrix
