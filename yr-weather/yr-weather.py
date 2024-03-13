# Data from MET Norway (NLOD 2.0, CC 4.0 BY International). https://developer.yr.no/

from calendar import month_abbr
from datetime import datetime, timedelta

import requests
from matplotlib import pyplot

API_URL = 'https://api.met.no/weatherapi/locationforecast/2.0/compact'
USER_AGENT = 'SollicitatieopdrachtMeemoo maxime_debosschere@hotmail.com'
COORD_LAT = 51.0619
COORD_LONG = 3.7336
PLOT_TITLE = 'Weather forecast for meemoo'


def make_plot(temperatures):
    x = temperatures.keys()
    y_max = [v[1] for v in temperatures.values()]
    y_min = [v[0] for v in temperatures.values()]

    pyplot.title(PLOT_TITLE)
    pyplot.xlabel('Day')
    pyplot.ylabel('Temperature (°C)')
    pyplot.plot(x, y_max, label='max.', color='orangered')
    pyplot.plot(x, y_min, label='min.', color='dodgerblue')
    pyplot.legend()
    pyplot.show()


# Returns a dict with seven key-value pairs: keys are days, values are (min, max) temperatures
def get_temperatures_per_day(data):
    all_temperatures = {}
    result = {}

    # Project air_temperature property per timestamp
    for timeseries in data['properties']['timeseries']:
        all_temperatures[timeseries['time']] = timeseries['data']['instant']['details']['air_temperature']

    # Determine min and max temperatures per day for the next seven days (including today)
    for day in [datetime.today().date() + timedelta(days=x) for x in range(7)]:
        temperatures = [v for k, v in all_temperatures.items() if datetime.fromisoformat(k).date() == day]
        result[f'{day.day} {month_abbr[day.month]}'] = (min(temperatures), max(temperatures))

    return result


def get_weather_data():
    url = f'{API_URL}?lat={COORD_LAT}&lon={COORD_LONG}'
    headers = {'User-Agent': USER_AGENT, 'Accept-Encoding': 'gzip, deflate'}

    response = None
    try:
        response = requests.get(url, headers=headers)
    except requests.exceptions.RequestException as ex:
        print(f'Error: {ex.response}')

    return response.json()


weather_data = get_weather_data()
temperatures_per_day = get_temperatures_per_day(weather_data)
make_plot(temperatures_per_day)
