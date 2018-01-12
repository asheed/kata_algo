#!/usr/bin/env python
# -*- coding: utf8 -*

import unittest

# 문1 : 문자열 감염
# AI가 문자로 텍스트를 감염시키고 있습니다.
# 텍스트가 비어있거나, 감염 문자가 비어있다면, 비어있는 문자열을 리턴합니다.
# 둘 다 비어 있는 경우는 없습니다.

# 예
# before = "abc"
# character = "z"
# after = "zzz"


def contamination(text, char):
    return char*len(text)


# Sample Tests
class ContaminationTest(unittest.TestCase):
    def test(self):
        self.assertEqual(contamination("abc", "z"), "zzz")
    def test1(self):
        self.assertEqual(contamination("", "z"), "")
    def test2(self):
        self.assertEqual(contamination("abc", ""), "")
    def test3(self):
        self.assertEqual(contamination("_3ebzgh4", "&"), "&&&&&&&&")
    def test4(self):
        self.assertEqual(contamination("//case", " "), "      ")


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(ContaminationTest)
    unittest.TextTestRunner(verbosity=2).run(suite)
    # unittest.main()