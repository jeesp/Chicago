import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate= Kassapaate()
        self.kassapaate.kassassa_rahaa = 1000
        
    
    def test_saldo__ja_lounaat_alussa_oikein(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa, 1000)
        self.assertEqual(self.kassapaate.edulliset, 0)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_kateisosto_toimii_edullisilla(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(300), 60)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 1240)
        self.assertEqual(self.kassapaate.edulliset, 1)
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(200), 200)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 1240)
        self.assertEqual(self.kassapaate.edulliset, 1)
    
    def test_kateisosto_toimii_maukkailla(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(500), 100)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 1400)
        self.assertEqual(self.kassapaate.maukkaat, 1)
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(200), 200)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 1400)
        self.assertEqual(self.kassapaate.maukkaat, 1)
    
    def test_korttimaksu_toimii_maukkailla(self):
        maksukortti = Maksukortti(1000)
        self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(maksukortti), True)
        self.assertEqual(maksukortti.saldo, 600)
        self.assertEqual(self.kassapaate.maukkaat, 1)
        self.assertEqual(self.kassapaate.kassassa_rahaa,1000)
        maksukortti2 = Maksukortti(100)
        self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(maksukortti2), False)
        self.assertEqual(maksukortti2.saldo, 100)
        self.assertEqual(self.kassapaate.maukkaat, 1)
        self.assertEqual(self.kassapaate.kassassa_rahaa,1000)
    
    def test_korttimaksu_toimii_edullisilla(self):
        maksukortti = Maksukortti(1000)
        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(maksukortti), True)
        self.assertEqual(maksukortti.saldo, 760)
        self.assertEqual(self.kassapaate.edulliset, 1)
        self.assertEqual(self.kassapaate.kassassa_rahaa,1000)
        maksukortti2 = Maksukortti(100)
        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(maksukortti2), False)
        self.assertEqual(maksukortti2.saldo, 100)
        self.assertEqual(self.kassapaate.edulliset, 1)
        self.assertEqual(self.kassapaate.kassassa_rahaa,1000)
    
    def test_kortille_lataaminen_onnistuu(self):
        maksukortti = Maksukortti(100)
        self.kassapaate.lataa_rahaa_kortille(maksukortti, 200)
        self.assertEqual(maksukortti.saldo, 300)
        self.assertEqual(self.kassapaate.kassassa_rahaa,1200)
        self.kassapaate.lataa_rahaa_kortille(maksukortti, -200)
        self.assertEqual(maksukortti.saldo, 300)
        self.assertEqual(self.kassapaate.kassassa_rahaa,1200)



