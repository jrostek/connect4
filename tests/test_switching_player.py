import unittest
import src.gameplay as gp


class TestSwitchingPlayer(unittest.TestCase):

    def test_switch_1_2(self):
        plr1 = 1
        plr2 = gp.switch_player(plr1)
        self.assertEqual(plr2, 2)

    def test_switch_2_1(self):
        plr1 = 2
        plr2 = gp.switch_player(plr1)
        self.assertEqual(plr2, 1)

    def test_switch_bad_plr(self):
        plr1 = 0
        plr2 = gp.switch_player(plr1)
        self.assertEqual(plr2, 1)


if __name__ == '__main__':
    unittest.main()
