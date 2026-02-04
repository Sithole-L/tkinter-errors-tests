import unittest # 🔴 Importing unittest
from test_start import HelloName

class SmokeTest(unittest.TestCase):
    def test_ut_works(self):
        self.assertTrue(True)

class HelloNameTest(unittest.TestCase):
    def test_decorate_name(self):
        app = HelloName()
        actual_result = app.decorate_name("Bukayo")
        expected_result = "Hello, 🌼Bukayo🌼!"
        self.assertEqual(actual_result, expected_result) 

class HelloNameTestWithType(unittest.TestCase):
    def test_decorate_name_with_type(self):
        app = HelloName()
        self.assertIsInstance(app.decorate_name("Gabriel"), str)
        self.assertNotIsInstance(app.decorate_name("Gabriel"), int)         

class HelloPresenceCheckTest(unittest.TestCase):
    def test_presence_check_fail(self):
        app = HelloName()
        actual_result = app.presence_check("")
        expected_result = False
        self.assertEqual(actual_result, expected_result)

    def test_presence_check_pass(self):
        app = HelloName()
        actual_result = app.presence_check("z")
        expected_result = True
        self.assertEqual(actual_result, expected_result)   

class HelloLengthCheckTest(unittest.TestCase):
    def test_length_check_under(self):
        app = HelloName()
        actual_result = app.length_check("jo")
        expected_result = False
        self.assertEqual(actual_result, expected_result)

    def test_length_check_pass(self):
        app = HelloName()
        actual_result = app.length_check("benny")
        expected_result = True
        self.assertEqual(actual_result, expected_result) 

    def test_length_check_over(self):
        app = HelloName()
        actual_result = app.length_check("resfinbqwertyuioplkjhgfdsazxcvbnm")
        expected_result = False
        self.assertEqual(actual_result, expected_result)           

class HelloPatternCheckTest(unittest.TestCase):
    def test_pattern_check_fail(self):
        app = HelloName()
        actual_result = app.pattern_check("123Abc=#_2cVZ")
        expected_result = False
        self.assertEqual(actual_result, expected_result)

    def test_pattern_check_pass(self):
        app = HelloName()
        actual_result = app.pattern_check("bvdr-Dn bf'reD")
        expected_result = True
        self.assertEqual(actual_result, expected_result)  

#class HelloDisplayOutputTest(unittest.TestCase): 
 #   def test_display_output(self):
  #      app = HelloName()
   #     actual_result = app.display_output("")
    #    expected_result = "Presence check failed"
     #   self.assertEqual(actual_result, expected_result)


if __name__=="__main__":
    unittest.main(verbosity=3, exit=True)