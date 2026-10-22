"""Tests des règles de jeu, exemples de l'énoncé et cas limites."""
import contextlib
import importlib.util
import io
from pathlib import Path
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]


def load(path):
    spec = importlib.util.spec_from_file_location(Path(path).stem, ROOT / path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


ttt = load('MiniProjects/tic_tac_toe.py')
hangman = load('MiniProjects/hangman.py')
c = load('Challenges/challenges.py')
daily = load('DailyChallenge/challenges.py')
pairs = load('DailyChallenge/advanced_algorithm.py')


class Day5Tests(unittest.TestCase):
    def test_all_winning_lines(self):
        lines = [[(r, col) for col in range(3)] for r in range(3)]
        lines += [[(r, col) for r in range(3)] for col in range(3)]
        lines += [[(i, i) for i in range(3)], [(i, 2-i) for i in range(3)]]
        for player in ('X', 'O'):
            for line in lines:
                board = [[' '] * 3 for _ in range(3)]
                for row, col in line:
                    board[row][col] = player
                self.assertTrue(ttt.check_win(board, player))
                self.assertFalse(ttt.check_tie(board))

    def test_full_tie_and_winning_game(self):
        for moves, expected in [
            ([1,1,2,1,1,2,2,2,1,3], 'X'),
            ([1,1,1,2,1,3,2,2,2,1,2,3,3,2,3,1,3,3], 'tie'),
        ]:
            with patch('builtins.input', side_effect=map(str, moves)), contextlib.redirect_stdout(io.StringIO()):
                self.assertEqual(ttt.play(), expected)

    def test_invalid_move(self):
        ttt.board = [['X', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
        with patch('builtins.input', side_effect=['oops','0','4','1','1','2','3']), contextlib.redirect_stdout(io.StringIO()):
            self.assertEqual(ttt.player_input('O'), (1, 2))

    def test_hangman_win_repeat_and_loss(self):
        self.assertEqual(hangman.masked_word('credit card', ['c', 'r']), 'cr**** c*r*')
        for word, guesses, expected in [('beach', ['', 'bb', '1', 'B', 'b', 'e', 'a', 'c', 'h'], True), ('python', list('abcdef'), False), ('credit card', list('credita'), True)]:
            with patch.object(hangman.random, 'choice', return_value=word), patch('builtins.input', side_effect=guesses), contextlib.redirect_stdout(io.StringIO()):
                self.assertEqual(hangman.play(), expected)

    def test_challenge_examples(self):
        self.assertEqual(c.my_sum([1,5,4,2]), 12)
        self.assertEqual(c.find_max([-5,-2,-7]), -2)
        self.assertEqual(c.factorial(0), 1)
        self.assertEqual(c.factorial(4), 24)
        self.assertEqual(c.list_count(['a','a','t','o'],'a'), 2)
        self.assertEqual(c.norm([1,2,2]), 3)
        for items in ([], [1], [7,6,5,5,2,0], [2,3,3,3]):
            self.assertTrue(c.is_mono(items))
        self.assertFalse(c.is_mono([1,2,0,4]))
        self.assertEqual(c.sum_over_k('Do or do not there is no try',2), 3)
        self.assertEqual(c.dict_avg({'a':1,'b':2,'c':8,'d':1}),3)
        self.assertEqual(c.common_div(10,20),[2,5,10])
        self.assertTrue(c.is_prime(11))
        for n in (-1,0,1,9): self.assertFalse(c.is_prime(n))
        self.assertEqual(c.type_count(a=1,b='string',c=1.0,d=True,e=False), {'int':1,'str':1,'float':1,'bool':2})
        self.assertEqual(c.hide_password('mypassword'), '*' * 10)

    def test_split_matches_python(self):
        for text in ('', '  a\t b\n', ',a,,b,', 'a<>b<><>'):
            for separator in (None, ',', '<>'):
                self.assertEqual(c.custom_split(text, separator), text.split(separator))
        with self.assertRaises(ValueError): c.custom_split('abc','')

    def test_daily(self):
        self.assertEqual(daily.sort_words('without,hello,bag,world'), 'bag,hello,without,world')
        for sentence, expected in [("Margaret's toy is a pretty doll.", "Margaret's"), ('A thing of beauty is a joy forever.', 'forever.'), ('Forgetfulness is by all means powerless!', 'Forgetfulness'), ('cat dog','cat'), ('','')]:
            self.assertEqual(daily.longest_word(sentence), expected)

    def test_pairs_against_brute_force(self):
        numbers = [0, 1, 2, 2, 3, 4, -1]
        expected = sorted({tuple(sorted((a,b))) for i,a in enumerate(numbers) for b in numbers[i+1:] if a+b == 4})
        self.assertEqual(pairs.find_pairs(numbers,4),expected)
        self.assertEqual(pairs.find_pairs([1864],3728),[])
        self.assertEqual(pairs.find_pairs([1864,1864],3728),[(1864,1864)])


if __name__ == '__main__':
    unittest.main()
