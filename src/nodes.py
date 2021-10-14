from datetime import date, timedelta, datetime

def add_business_days(from_date, days) -> date:
    """Auxiliar function to add n business days to a given date
    ignoring weekends.
    Args:
        from_date: date to add n business days
        days: n days to add
    Returns:
        date: date with n business days added
    """
    _from_date = to_date(from_date)
    while days > 0:
        _from_date += timedelta(days=1)
        if _from_date.weekday() >= 5:
            continue
        days -= 1
    return _from_date

def to_date(date) -> date:
    """[summary]

    Args:
        date (Datetime): [description]

    Returns:
        date: [description]
    """
    return(datetime.strptime(date, "%d/%m/%Y").date())
