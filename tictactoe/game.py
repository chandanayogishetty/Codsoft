import math
import random

class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]
        self.current_winner = None

    def print_board(self):
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')

    @staticmethod
    def print_board_nums():
        number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in number_board:
            print('| ' + ' | '.join(row) + ' |')

    def available_moves(self):
        return [i for i, spot in enumerate(self.board) if spot == ' ']

    def make_move(self, pos, letter):
        if self.board[pos] == ' ':
            self.board[pos] = letter
            if self.winner(pos, letter):
                self.current_winner = letter
            return True
        return False

    def winner(self, pos, letter):
        row_ind, col_ind = pos // 3, pos % 3
        row = self.board[row_ind*3:(row_ind+1)*3]
        column = [self.board[col_ind+i*3] for i in range(3)]
        if all([s == letter for s in row]) or all([s == letter for s in column]):
            return True
        if pos % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]]
            diagonal2 = [self.board[i] for i in [2, 4, 6]]
            if all([s == letter for s in diagonal1]) or all([s == letter for s in diagonal2]):
                return True
        return False

def minimax(board, depth, alpha, beta, maximizing):
    if board.current_winner == 'O':
        return {'position': None, 'score': 1 * (board.board.count(' ') + 1)}
    elif board.current_winner == 'X':
        return {'position': None, 'score': -1 * (board.board.count(' ') + 1)}
    elif not ' ' in board.board:
        return {'position': None, 'score': 0}
    if maximizing:
        max_eval = {'position': None, 'score': -math.inf}
        for move in board.available_moves():
            board.make_move(move, 'O')
            sim_score = minimax(board, depth + 1, alpha, beta, False)
            board.board[move] = ' '
            board.current_winner = None
            sim_score['position'] = move
            if sim_score['score'] > max_eval['score']:
                max_eval = sim_score
            alpha = max(alpha, sim_score['score'])
            if beta <= alpha:
                break
        return max_eval
    else:
        min_eval = {'position': None, 'score': math.inf}
        for move in board.available_moves():
            board.make_move(move, 'X')
            sim_score = minimax(board, depth + 1, alpha, beta, True)
            board.board[move] = ' '
            board.current_winner = None
            sim_score['position'] = move
            if sim_score['score'] < min_eval['score']:
                min_eval = sim_score
            beta = min(beta, sim_score['score'])
            if beta <= alpha:
                break
        return min_eval

class HumanPlayer:
    def __init__(self, letter):
        self.letter = letter

    def get_move(self, game):
        valid_square = False
        while not valid_square:
            pos = input('Human: '+self.letter +'\'s turn. Input move (0-8): ')
            try:
                val = int(pos)
                if val in game.available_moves():
                    valid_square = True
                    return val
                else:
                    print('Invalid position. Try again.')
            except ValueError:
                print('Invalid input. Try again.')

class AIPlayer:
    def __init__(self, letter):
        self.letter = letter

    def get_move(self, game):
        if len(game.available_moves()) == 9:
            pos = random.choice(game.available_moves())
        else:
            pos = minimax(game, 0, -math.inf, math.inf, True)['position']
        return pos

def play(game, x_player, o_player, print_game=True):
    if print_game:
        game.print_board_nums()
    letter = 'X'
    while ' ' in game.board:
        if letter == 'O':
            pos = o_player.get_move(game)
        else:
            pos = x_player.get_move(game)
        if game.make_move(pos, letter):
            if print_game:
                if(letter=='O'):
                    print('AI: '+letter + f' makes a move to position {pos}')
                else:
                    print('Human: '+letter + f' makes a move to position {pos}')
                game.print_board()
                print('')
            if game.current_winner:
                if print_game:
                    if(letter=='O'):
                        print('AI'+ ' wins!')
                    else:
                        print('Human '+ ' wins!')
                return letter
            letter = 'O' if letter == 'X' else 'X'
    if print_game:
        print('It\'s a tie!')

if __name__ == '__main__':
    t = TicTacToe()
    x_player = HumanPlayer('X')
    o_player = AIPlayer('O')
    play(t, x_player, o_player)
