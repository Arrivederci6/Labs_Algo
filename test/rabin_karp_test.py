import unittest

from models.rabin_karp import rabin_karp_search


class TestRabinKarpSearch(unittest.TestCase):
    def test_simple_case(self):
        haystack = "My name is Andrii"
        needle = "is"
        result_indices = rabin_karp_search(haystack, needle)
        self.assertEqual(result_indices, [8], f"Expected [8], but got {result_indices}")

    def test_single_occurrence(self):
        haystack = "This is a test string"
        needle = "test"
        result_indices = rabin_karp_search(haystack, needle)
        self.assertEqual(result_indices, [10], f"Expected [10], but got {result_indices}")

    def test_multiple_occurrences(self):
        haystack = "abcabcabc"
        needle = "abc"
        result_indices = rabin_karp_search(haystack, needle)
        self.assertEqual(result_indices, [0, 3, 6], f"Expected [0], but got {result_indices}")

    def test_no_occurrence(self):
        haystack = "Hello, World!"
        needle = "Python"
        result_indices = rabin_karp_search(haystack, needle)
        self.assertEqual(result_indices, [], f"Expected [], but got {result_indices}")

    def test_empty_haystack(self):
        haystack = ""
        needle = "test"
        result_indices = rabin_karp_search(haystack, needle)
        self.assertEqual(result_indices, [], f"Expected [], but got {result_indices}")

    def test_substring_longer_than_haystack(self):
        haystack = "abababab"
        needle = "ababababab"
        result_indices = rabin_karp_search(haystack, needle)
        self.assertEqual(result_indices, [], f"Expected [], but got {result_indices}")

if __name__ == "__main__":
    unittest.main()
