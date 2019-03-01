import pytest
from .  import check_settings

settings = {
    'calendar_id': 'primary',
    'time_zone': 'Europe/Warsaw',
    'minutes_between': 10,
    'start_time': "08:00",
    'day': 'today'
}




def test_not_valid_time_zone():
    new_settings = settings
    new_settings.time_zone = 'Some Time Zone'
    assert check_settings(new_settings) == 'Incorrect Time Zone'
    new_settings.time_zone = ''
    assert check_settings(new_settings) == 'Time Zone not set, please fill in \
                                           Time Zone field in settings'


def test_not_valid_start_time():
    new_settings = settings
    new_settings.start_time = '08'
    assert check_settings(new_settings) == 'Incorrect Time Format'
    new_settings.time_zone = '25:00'
    assert check_settings(new_settings) == 'Time can\'t be greater than 24:00'
    new_settings.time_zone = '21:70'
    assert check_settings(new_settings) == 'Please correct the minutes in \
                                            start time, can\'t be greater \
                                            than 59 minutes'
    new_settings.time_zone = ''
    assert check_settings(new_settings) == 'Start Time is not set, please \
                                            fill in this field in settings'
    new_settings.time_zone = 'abc'
    assert check_settings(new_settings) == 'Incorrect Time Format'
    new_settings.time_zone = '-09:20'
    assert check_settings(new_settings) == 'Negative values are forbidden'


def test_not_valid_day():
    new_settings = settings
    new_settings.time_zone = 'Some Time Zone'
    assert check_settings(new_settings) == 'Incorrect Time Zone'
    new_settings.time_zone = ''
    assert check_settings(new_settings) == 'Time Zone not set, please fill in \
                                           Time Zone field in settings'


def test_all_data_valid():
    new_settings = settings
    assert check_settings(new_settings) == 'settings correct'

def test_not_valid_calendar_id():
    # TODO: check available calendar id, for active user
    pass
