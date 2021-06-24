# Test functions goes here
import unittest

from huffman import encode, decode

class TestHuffman(unittest.TestCase):
	# write all your tests here
	# function name should be prefixed with 'test'

	def test_encode(self):
		encode("story.txt", "story.huff")
		assert True

	def test_decode(self):
		decode("story.huff", "story_.txt")
		assert True
	
	def test_encode1(self):
		encode("text.txt", "text.huff")
		assert True

	def test_decode1(self):
		decode("text.huff", "text1.txt")
		assert True

	def test_encode2(self):
		encode("input.txt", "output.huff")
		assert True

	def test_decode2(self):
		decode("output.huff", "output.txt")
		assert True

if __name__ == '__main__':
	unittest.main()
