import unittest

from roulette import Outcome, Bin, Wheel

class TestWheel(unittest.TestCase):
    def test_addOutcome(self):
        # Create instances of Outcome
        outcome1 = Outcome(name="Outcome1", odds=2)
        outcome2 = Outcome(name="Outcome2", odds=3)

        # Create instances of Bin
        bin1 = Bin()
        bin2 = Bin()

        # Create an instance of Wheel
        my_wheel = Wheel()

        # Add outcomes to bins in the wheel
        my_wheel.addOutcome(8, outcome1)
        my_wheel.addOutcome(3, outcome2)

        # Assert that the outcomes are added correctly
        self.assertIn(outcome1, my_wheel.get(8))
        self.assertIn(outcome2, my_wheel.get(3))

    def test_choose_with_seed(self):
        # Set a fixed seed for reproducibility
        seed_value = 42

        # Create an instance of Wheel with the fixed seed
        my_wheel = Wheel()
        my_wheel.rng.seed(seed_value)

        # Choose several bins using the fixed seed
        chosen_bin_1 = my_wheel.choose()
        chosen_bin_2 = my_wheel.choose()
        chosen_bin_3 = my_wheel.choose()

        # Assert that the chosen bins are consistent with the fixed seed
        self.assertEqual(chosen_bin_1, my_wheel.get(25))
        self.assertEqual(chosen_bin_2, my_wheel.get(17))
        self.assertEqual(chosen_bin_3, my_wheel.get(9))

