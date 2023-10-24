try:
    from unittest import TestCase
    import roulette
except ImportError as ie:
    print("Error importing libraries: ")
    print("Details: {}".format(ie))
    exit(1)

class TestBin(TestCase):
    def test(self):
        o1 = roulette.Outcome("Red", 1)
        o2 = roulette.Outcome("Red", 1)
        o3 = roulette.Outcome("Black", 2)
        o4 = roulette.Outcome("Low",2)
        b1 = roulette.Bin({o1,o2})
        b2 = roulette.Bin({o2,o3,o4})
        self.assertEqual(set(b1), {o1, o2})
        self.assertEqual(set(b2), {o2, o4, o3})
