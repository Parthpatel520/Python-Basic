import unittest
from app import add

class TestApp(unittest.TestCase):
    def test_app(self):
        self.assertEqual(add(5, 3), 8)

if __name__ == "__main__":
    unittest.main()