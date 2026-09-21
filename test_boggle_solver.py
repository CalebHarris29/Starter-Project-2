"""
Name: Caleb Harris
SID: 003091457

Boggle Solver Black-Box Tests
Tests the Boggle solver using 25 test cases
created from the Category Partition Method.
"""

import unittest
from boggle_solver import Boggle


class TestBoggleSolver(unittest.TestCase):

    # -----------------------------
    # Normal Boggle cases
    # -----------------------------

    # Test 1: Find one valid 3-letter word
    def test_01_one_valid_word(self):
        grid = [
            ["A", "B"],
            ["C", "D"]
        ]
        dictionary = ["ACB"]

        game = Boggle(grid, dictionary)

        self.assertEqual(game.getSolution(), ["ACB"])

    # Test 2: Find a valid word longer than 3 letters
    def test_02_longer_word(self):
        grid = [
            ["A", "B"],
            ["C", "D"]
        ]
        dictionary = ["ABDC"]

        game = Boggle(grid, dictionary)

        self.assertEqual(game.getSolution(), ["ABDC"])

    # Test 3: Find multiple valid words
    def test_03_multiple_words(self):
        grid = [
            ["C", "A"],
            ["R", "T"]
        ]
        dictionary = ["CAT", "CAR", "RAT"]

        game = Boggle(grid, dictionary)

        self.assertCountEqual(
            game.getSolution(),
            ["CAT", "CAR", "RAT"]
        )

    # Test 4: Dictionary contains no words on the grid
    def test_04_no_matching_words(self):
        grid = [
            ["A", "B"],
            ["C", "D"]
        ]
        dictionary = ["DOG", "FISH"]

        game = Boggle(grid, dictionary)

        self.assertEqual(game.getSolution(), [])

    # Test 5: Empty dictionary should return empty list
    def test_05_empty_dictionary(self):
        grid = [
            ["A", "B"],
            ["C", "D"]
        ]
        dictionary = []

        game = Boggle(grid, dictionary)

        self.assertEqual(game.getSolution(), [])


    # -----------------------------
    # Word length
    # -----------------------------

    # Test 6: A 1-letter word is too short
    def test_06_one_letter_word(self):
        grid = [
            ["A", "B"],
            ["C", "D"]
        ]
        dictionary = ["A"]

        game = Boggle(grid, dictionary)

        self.assertEqual(game.getSolution(), [])

    # Test 7: A 2-letter word is too short
    def test_07_two_letter_word(self):
        grid = [
            ["A", "B"],
            ["C", "D"]
        ]
        dictionary = ["AB"]

        game = Boggle(grid, dictionary)

        self.assertEqual(game.getSolution(), [])

    # Test 8: A 3-letter word meets the minimum length
    def test_08_three_letter_word(self):
        grid = [
            ["C", "A"],
            ["X", "T"]
        ]
        dictionary = ["CAT"]

        game = Boggle(grid, dictionary)

        self.assertEqual(game.getSolution(), ["CAT"])


    # -----------------------------
    # Movement directions
    # -----------------------------

    # Test 9: Find a horizontal word
    def test_09_horizontal_word(self):
        grid = [
            ["C", "A", "T"],
            ["X", "X", "X"],
            ["X", "X", "X"]
        ]
        dictionary = ["CAT"]

        game = Boggle(grid, dictionary)

        self.assertEqual(game.getSolution(), ["CAT"])

    # Test 10: Find a vertical word
    def test_10_vertical_word(self):
        grid = [
            ["C", "X", "X"],
            ["A", "X", "X"],
            ["T", "X", "X"]
        ]
        dictionary = ["CAT"]

        game = Boggle(grid, dictionary)

        self.assertEqual(game.getSolution(), ["CAT"])

    # Test 11: Find a diagonal word
    def test_11_diagonal_word(self):
        grid = [
            ["C", "X", "X"],
            ["X", "A", "X"],
            ["X", "X", "T"]
        ]
        dictionary = ["CAT"]

        game = Boggle(grid, dictionary)

        self.assertEqual(game.getSolution(), ["CAT"])

    # Test 12: Find a word using different directions
    def test_12_mixed_directions(self):
        grid = [
            ["C", "A", "X"],
            ["X", "T", "X"],
            ["X", "S", "X"]
        ]
        dictionary = ["CATS"]

        game = Boggle(grid, dictionary)

        self.assertEqual(game.getSolution(), ["CATS"])


    # -----------------------------
    # Tile reuse and adjacency
    # -----------------------------

    # Test 13: The same tile cannot be used twice
    def test_13_cannot_reuse_tile(self):
        grid = [
            ["A", "B"],
            ["C", "D"]
        ]
        dictionary = ["ABA"]

        game = Boggle(grid, dictionary)

        self.assertEqual(game.getSolution(), [])

    # Test 14: Different tiles with the same letter can be used
    def test_14_same_letter_different_tiles(self):
        grid = [
            ["A", "B"],
            ["A", "C"]
        ]
        dictionary = ["ABA"]

        game = Boggle(grid, dictionary)

        self.assertEqual(game.getSolution(), ["ABA"])

    # Test 15: Word is in dictionary but letters are not all on grid
    def test_15_word_not_on_grid(self):
        grid = [
            ["A", "B"],
            ["C", "D"]
        ]
        dictionary = ["CAT"]

        game = Boggle(grid, dictionary)

        self.assertEqual(game.getSolution(), [])

    # Test 16: Letters exist but are not adjacent
    def test_16_letters_not_adjacent(self):
        grid = [
            ["C", "X", "A"],
            ["X", "X", "X"],
            ["T", "X", "X"]
        ]
        dictionary = ["CAT"]

        game = Boggle(grid, dictionary)

        self.assertEqual(game.getSolution(), [])


    # -----------------------------
    # Special tiles
    # -----------------------------

    # Test 17: Qu counts as one tile with two letters
    def test_17_qu_tile(self):
        grid = [
            ["Qu", "A"],
            ["X", "T"]
        ]
        dictionary = ["QUA"]

        game = Boggle(grid, dictionary)

        self.assertEqual(game.getSolution(), ["QUA"])

    # Test 18: St counts as one tile with two letters
    def test_18_st_tile(self):
        grid = [
            ["St", "A"],
            ["X", "R"]
        ]
        dictionary = ["STAR"]

        game = Boggle(grid, dictionary)

        self.assertEqual(game.getSolution(), ["STAR"])

    # Test 19: Ie counts as one tile with two letters
    def test_19_ie_tile(self):
        grid = [
            ["Ie", "A"],
            ["X", "R"]
        ]
        dictionary = ["IEA"]

        game = Boggle(grid, dictionary)

        self.assertEqual(game.getSolution(), ["IEA"])

    # Test 20: Qu + A makes a 3-letter word using only 2 tiles
    def test_20_special_tile_word_length(self):
        grid = [
            ["Qu", "A"],
            ["X", "X"]
        ]
        dictionary = ["QUA"]

        game = Boggle(grid, dictionary)

        self.assertEqual(game.getSolution(), ["QUA"])


    # -----------------------------
    # Different grid sizes
    # -----------------------------

    # Test 21: A 1x1 grid cannot make a normal 3-letter word
    def test_21_one_by_one_grid(self):
        grid = [["A"]]
        dictionary = ["AAA"]

        game = Boggle(grid, dictionary)

        self.assertEqual(game.getSolution(), [])

    # Test 22: Test the 4x4 example from the assignment
    def test_22_four_by_four_grid(self):
        grid = [
            ["A", "B", "C", "D"],
            ["E", "F", "G", "H"],
            ["Ie", "J", "K", "L"],
            ["A", "B", "C", "D"]
        ]

        dictionary = [
            "ABEF",
            "AFJIEEB",
            "DGKD",
            "DGKA"
        ]

        game = Boggle(grid, dictionary)

        self.assertCountEqual(
            game.getSolution(),
            ["ABEF", "AFJIEEB", "DGKD"]
        )


    # -----------------------------
    # Invalid inputs
    # -----------------------------

    # Test 23: Grid must be square
    def test_23_non_square_grid(self):
        grid = [
            ["A", "B", "C"],
            ["D", "E"]
        ]
        dictionary = ["ABC"]

        game = Boggle(grid, dictionary)

        self.assertEqual(game.getSolution(), [])

    # Test 24: Grid must be a 2D list
    def test_24_invalid_grid_type(self):
        grid = "ABC"
        dictionary = ["ABC"]

        game = Boggle(grid, dictionary)

        self.assertEqual(game.getSolution(), [])

    # Test 25: Dictionary must be a list
    def test_25_invalid_dictionary_type(self):
        grid = [
            ["A", "B"],
            ["C", "D"]
        ]
        dictionary = "ABC"

        game = Boggle(grid, dictionary)

        self.assertEqual(game.getSolution(), [])


if __name__ == "__main__":
    unittest.main()