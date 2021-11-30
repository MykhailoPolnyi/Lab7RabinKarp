import unittest
from RabinKarp import rabin_karp


class TestRabinKarp(unittest.TestCase):
    def test_casual_example(self):
        self.assertEqual([4, 7], rabin_karp("Hello world!", "o"))
        self.assertEqual([6], rabin_karp("Hello world!", "wor"))

    def test_empty_pattern(self):
        self.assertEqual([], rabin_karp("SIDFooijoiasdffioiaf", ""))

    def test_multi_matches(self):
        self.assertEqual(
            [5, 21, 43, 59],
            rabin_karp("Like the Naive Algorithm, Rabin-Karp algorithm also slides the pattern one by one.", "th")
        )

    def test_no_matches(self):
        self.assertEqual(
            [],
            rabin_karp("But unlike the Naive algorithm, Rabin Karp algorithm matches the hash value", "Tarjan")
        )



if __name__ == '__main__':
    unittest.main()
