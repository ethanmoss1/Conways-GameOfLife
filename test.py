import unittest
from main import Life


class Test(unittest.TestCase):
    def test_inside_grid(self):
        print(life.grid_size)
        # inside grid takes X and Y
        self.assertTrue(life.inside_grid(1, 1))
        self.assertFalse(life.inside_grid(-1, 1))
        self.assertTrue(life.inside_grid(100, 200))


if __name__ == '__main__':
    life = Life((800, 800), 2)  # produces a grid of 400 / 400
    unittest.main()
