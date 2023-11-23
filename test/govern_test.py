import unittest
from collections import defaultdict
from models.govern import topological_sort, read_input, write_output

class TestTopologicalSort(unittest.TestCase):
    """
    This class tests the function 'topological_sort' from your module.
    """
    def setUp(self):
        """
        This method sets up a simple graph for testing.
        """
        self.graph = defaultdict(list)
        self.graph['a'].append('b')
        self.graph['b'].append('c')

    def test_topological_sort(self):
        """
        This method tests the 'topological_sort' function with the graph set up in 'setUp'.
        It asserts that the function returns the correct topological order for the graph.
        """
        self.assertEqual(topological_sort(self.graph), ['c', 'b', 'a'])

class TestReadInput(unittest.TestCase):
    """
    This class tests the function 'read_input' from your module.
    """
    def test_read_input(self):
        """
        This method tests the 'read_input' function with a test input file 'test_input.txt'.
        It asserts that the function correctly reads the graph from the file.
        """
        graph = read_input('test_files/test.in')
        expected_graph = defaultdict(list, {'a': ['b'], 'b': ['c']})
        self.assertEqual(graph, expected_graph)

class TestWriteOutput(unittest.TestCase):
    """
    This class tests the function 'write_output' from your module.
    """
    def test_write_output(self):
        """
        This method tests the 'write_output' function with a test output file 'test_output.txt' and a test topological order.
        It asserts that the function correctly writes the topological order to the file.
        """
        write_output('test_files/test.txt', ['c', 'b', 'a'])
        with open('test_files/test.out', 'r') as file:
            lines = file.readlines()
            self.assertEqual(lines, ['c\n', 'b\n', 'a\n'])

if __name__ == '__main__':
    """
    This is the main entry point for running the tests.
    """
    unittest.main()
