import unittest

from models.bfs import is_valid_move, bfs, read_input_file, write_output_file


class BfsTest(unittest.TestCase):
    def test_is_valid_move(self):
        matrix = [[1, 0, 1], [1, 1, 1], [0, 1, 1]]
        visited_cells = [[False, False, False], [False, False, False], [False, False, False]]
        self.assertTrue(is_valid_move(matrix, visited_cells, 0, 0))
        self.assertFalse(is_valid_move(matrix, visited_cells, 0, 1))
        self.assertFalse(is_valid_move(matrix, visited_cells, 2, 0))

    def test_read_input_file(self):
        start_point, end_point, matrix = read_input_file('../input.txt')
        self.assertEqual(start_point, (0, 0))
        self.assertEqual(end_point, (7, 5))
        self.assertEqual(len(matrix), 10)
        self.assertEqual(len(matrix[0]), 10)

    def test_write_output_file(self):
        write_output_file('../output.txt', 12)
        with open('../output.txt', 'r', encoding='utf-8') as file:
            self.assertEqual(file.read(), "Найкоротший шлях має довжину 12")

if __name__ == "__main__":
    unittest.main()
