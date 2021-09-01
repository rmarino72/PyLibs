from farsight.bo.Coordinates import Coordinates
from farsight.bo.WallHumidity import WallHumidity


class Utils:

    @staticmethod
    def get_cpu_temperature() -> float or None:
        try:
            return 20

        except Exception:
            return None

    @staticmethod
    def get_wall_humidity() -> WallHumidity or None:
        try:
            wall_humidity = WallHumidity()

            return wall_humidity
        except Exception:
            return None

    @staticmethod
    def get_coordinates() -> Coordinates or None:
        try:
            coordinates = Coordinates()

            return  coordinates

        except Exception:
            return None

    @staticmethod
    def get_ambient_humidity() -> float or None:
        try:
            return 0

        except Exception:
            return None
