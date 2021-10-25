import unittest

import app


class TestMethods(unittest.TestCase):
    def test_add(self):
        self.assertEqual(app.smile(), ":)")


if __name__ == '__main__':
    unittest.main()
