class Game:
    """
    """
    def __init__(self):
        self.TIME_CONTROL = ["30min", "15min", "10_min", "3plus1"]
        self.ELO = ["500", "1500", "2000", "2500", "SUPER_GM"]
        self.CLOCK = 0
        self.over = False
        self.board = Board()
    
    def initBoard(self):
        self.board.SQUARES = {"A8": Rook(clr="black"), "B8": Knight(clr="black"), "C8": Bishop(clr="black"), "D8": Queen(clr="black"), "E8": King(clr="black"), "F8": Bishop(clr="black"), "G8": Knight(clr="black"), "H8": Rook(clr="black"),
                            "A7": Pawn(clr="black"), "B7": Pawn(clr="black"), "C7": Pawn(clr="black"), "D7": Pawn(clr="black"), "E7": Pawn(clr="black"), "F7": Pawn(clr="black"), "G7": Pawn(clr="black"), "H7": Pawn(clr="black"),
                            "A6": Empty(), "B6": Empty(), "C6": Empty(), "D6": Empty(), "E6": Empty(), "F6": Empty(), "G6": Empty(), "H6": Empty(),
                            "A5": Empty(), "B5": Empty(), "C5": Empty(), "D5": Empty(), "E5": Empty(), "F5": Empty(), "G5": Empty(), "H5": Empty(),
                            "A4": Empty(), "B4": Empty(), "C4": Empty(), "D4": Empty(), "E4": Empty(), "F4": Empty(), "G4": Empty(), "H4": Empty(),
                            "A3": Empty(), "B3": Empty(), "C3": Empty(), "D3": Empty(), "E3": Empty(), "F3": Empty(), "G3": Empty(), "H3": Empty(),
                            "A2": Pawn(clr="white"), "B2": Pawn(clr="white"), "C2": Pawn(clr="white"), "D2": Pawn(clr="white"), "E2": Pawn(clr="white"), "F2": Pawn(clr="white"), "G2": Pawn(clr="white"), "H2": Pawn(clr="white"),
                            "A1": Rook(clr="white"), "B1": Knight(clr="white"), "C1": Bishop(clr="white"), "D1": Queen(clr="white"), "E1": King(clr="white"), "F1": Bishop(clr="white"), "G1": Knight(clr="white"), "H1": Rook(clr="white")}
    
    def test(self) -> None:
        rowCounter = 0
        for i in self.board.SQUARES:
            if rowCounter > 7:
                print("\n")
                rowCounter = 0
                print(self.board.SQUARES[i].testid, end="")
                rowCounter += 1
            else:
                print(self.board.SQUARES[i].testid, end="")
                rowCounter += 1

class Board:
    """
    """
    def __init__(self):
        self.SQUARES = {}

class Pawn:
    """
    """
    def __init__(self, clr: str):
        self.loc = ""
        self.color = clr
        self.testid = "p"

class Rook:
    """
    """
    def __init__(self, clr: str):
        self.loc = ""
        self.color = clr
        self.testid = "r"

class Knight:
    """
    """
    def __init__(self, clr: str):
        self.loc = ""
        self.color = clr
        self.testid = "N"

class Bishop:
    """
    """
    def __init__(self, clr: str):
        self.loc = ""
        self.color = clr
        self.testid = "b"

class Queen:
    """
    """
    def __init__(self, clr: str):
        self.loc = ""
        self.color = clr
        self.testid = "Q"

class King:
    """
    """
    def __init__(self, clr: str):
        self.loc = ""
        self.color = clr
        self.testid = "K"

class Empty:
    """
    """
    def __init__(self):
        self.loc = ""
        self.testid = "_"

class Moves:
    """
    """
    def __init__(self):
        return
    
   # def capture():
        

if __name__ == "__main__":
    game = Game()
    #while not game.over:
    game.initBoard()
    game.test()
