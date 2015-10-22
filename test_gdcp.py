#!/usr/bin/env python
import unittest
import gdcp

class GDCPTest(unittest.TestCase):
    def test_find_id(self):
        """
        Test ID parsing function
        """
        ids = [
            "https://drive.google.com/drive/#folders/0B01234567890123456789012340",
            "https://drive.google.com/drive/#folders/0B01234567890123456789012340/0B01234567890123456789012341",
            "987012345/0B01234567890123456789012342",
            "https://drive.google.com/open?id=0B01234567890123456789012343",
            "https://drive.google.com/open?id=0B01234567890123456789012344&authuser=0",
            "https://docs.google.com/a/uw.edu/file/d/0B01234567890123456789012345/edit?usp=drivesdk",
            "https://docs.google.com/a/uw.edu/file/d/0B01234567890123456789012346",
            "https://drive.google.com/a/uw.edu/file/d/0B01234567890123456789012347/view?usp=drivesdk",
            "https://drive.google.com/a/uw.edu/file/d/0B01234567890123456789012348",
            "0B01234567890123456789012349",
            "not_an_id"
        ]
        correct_answers = [
            "0B01234567890123456789012340",
            "0B01234567890123456789012341",
            "0B01234567890123456789012342",
            "0B01234567890123456789012343",
            "0B01234567890123456789012344",
            "0B01234567890123456789012345",
            "0B01234567890123456789012346",
            "0B01234567890123456789012347",
            "0B01234567890123456789012348",
            "0B01234567890123456789012349",
            "not_an_id"
        ]
        answers = [gdcp.find_id(x) for x in ids]
        self.assertListEqual(answers, correct_answers)

if __name__ == "__main__":
    unittest.main()
