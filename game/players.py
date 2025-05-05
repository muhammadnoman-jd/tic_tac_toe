class Player:
    def __init__(self, name, marker):
        self.name = name
        self.marker = marker

    def get_move(self, board):
        while True:
            try:
                position = int(input(f"{self.name}'s Turn ({self.marker}): Enter a position (1-9): "))
                if 1 <= position <= 9:
                    return position
                else:
                    print("Position must be between 1 and 9.")
            except ValueError:
                print("Please enter a valid number.")
