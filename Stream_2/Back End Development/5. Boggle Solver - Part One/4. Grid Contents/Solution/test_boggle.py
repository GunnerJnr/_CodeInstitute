import unittest
import boggle
from string import ascii_uppercase


class TestBoggle(unittest.TestCase):
    def test_Is_This_Thing_On(self):
        self.assertEquals(1, boggle.check())


def test_can_create_an_empty_grid(self):
    grid = boggle.make_grid(0, 0)
    self.assertEquals(len(grid), 0)


def test_grid_size_is_width_times_height(self):
    grid = boggle.make_grid(2, 3)
    self.assertEquals(len(grid), 6)


def test_grid_coordinates(self):
    grid = boggle.make_grid(2, 2)
    self.assertTrue((0, 0) in grid)
    self.assertTrue((0, 1) in grid)
    self.assertTrue((1, 0) in grid)
    self.assertTrue((1, 1) in grid)
    self.assertTrue((2, 2) not in grid)


def test_grid_is_filled_with_letters(self):
    grid = boggle.make_grid(2, 3)
    for L in grid.values():
        self.assertTrue(L in ascii_uppercase)