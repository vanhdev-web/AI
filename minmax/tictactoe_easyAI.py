from easyAI import TwoPlayerGame, AI_Player, Negamax
from easyAI.Player import Human_Player


class TicTacToeGame(TwoPlayerGame):
    def __init__(self, players):
        self.players = players
        self.current_player = 1
        self.board = [0] * 9  # Trạng thái bàn cờ 3x3

    def possible_moves(self):
        return [index + 1 for index, cell in enumerate(self.board) if cell == 0]

    def make_move(self, move):
        self.board[int(move) - 1] = self.current_player

    def loss_condition(self):
        opponent = 3 - self.current_player
        winning_combinations = [
            [1, 2, 3], [4, 5, 6], [7, 8, 9],
            [1, 4, 7], [2, 5, 8], [3, 6, 9],
            [1, 5, 9], [3, 5, 7]
        ]
        return any(
            all(self.board[i - 1] == opponent for i in combo)
            for combo in winning_combinations
        )

    def is_over(self):
        return (self.possible_moves() == []) or self.loss_condition()

    def show(self):
        symbols = ['. ', 'O', 'X']
        print('\n' + '\n'.join([
            ' '.join([symbols[self.board[3 * row + col]] for col in range(3)])
            for row in range(3)
        ]))

    def scoring(self):
        return -100 if self.loss_condition() else 0


if __name__ == "__main__":
    ai_algo = Negamax(7)
    TicTacToeGame([Human_Player(), AI_Player(ai_algo)]).play()
