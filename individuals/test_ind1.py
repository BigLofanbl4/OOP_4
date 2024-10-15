import unittest

from ind1 import Date, Triad


class TestTriad(unittest.TestCase):
    def setUp(self):
        self.triad = Triad(1, 2, 3)

    def test_increment_num_1(self):
        self.triad.increment_num_1()
        self.assertEqual(self.triad.num_1, 2)

    def test_increment_num_2(self):
        self.triad.increment_num_2()
        self.assertEqual(self.triad.num_2, 3)

    def test_increment_num_3(self):
        self.triad.increment_num_3()
        self.assertEqual(self.triad.num_3, 4)


class TestDate(unittest.TestCase):
    def setUp(self):
        self.date = Date(2023, 12, 30)

    def test_increment_year(self):
        self.date.increment_num_1()
        self.assertEqual(self.date.num_1, 2024)

    def test_increment_month(self):
        self.date.increment_num_2()
        self.assertEqual(self.date.num_2, 1)  # Месяц должен сброситься на 1.
        self.assertEqual(self.date.num_1, 2024)  # Год увеличен на 1.

    def test_increment_day(self):
        self.date.increment_num_3()
        self.assertEqual(self.date.num_3, 31)

    def test_add_days_same_month(self):
        self.date.add_days(1)
        self.assertEqual(
            (self.date.num_1, self.date.num_2, self.date.num_3), (2023, 12, 31)
        )

    def test_add_days_new_year(self):
        self.date.add_days(2)  # Переход на новый год.
        self.assertEqual(
            (self.date.num_1, self.date.num_2, self.date.num_3), (2024, 1, 1)
        )


if __name__ == "__main__":
    unittest.main()
