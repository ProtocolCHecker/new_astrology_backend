# house_processor.py

class HouseProcessor:
    SIGNS = [
        'Aries', 'Taurus', 'Gemini', 'Cancer', 'Leo', 'Virgo',
        'Libra', 'Scorpio', 'Sagittarius', 'Capricorn', 'Aquarius', 'Pisces'
    ]

    def __init__(self, houses: dict):
        """
        Initialize with the houses dict.
        """
        self.houses = houses
        self.processed = self._process_houses()

    def _degree_to_sign(self, degree: float) -> str:
        index = int(degree // 30) % 12
        return self.SIGNS[index]

    def _degree_within_sign(self, degree: float) -> float:
        return round(degree % 30, 2)

    def _process_houses(self) -> dict:
        """
        Convert each house cusp to sign and degree within sign.
        Returns a dictionary with detailed info.
        """
        return {
            house: {
                "sign": self._degree_to_sign(deg),
                "degree_in_sign": self._degree_within_sign(deg),
                "full_degree": round(deg, 2)
            }
            for house, deg in self.houses.items()
        }

    def get_processed_data(self) -> dict:
        """
        Returns the processed house data.
        """
        return self.processed
