import util.utm_converter as utm_converter
from util.testing import AvalancheTestCase


class TestUtmConverter(AvalancheTestCase):

    def test_converter(self):
        east = 340000
        north = 5710000
        converter = utm_converter.convert(east, north)
        self.assertAlmostEqual(
            converter, (51.518406544328315, 12.693877485718236))
