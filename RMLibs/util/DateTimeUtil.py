from datetime import datetime, timedelta


class DateTimeUtil:

    FORMAT_YMDHMS = "%Y/%m/%d %H:%M:%S"

    @staticmethod
    def get_now() -> str:
        now: datetime = datetime.now()
        return now.strftime(DateTimeUtil.FORMAT_YMDHMS)

    @staticmethod
    def datetime_from_string(value: str) -> datetime:
        return datetime.strptime(value, DateTimeUtil.FORMAT_YMDHMS)

    @staticmethod
    def datetime_to_string(dt: datetime) -> str:
        return dt.strftime(DateTimeUtil.FORMAT_YMDHMS)

    @staticmethod
    def add_minutes(dt: datetime, minutes: int):
        return dt + timedelta(minutes=minutes)
