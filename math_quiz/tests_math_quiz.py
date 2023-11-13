import unittest
from math_quiz import random_int_between, random_operator, do_math_operation


class TestMathGame(unittest.TestCase):

    def test_random_int_between(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = random_int_between(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_random_operator(self):
        operator_list = ['+', '-', '*']
        for _ in range(1000):
            this_operator = random_operator()
            self.assertIn(this_operator, operator_list)

    def test_do_math_operation(self):
        test_cases = [
            (5, 2, '+', '5 + 2', 7),
            (10, 4, '-', '10 - 4', 6),
            (-5, 3, '*', '-5 * 3', -15)
        ]

        for num1, num2, operator, expected_problem, expected_answer in test_cases:
            problem, real_answer = do_math_operation(num1, num2, operator)
            self.assertTrue(problem == expected_problem)
            self.assertTrue(real_answer == expected_answer)


if __name__ == "__main__":
    unittest.main()
