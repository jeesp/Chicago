import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(10)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)
    
    def test_saldo_alussa_oikein(self):
        self.assertEqual(str(self.maksukortti), "saldo: 0.1")
    
    def test_lataaminen_kasvattaa_saldoa_oikein(self):
        self.maksukortti.lataa_rahaa(2)
        self.assertEqual(str(self.maksukortti), "saldo: 0.12")
    
    def test_saldo_vahenee_oikein_kun_rahaa_tarpeeksi(self):
        self.maksukortti.ota_rahaa(2)
        self.assertEqual(str(self.maksukortti), "saldo: 0.08")
    
    def test_saldo_ei_vahene_jos_rahaa_ei_ole_tarpeeksi(self):
        self.maksukortti.ota_rahaa(22)
        self.assertEqual(str(self.maksukortti), "saldo: 0.1")
    
    def test_rahan_ottaminen_palauttaa_True_jos_rahaa_on_ja_False_jos_ei(self):
        self.assertEqual(self.maksukortti.ota_rahaa(2), True)
        self.assertEqual(self.maksukortti.ota_rahaa(22), False)