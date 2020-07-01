import unittest
import sys
sys.path.append('..')

from blackjack import *

class PythonTest(unittest.TestCase):
    def test_python(self):
        with open('blackjack.py') as f:
            if 'print("Your card is:")' in f.read():
                found = True
        print(found)
        self.assertTrue(found, "Missing print statement.")

if __name__ == '__main__':
    unittest.main() 