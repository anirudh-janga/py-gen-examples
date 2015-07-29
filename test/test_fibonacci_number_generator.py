import unittest
from code import fibonacci_number_generator as fb

class TestFibNumGen(unittest.TestCase):

    def test_for_number_0(self):
        gen_list = list(fb.fib_num_gen(0))
        exp_result = [0]
        self.assertEqual(gen_list, exp_result)

    def test_for_number_1(self):
        gen_list = list(fb.fib_num_gen(1))
        exp_result = [0, 1, 1]
        self.assertEqual(gen_list, exp_result)

    def test_with_negative_number_input(self):
        with self.assertRaises(TypeError):
            gen_list = list(fb.fib_num_gen(-20))

    def test_with_floating_number_input(self):
        with self.assertRaises(TypeError):
            gen_list = list(fb.fib_num_gen(1.20))

if __name__ == "__main__":
    unittest.main()




