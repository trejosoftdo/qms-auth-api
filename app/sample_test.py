"""Sample test case
"""

import unittest


class SampleTest(unittest.TestCase):
    """Sample test case

    Args:
        unittest (unittest.TestCase): TestCase base class
    """

    def test_sample(self):
        """Sample test
        """
        a = "some"
        b = "some"
        self.assertEqual(a, b)


if __name__ == "__main__":
    unittest.main()
