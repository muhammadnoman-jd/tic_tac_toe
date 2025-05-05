class Board:
    def __init__(self):
        self.board = [str(i) for i in range(1, 10)]

    def display(self):
        print(f"{self.board[0]} | {self.board[1]} | {self.board[2]}")
        print("-" * 11)
        print(f"{self.board[3]} | {self.board[4]} | {self.board[5]}")
        print("-" * 11)
        print(f"{self.board[6]} | {self.board[7]} | {self.board[8]}")

    def place_marker(self, position, marker):
        if self.board[position - 1].isdigit():
            self.board[position - 1] = marker
            return True
        return False

    def check_winner(self, marker):
        b = self.board
        return any([
            b[0] == b[1] == b[2] == marker,
            b[3] == b[4] == b[5] == marker,
            b[6] == b[7] == b[8] == marker,
            b[0] == b[3] == b[6] == marker,
            b[1] == b[4] == b[7] == marker,
            b[2] == b[5] == b[8] == marker,
            b[0] == b[4] == b[8] == marker,
            b[2] == b[4] == b[6] == marker
        ])

    def is_draw(self):
        return all(pos in ['X', 'O'] for pos in self.board)

    def get_board_state(self):
        return "\n".join([
            f"{self.board[0]} | {self.board[1]} | {self.board[2]}",
            "-" * 11,
            f"{self.board[3]} | {self.board[4]} | {self.board[5]}",
            "-" * 11,
            f"{self.board[6]} | {self.board[7]} | {self.board[8]}"
        ])
