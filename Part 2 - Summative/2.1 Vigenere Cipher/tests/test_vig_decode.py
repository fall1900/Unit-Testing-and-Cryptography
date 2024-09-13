from unittest import TestCase
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from main import vig_decode

class TestVigDecode(TestCase):
    keyword1 = "TEST"
    keyword2 = "CORGI"
    keyword3 = "BANANA"
    def test_vig_decode_no_space_upper_keyword1(self):
        self.assertEqual(vig_decode('FEZAW__F', self.keyword1), 'NAHIDWIN')
    def test_vig_decode_no_space_lower_keyword1(self):
        self.assertEqual(vig_decode('fezaw__f', self.keyword1), 'nahidwin')
    def test_vig_decode_multiple_spaces_upper_keyword1(self):
        self.assertEqual(vig_decode('FEZSAHROAR', self.keyword1), 'NAH_ID_WIN')
    def test_vig_decode_no_space_upper_keyword2(self):
        self.assertEqual(vig_decode('POYOLYWD', self.keyword2), 'NAHIDWIN')
    def test_vig_decode_no_space_lower_keyword2(self):
        self.assertEqual(vig_decode('poyolywd', self.keyword2), 'nahidwin')
    def test_vig_decode_multiple_spaces_upper_keyword2(self):
        self.assertEqual(vig_decode('POYFQFNMOV', self.keyword2), 'NAH_ID_WIN')
    def test_vig_decode_no_space_upper_keyword3(self):
        self.assertEqual(vig_decode('OAUIQWJN', self.keyword3), 'NAHIDWIN')
    def test_vig_decode_no_space_lower_keyword3(self):
        self.assertEqual(vig_decode('oauiqwjn', self.keyword3), 'nahidwin')
    def test_vig_decode_multiple_spaces_upper_keyword3(self):
        self.assertEqual(vig_decode('OAU_VDAWVN', self.keyword3), 'NAH_ID_WIN')