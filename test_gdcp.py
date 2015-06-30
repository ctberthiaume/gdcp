#!/usr/bin/env python
import unittest
import gdcp

class GDCPTest(unittest.TestCase):
    def test_find_id(self):
        """
        Test ID parsing function
        """
        ids = [
            "https://drive.google.com/drive/#folders/0B01234567890123456789012345",
            "https://drive.google.com/drive/#folders/0B01234567890123456789012345/0B01234567890123456789012346",
            "987012345/0B01234567890123456789012346",
            "https://drive.google.com/open?id=0B01234567890123456789012346&authuser=0",
            "https://drive.google.com/open?id=0B01234567890123456789012346",
            "https://docs.google.com/a/uw.edu/file/d/0B1vFU7eD_alGaXRiMk1qa1J6UzQ/edit?usp=drivesdk",
            "0B1vFU7eD_alGaXRiMk1qa1J6UzQ",
            "not_an_id"
        ]
        correct_answers = [
            "0B01234567890123456789012345",
            "0B01234567890123456789012346",
            "0B01234567890123456789012346",
            "0B01234567890123456789012346",
            "0B01234567890123456789012346",
            "0B1vFU7eD_alGaXRiMk1qa1J6UzQ",
            "0B1vFU7eD_alGaXRiMk1qa1J6UzQ",
            "not_an_id"
        ]
        answers = [gdcp.find_id(x) for x in ids]
        self.assertListEqual(answers, correct_answers)

if __name__ == "__main__":
    unittest.main()
