from game.board import Board
from game.players import Player
from tools.display import show_welcome, show_board, announce_result, prompt_restart
from tools.logger import Logger

def main():
    name1 = input("Please enter Player 1 name: ")
    name2 = input("Please enter Player 2 name: ")

    player1 = Player(name1, 'X')
    player2 = Player(name2, 'O')

    show_welcome(player1.name, player2.name)

    play_again = True
    game_number = 1

    while play_again:
        board = Board()
        logger = Logger(game_number, player1, player2)
        logger.log_players()
        current_player = player1
        show_board(board)

        while True:
            move = current_player.get_move(board)
            if board.place_marker(move, current_player.marker):
                logger.log_move(current_player, move, board)
                show_board(board)

                if board.check_winner(current_player.marker):
                    announce_result(f"Congratulations, {current_player.name}! You win!")
                    logger.log_result(f"{current_player.name} wins!")
                    break
                elif board.is_draw():
                    announce_result("It's a draw!")
                    logger.log_result("Draw")
                    break

                current_player = player2 if current_player == player1 else player1
            else:
                print("Invalid move. Try again.")

        play_again = prompt_restart()
        game_number += 1

if __name__ == "__main__":
    main()
