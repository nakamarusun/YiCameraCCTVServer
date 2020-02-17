from enum import Enum
import exceptions

class Interval(Enum):
    HOURLY = 1
    DAILY = 2
    HALFDAILY = 3
    HALFHOURLY = 4
    QUARTERHOURLY = 5
    MINUTELY = 6

    def getSecond(intervalEnum: int) -> int:
        secondDict = {
            Interval.HOURLY: 3600,
            Interval.DAILY: 86400,
            Interval.HALFDAILY: 43200,
            Interval.HALFHOURLY: 1800,
            Interval.QUARTERHOURLY: 900,
            Interval.MINUTELY: 60
        }

        try:
            secondDict[intervalEnum]
        except KeyError:
            raise exceptions.EnumerationError
        
        return secondDict[intervalEnum]