class Game:
    """
    """
    def __init__(self):
        self.TIME_CONTROL = ["30min", "15min", "10_min", "3plus1"]
        self.ELO = ["800", "1500", "2000", "SUPER_GM"]
        self.CLOCK = 0
        self.over = False
        self.board = Board()
    
    def initBoard(self, board):
        board.WHITE_SQUARES{"A2": Pawn(clr="white"), "A4": Empty, "A6": Empty, "A8": Rook(clr="black"),
                              "B1": Knight(clr="white"), "B3": Empty, "B5": Empty, "B7": Pawn(clr="black"),
                              "C2": Pawn(clr="white"), "C4": Empty, "C6": Empty, "C8": Bishop(clr="black"),
                              "D1": "", "D3": "", "D5": "", "D7": "",
                              "E2": "", "E4": "", "E6": "", "E8": "",
                              "F1": "", "F3": "", "F5": "", "F7": "",
                              "G2": "", "G4": "", "G6": "", "G8": "",
                              "H1": "", "H3": "", "H5": "", "H7": ""}

class Board:
    """
    """
    def __init__(self):
        self.WHITE_SQUARES = {"A2": "", "A4": "", "A6": "", "A8": "",
                              "B1": "", "B3": "", "B5": "", "B7": "",
                              "C2": "", "C4": "", "C6": "", "C8": "",
                              "D1": "", "D3": "", "D5": "", "D7": "",
                              "E2": "", "E4": "", "E6": "", "E8": "",
                              "F1": "", "F3": "", "F5": "", "F7": "",
                              "G2": "", "G4": "", "G6": "", "G8": "",
                              "H1": "", "H3": "", "H5": "", "H7": ""}
        self.BLACK_SQUARES = {"A1": "", "A3": "", "A5": "", "A7": "",
                              "B2": "", "B4": "", "B6": "", "B8": "",
                              "C1": "", "C3": "", "C5": "", "C7": "",
                              "D2": "", "D4": "", "D6": "", "D8": "",
                              "E1": "", "E3": "", "E5": "", "E7": "",
                              "F2": "", "F4": "", "F6": "", "F8": "",
                              "G1": "", "G3": "", "G5": "", "G7": "",
                              "H2": "", "H4": "", "H6": "", "H8": ""}

class Pawn:
    """
    """
    def __init__(self, clr: str):
        self.loc = ""
        self.color = clr

class Rook:
    """
    """
    def __init__(self, clr: str):
        self.loc = ""
        self.color = clr

class Knight:
    """
    """
    def __init__(self, clr: str):
        self.loc = ""
        self.color = clr

class Bishop:
    """
    """
    def __init__(self, clr: str):
        self.loc = ""
        self.color = clr

class Queen:
    """
    """
    def __init__(self, clr: str):
        self.loc = ""
        self.color = clr

class King:
    """
    """
    def __init__(self, clr: str):
        self.loc = ""
        self.color = clr

class Empty:
    """
    """
    def __init__(self):
        self.loc = ""

if __name__ == "__main__":
    game = Game()
    while not game.over:
        
