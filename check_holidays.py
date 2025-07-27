import holidays
from datetime import date

def is_holiday(day=date.today()):
    public_holidays=holidays.India(years=day.year)
    return day in public_holidays
    
def list_holidays(day=date.today()):
    if is_holiday(day):
        public_holidays=holidays.India(years=day.year)
        l= public_holidays[day].split("; ")
        return l
    return None

def check_holiday(day=date.today()):
    public_holidays=holidays.India(years=day.year)
    hol_name=public_holidays.get(day)
    if hol_name is not None:
        hol_name=hol_name.split("; ")

    return {'is_holiday':bool(hol_name),
            'holiday name':hol_name,
            'date':str(day)}
