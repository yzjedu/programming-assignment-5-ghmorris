import unittest
from assignment import create_2d_list, sum_of_row, max_in_column, flatten_matrix

class TestAdvancedListOperations(unittest.TestCase):

    def setUp(self):
        self.matrix = [
            [1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 12],
            [13, 14, 15, 16]
        ]
        self.flat_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

    def test_create_2d_list(self):
        matrix = create_2d_list(4, 4)
        self.assertEqual(matrix, [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])

    def test_sum_of_row(self):
        result = sum_of_row(self.matrix, 2)
        self.assertEqual(result, 42)

    def test_max_in_column(self):
        result = max_in_column(self.matrix, 3)
        self.assertEqual(result, 16)

    def test_flatten_matrix(self):
        result = flatten_matrix(self.matrix)
        self.assertEqual(result, self.flat_list)

if __name__ == "__main__":
    unittest.main()