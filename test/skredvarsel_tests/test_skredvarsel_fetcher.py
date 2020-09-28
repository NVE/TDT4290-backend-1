import unittest
from datetime import date
from src.apis.skredvarsel.skredvarsel_fetcher import SkredvarselFetcher
from util.avalanche_incident import AvalancheIncident
import json

class TestSkredvarselFetcher(unittest.TestCase):
    
    def test_create_url(self):
        date = "2020-01-05"
        lat = 61.62413454082607
        lon = 8.470996875
        api_url = SkredvarselFetcher.create_url(lat, lon, date)
        expected_api_url = "https://api01.nve.no/hydrology/forecast/avalanche/v5.0.1/api/AvalancheWarningByCoordinates/Detail/61.62413454082607/8.470996875/1/2020-01-05/2020-01-05/"
        self.assertEqual(api_url, expected_api_url)

    def test_fetch_data_for_skredvarsel(self):
        avalanche_incident = AvalancheIncident(
            id=1,
            time=date.fromisoformat("2019-02-20"),
            coords_utm=(179633, 6782269),
            coords_latlng=(61.044338, 9.062769)
        )

        response = SkredvarselFetcher.fetch_data_from_skredvarsel(avalanche_incident)
        self.assertEqual(response[0]["ValidFrom"],"2019-02-20T00:00:00")
        

    def test_fetch(self):
        avalanche_incident_list = []
        avalanche_incident_list.append(AvalancheIncident(
            id=1,
            time=date.fromisoformat("2019-02-20"),
            coords_utm=(179633, 6782269),
            coords_latlng=(61.044338, 9.062769)
        ))

        avalanche_incident_list.append(AvalancheIncident(
            id=2,
            time=date.fromisoformat("2019-02-25"),
            coords_utm=(109190, 6725372),
            coords_latlng=(60.474065, 7.882042)
        ))

        raw_data = SkredvarselFetcher().fetch(avalanche_incident_list)
        print(raw_data[1])
        self.assertEqual(raw_data[1]["ValidFrom"],"2019-02-20T00:00:00")
        self.assertEqual(raw_data[2]["ValidFrom"],"2019-02-25T00:00:00")

    