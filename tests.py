import friendly_dates
import unittest

class MyTest(unittest.TestCase):
    
    def test_same_year_same_month(self):
        self.assertEqual(
            friendly_dates.friendlify('01-07-2015', '04-07-2015'), '1st - 4th July, 2015'
        )
    
    def test_same_year_diff_month(self):
        self.assertEqual(
            friendly_dates.friendlify('01-03-2016', '03-05-2016'), '1st March - 3rd May, 2016'
        )

    def test_diff_year_diff_month(self):
        self.assertEqual(
            friendly_dates.friendlify('05-09-2022', '03-09-2023'), '5th September, 2022 - 3rd September, 2023'
        )

    def test_fail_same_day(self):
        self.assertRaises(
            ValueError,
            friendly_dates.friendlify, '05-09-2022', '05-09-2022'
        )

    def test_fail_earlier_end_date(self):
        self.assertRaises(
            ValueError,
            friendly_dates.friendlify, '05-09-2022', '05-09-2000'
        )

if __name__ == '__main__':
    unittest.main()


