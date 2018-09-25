import unittest
import sample_func

class TestCap(unittest.TestCase):
  def test_one_word(self):
    text = 'python'
    result = sample_func.cap_text(text)
    self.assertEqual(result,'Python')
  def test_multiple_words(self):
    text = 'monty python'
    result = sample_func.cap_text(text)
    self.assertEqual(result,'Monty Python')

if __name__ == '__main__':
  unittest.main()

