from datetime import date


def get_date_today_str():
    return date.today().strftime("%Y%m%d")
