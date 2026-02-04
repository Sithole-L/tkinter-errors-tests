import unittest
from unittest.mock import patch
from test_start import HelloName

class TestHelloNameIntegrate(unittest.TestCase):
    def setUp(self):
        self.app = HelloName()

    def test_display_output_valid(self):   
        result = self.app.display_output("John")
        self.assertEqual(result, "OK")

    def test_display_output_valid_edge(self):   
        result = self.app.display_output("Ann-Marie")
        self.assertEqual(result, "OK")  

    @patch('tkinter.messagebox.showerror')
    def test_display_output_invalid_empty(self, mock_error):   
        self.app.display_output("")
        mock_error.assert_called_with("Error", "Name cannot be left blank")

    @patch('tkinter.messagebox.showerror')
    def test_display_output_invalid_length_short(self, mock_error):   
        self.app.display_output("jo")
        mock_error.assert_called_with("Error", "The name should be between 3 and 19 characters")

    @patch('tkinter.messagebox.showerror')
    def test_display_output_invalid_length_long(self, mock_error):   
        self.app.display_output("resfinbqwertyuioplkjhgfdsazxcvbnm")
        mock_error.assert_called_with("Error", "The name should be between 3 and 19 characters")    

    @patch('tkinter.messagebox.showerror')
    def test_display_output_invalid_type(self, mock_error):   
        self.app.display_output("123Abc=#_2cVZ")
        mock_error.assert_called_with("Error", "The name can only contain letters")       


if __name__=="__main__":
    unittest.main(verbosity=3, exit=True)