# Technical test
# Problem : Write a program that accepts two lines
# (x1, x2) and (x3, x4) on the x-axis and returns
# whether the lines overlap or not.
# Goal : (1,5) and (2,6) overlaps but not (1,5) and (6,8).
# Assumptions :
# - We only accept numbers for points coordinates
# - x1 & x3 can be greater than x2 & x4 respectively
# Test cases :
# - Overlapping lines
# - Zero-length lines
# - Negative coordinates lines
# - Identical points
# - Invalid data entry
import unittest


def do_lines_overlap(line1, line2):
    # Helper function to check if all elements in a tuple are numbers
    def all_numbers(tup):
        return all(isinstance(n, int) for n in tup)

    # Check if inputs are tuples of numbers
    if not (isinstance(line1, tuple) and isinstance(line2, tuple) and
            len(line1) == 2 and len(line2) == 2 and
            all_numbers(line1) and all_numbers(line2)):
        raise ValueError("Inputs must be tuples of two numbers each.")

    x1, x2 = line1
    x3, x4 = line2

    # Check for overlap
    if x1 > x2 or x3 > x4:
        return max(x1, x3) >= min(x2, x4)
    return max(x1, x3) <= min(x2, x4)


class TestLineOverlap(unittest.TestCase):
    def test_overlap(self):
        self.assertTrue(do_lines_overlap((1, 5), (2, 6)))

    def test_no_overlap(self):
        self.assertFalse(do_lines_overlap((1, 5), (6, 8)))

    def test_inside(self):
        self.assertTrue(do_lines_overlap((1, 10), (2, 5)))

    def test_common_endpoint(self):
        self.assertTrue(do_lines_overlap((1, 5), (5, 8)))

    def test_zero_length(self):
        self.assertFalse(do_lines_overlap((3, 3), (1, 2)))

    def test_identical_point(self):
        self.assertTrue(do_lines_overlap((2, 2), (2, 2)))

    def test_negative_coordinates(self):
        self.assertTrue(do_lines_overlap((-5, -1), (-3, 0)))

    def test_reverse_order(self):
        self.assertTrue(do_lines_overlap((5, 1), (2, 6)))

    def test_invalid_input(self):
        with self.assertRaises(ValueError):
            do_lines_overlap((1, "a"), (2, 3))

    def test_invalid_input_float(self):
        with self.assertRaises(ValueError):
            do_lines_overlap((1, 2), (2.1, 3))

    def test_invalid_tuple_size(self):
        with self.assertRaises(ValueError):
            do_lines_overlap((1, 2, 3), (4, 5))

    def test_invalid_not_tuple(self):
        with self.assertRaises(ValueError):
            do_lines_overlap("test", (1, 2))


if __name__ == '__main__':
    unittest.main()
