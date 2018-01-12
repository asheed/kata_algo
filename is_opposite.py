#!/usr/bin/env python
# -*- coding: utf8 -*
import unittest

def is_opposite(s1, s2):

    if s1 == "" or s2 == "":
        return False
    else:
        if s1.isalpha() and s2.isalpha():
            for a in list(zip(s1, s2)):
                if abs(ord(a[0]) - ord(a[1])) != 32:
                    return False
    return True

class IsOppositeTest(unittest.TestCase):
    def test(self):
        self.assertEqual(is_opposite("ab", "AB"), True)

    def test1(self):
        self.assertEqual(is_opposite("aB", "Ab"), True)

    def test2(self):
        self.assertEqual(is_opposite("aBcd", "AbCD"), True)

    def test3(self):
        self.assertEqual(is_opposite("AB", "Ab"), False)

    def test4(self):
        self.assertEqual(is_opposite("", ""), False)

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(IsOppositeTest)
    unittest.TextTestRunner(verbosity=2).run(suite)