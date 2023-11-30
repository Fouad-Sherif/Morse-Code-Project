import unittest
from mourse import english_to_morse, morse_to_english, MorseError

class TestMorseCodeConverter(unittest.TestCase):

    def test_english_to_morse_valid_input(self):
        text_to_encrypt = "HELLO WORLD"
        result = english_to_morse(text_to_encrypt)
        expected_result = ".... . .-.. .-.. --- / .-- --- .-. .-.. -.."
        self.assertEqual(result, expected_result)

    def test_english_to_morse_invalid_input(self):
        with self.assertRaises(MorseError):
            english_to_morse("123")  # Invalid input containing numbers