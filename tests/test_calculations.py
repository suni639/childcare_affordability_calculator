import unittest
from src.calculations import calculate_net_gain_loss

class TestCalculations(unittest.TestCase):
    def test_calculate_net_gain_loss(self):
        self.assertEqual(calculate_net_gain_loss(2000, 1800, 800, 200), 2800)
        self.assertEqual(calculate_net_gain_loss(2500, 2500, 1000, 500), 3500)
        self.assertAlmostEqual(calculate_net_gain_loss(1000.50, 1000.50, 500.25, 100.25), 1400.50)

if __name__ == '__main__':
    unittest.main()
