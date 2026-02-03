import unittest # 🔴 Importing unittest


class SmokeTest(unittest.TestCase):
    def test_ut_works(self):
        self.assertEqual(2+2,4)
        self.assertNotEqual(5,1)

    def test_ut_works_with_truthiness(self):
        self.assertTrue(True)
        self.assertFalse(0)

if __name__=="__main__":
    unittest.main(verbosity=3, exit=True)