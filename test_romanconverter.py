# Copyright 2020 by Jennifer Campbell

import unittest
from romanconverter import whatHaveTheRomans

class RomanTestCase(unittest.TestCase):

	def test_RomanConvert(self):
		checkLib = {1: '1', 2: 15, 3: '49', 4: '58', \
		5: '99', 6: 300, 7: '459', 8: '567', 9: '999', \
		10: '1110', 11: 3999, 12: 4001, 13: 10.1, \
		14: '-1', 15: '1a0', 16: '10*2'}

		ansLib = {1: 'I', 2: 'XV', 3: 'XLIX', 4: 'LVIII', \
		5: 'XCIX', 6: 'CCC', 7: 'CDLIX', 8: 'DLXVII', \
		9: 'CMXCIX', 10: 'MCX', 11: 'MMMCMXCIX', \
		12: 'MMMMI', 13: False, 14: False, 15: False, \
		16: False}

		for i in range(1,len(checkLib)+1):
			passCheck = whatHaveTheRomans(checkLib[i])
			self.assertEqual(passCheck, ansLib[i])

if __name__ == '__main__':
	unittest.main()