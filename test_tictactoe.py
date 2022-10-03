from tictactoe import *
import pytest


class TestActions:
    def test_empty(self):
        board = initial_state()
        exptectedMoves = set([(i, j) for i in range(3) for j in range(3)])
        assert set(actions(board)) == exptectedMoves

    def test_oneSpot(self):
        board = [[X, O, X], [O, X, O], [EMPTY, X, O]]
        assert actions(board) == {(2, 0)}


class TestWinner:
    def test_X_wins_diag(self):
        board = [[X, O, X], [O, X, O], [EMPTY, EMPTY, X]]
        board2 = [[EMPTY, O, X], [O, X, EMPTY], [X, EMPTY, EMPTY]]
        assert winner(board) == X == winner(board2)

    def test_O_wins_diag(self):
        board = [[O, X, X], [X, O, O], [EMPTY, X, O]]
        board2 = [[X, X, O], [EMPTY, O, EMPTY], [O, X, EMPTY]]
        assert winner(board) == O
        assert winner(board2) == O

    def test_X_wins_row(self):
        board1 = [[X] * 3, [O, O, EMPTY], [EMPTY] * 3]
        board2 = [[O, O, EMPTY], [X] * 3, [EMPTY] * 3]
        board3 = [[O, O, EMPTY], [EMPTY] * 3, [X] * 3]
        assert winner(board1) == winner(board2) == winner(board3) == X

    def test_O_wins_row(self):
        board1 = [[O] * 3, [X, X, EMPTY], [EMPTY] * 3]
        board2 = [[X, X, EMPTY], [O] * 3, [EMPTY] * 3]
        board3 = [[X, X, EMPTY], [EMPTY] * 3, [O] * 3]
        assert winner(board1) == winner(board2) == winner(board3) == O

    def test_X_wins_col(self):
        T = X
        board1 = [[T, EMPTY, EMPTY]] * 3
        board2 = [[EMPTY, T, EMPTY]] * 3
        board3 = [[EMPTY, EMPTY, T]] * 3
        assert winner(board1) == winner(board2) == winner(board3) == T

    def test_O_wins_col(self):
        T = O
        board1 = [[T, EMPTY, EMPTY]] * 3
        board2 = [[EMPTY, T, EMPTY]] * 3
        board3 = [[EMPTY, EMPTY, T]] * 3
        assert winner(board1) == winner(board2) == winner(board3) == T

    def test_draw(self):
        board = [[X, O, X], [X, X, O], [O, X, O]]
        assert winner(board) is None


class TestPlayer:
    def test_initial(self):
        assert player(initial_state()) == X

    def test_X(self):
        board = [[X, O, X], [O, X, O], [EMPTY] * 3]
        assert player(board) == X

    def test_O(self):
        board = [[X, O, X], [O, X, O], [X, EMPTY, EMPTY]]
        assert player(board) == O


class TestResult:
    def test_invalid_OOB(self):
        board = initial_state()
        with pytest.raises(Exception):
            result(board, (3, 1))

    def test_space_taken(self):
        board = [[X, EMPTY, EMPTY], [EMPTY] * 3, [EMPTY] * 3]
        with pytest.raises(Exception):
            result(board, (0, 0))

    def test_X_move(self):
        board = initial_state()
        original_board = deepcopy(board)
        expected_board = [[X, EMPTY, EMPTY], [EMPTY] * 3, [EMPTY] * 3]
        assert result(board, (0, 0)) == expected_board
        assert board == original_board

    def test_O_move(self):
        board = [[X, EMPTY, EMPTY], [EMPTY] * 3, [EMPTY] * 3]
        original_board = deepcopy(board)
        expected_board = [[X, O, EMPTY], [EMPTY] * 3, [EMPTY] * 3]
        assert result(board, (0, 1)) == expected_board
        assert board == original_board


class TestMinimax:
    def test_X_win(self):
        board = [[X, X, EMPTY], [O, O, EMPTY], [EMPTY] * 3]
        assert minimax(board) == (0, 2)

    def test_block_O(self):
        board = [[O, O, EMPTY], [EMPTY, X, EMPTY], [EMPTY, EMPTY, X]]
        assert minimax(board) == (0, 2)

    def test_O_win(self):
        board = [[EMPTY, X, EMPTY], [O, O, EMPTY], [EMPTY, X, X]]
        assert minimax(board) == (1, 2)

    def test_block_X(self):
        board = [[X, O, EMPTY], [O, X, EMPTY], [EMPTY, X, EMPTY]]
        assert minimax(board) == (2, 2)
