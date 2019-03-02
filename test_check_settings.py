import pytest
from .utility.check_settings import check_settings

settings = {
    'calendar_id': 'primary',
    'time_zone': 'Europe/Warsaw',
    'minutes_between': 10,
    'start_time': "08:00",
    'day': 'today'
}


def test_not_valid_time_zone():
    new_settings = settings.copy()
    new_settings['time_zone'] = 'Some Time Zone'
    assert check_settings(new_settings) == 'Incorrect Time Zone'
    new_settings['time_zone'] = ''
    assert check_settings(new_settings) == 'Time Zone not set, please fill in ' \
                                           'Time Zone field in settings'


def test_not_valid_start_time():
    new_settings = settings.copy()
    new_settings['start_time'] = '08'
    assert check_settings(new_settings) == 'Incorrect Time Format'
    new_settings['start_time'] = '25:00'
    assert check_settings(new_settings) == 'Time can\'t be greater than 24:00'
    new_settings['start_time'] = '21:70'
    assert check_settings(new_settings) == 'Please correct the minutes in \
                                            start time, can\'t be greater \
                                            than 59 minutes'
    new_settings['start_time'] = ''
    assert check_settings(new_settings) == 'Start Time is not set, please \
                                            fill in this field in settings'
    new_settings['start_time'] = 'abc'
    assert check_settings(new_settings) == 'Incorrect Time Format'
    new_settings['start_time'] = '-09:20'
    assert check_settings(new_settings) == 'Negative values are forbidden'


def test_not_valid_day():
    new_settings = settings.copy()
    new_settings['day'] = 'Wednesday'
    assert check_settings(new_settings) == 'Incorrect Day'
    new_settings['day'] = ''
    assert check_settings(new_settings) == 'Day not set, please fill in ' \
                                           'Day field in settings'


def test_all_data_valid():
    new_settings = settings.copy()
    assert check_settings(new_settings) == 'Settings correct'


# def test_not_valid_calendar_id():
#     # TODO: check available calendar id, for active user
#     pass
