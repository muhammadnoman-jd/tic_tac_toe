from pathlib import Path
from datetime import datetime

class Logger:
    def __init__(self, game_number, player1, player2):
        self.game_dir = Path("tic_tac_toe/game_log") / f"game{game_number}"
        self.game_dir.mkdir(parents=True, exist_ok=True)
        self.log_file = self.game_dir / "log.txt"
        self.move_counter = 1
        self.player1 = player1
        self.player2 = player2
        with self.log_file.open("w") as f:
            f.write(f"Game {game_number} Log\n")
            f.write(f"Players:\n- {player1.name} ({player1.marker})\n- {player2.name} ({player2.marker})\n")
            f.write(f"First move: {player1.name}\n\nMoves:\n")

    def log_players(self):
        pass  # Already done in __init__

    def log_move(self, player, position, board):
        with self.log_file.open("a") as f:
            f.write(f"Move {self.move_counter}: {player.name} -> Position {position}\n")
            f.write("Board After Move:\n")
            f.write(board.get_board_state() + "\n\n")
        self.move_counter += 1

    def log_result(self, result):
        with self.log_file.open("a") as f:
            f.write(f"Result: {result}\n")
