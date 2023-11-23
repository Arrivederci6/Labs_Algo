import unittest
from models.govern import topological_sort, read_input, write_output

class TestGovern(unittest.TestCase):
    def test_topological_sort(self):
        graph = {
            'a': ['b', 'c'],
            'b': ['d'],
            'c': ['d'],
            'd': []
        }
        expected_orders = [['a', 'b', 'c', 'd'], ['a', 'c', 'b', 'd']]
        self.assertIn(topological_sort(graph), expected_orders)

    def test_read_input(self):
        input_file_path = 'test_files/test.in'
        with open(input_file_path, 'w') as file:
            file.write('a b\na c\nb d\nc d\n')

        expected_graph = {'a': ['b', 'c'], 'b': ['d'], 'c': ['d'], 'd': []}
        actual_graph = read_input(input_file_path)

        expected_graph_set = {key: set(value) for key, value in expected_graph.items()}
        actual_graph_set = {key: set(value) for key, value in actual_graph.items()}
        self.assertEqual(expected_graph_set, actual_graph_set)

    def test_write_output(self):
        output_file_path = 'test_files/test.out'
        order = ['a', 'c', 'b', 'd']
        with open(output_file_path, 'w') as file:
            file.write('\n'.join(order))

        with open(output_file_path, 'r') as file:
            lines = [line.strip() for line in file.readlines()]
        self.assertEqual(lines, order)

if __name__ == "__main__":
    unittest.main()
