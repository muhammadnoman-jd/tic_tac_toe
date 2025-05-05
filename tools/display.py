def show_welcome(player1, player2):
    print(f"Welcome, {player1} and {player2}!")

def show_board(board):
    print("\nCurrent Board:")
    board.display()

def announce_result(result):
    print(result)

def prompt_restart():
    answer = input("Would you like to play again? (yes/no): ").lower()
    return answer == "yes"
