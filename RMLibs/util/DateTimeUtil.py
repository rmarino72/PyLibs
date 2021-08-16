from datetime import datetime, timedelta


class DateTimeUtil:

    FORMAT_YMDHMS = "%Y-%m-%d %H:%M:%S"
    FORMAT_TIMESTAMP = "%Y%m%d%H%M%S"

    @staticmethod
    def get_now() -> datetime:
        return datetime.now()

    @staticmethod
    def get_now_str() -> str:
        now: datetime = datetime.now()
        return now.strftime(DateTimeUtil.FORMAT_YMDHMS)

    @staticmethod
    def get_current_timestamp() -> str:
        now: datetime = datetime.now()
        return now.strftime(DateTimeUtil.FORMAT_TIMESTAMP)

    @staticmethod
    def datetime_from_string(value: str) -> datetime:
        return datetime.strptime(value, DateTimeUtil.FORMAT_YMDHMS)

    @staticmethod
    def datetime_from_timestamp(value: str) -> datetime:
        return datetime.strptime(value, DateTimeUtil.FORMAT_TIMESTAMP)

    @staticmethod
    def datetime_to_string(dt: datetime) -> str:
        return dt.strftime(DateTimeUtil.FORMAT_YMDHMS)

    @staticmethod
    def datetime_to_timestamp(dt: datetime) -> str:
        return dt.strftime(DateTimeUtil.FORMAT_TIMESTAMP)

    @staticmethod
    def add_minutes(dt: datetime, minutes: int):
        return dt + timedelta(minutes=minutes)

    @staticmethod
    def add_days(dt: datetime, days: int):
        return dt + timedelta(days=days)
