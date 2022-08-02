import datetime


def get_current_hour1() -> int:
    now = datetime.datetime.now()
    return now.hour


def get_current_hour2(x: datetime.datetime) -> int:
    return x.hour


def get_current_hour3() -> int:
    return 3
