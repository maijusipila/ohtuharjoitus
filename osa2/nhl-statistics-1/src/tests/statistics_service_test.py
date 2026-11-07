import unittest
from statistics_service import StatisticsService
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        # annetaan StatisticsService-luokan oliolle "stub"-luokan olio
        self.stats = StatisticsService(
            PlayerReaderStub()
        )

    def test_search_loytyy_pelaaja(self):
        pelaaja = self.stats.search("Kurri")
        self.assertEqual(pelaaja.name, "Kurri")

    def test_search_ei_loydy_pelaajaa(self):
        pelaaja = self.stats.search("Selanne")
        self.assertIsNone(pelaaja)

    def test_team_palauttaa_oikean_joukkueen(self):
        edm_pelaajat = self.stats.team("EDM")
        self.assertEqual(len(edm_pelaajat), 3)

    def test_top_palauttaa_parhaat(self):
        top_pelaajat = self.stats.top(2)
        self.assertEqual(len(top_pelaajat), 3)
        self.assertEqual(top_pelaajat[0].name, "Gretzky")
