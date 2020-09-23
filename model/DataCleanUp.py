from service.LoadCSV import LoadCSV
import pandas as pd


class DataCleanUp(object):

    url = 'https://raw.githubusercontent.com/nytimes/covid-19-data/master/us.csv'
    jh_url = 'https://raw.githubusercontent.com/datasets/covid-19/master/data/time-series-19-covid-combined.csv?opt_id=oeu1597021073673r0.5796427210291657'

    # __init__
    ny_file = LoadCSV(url)
    jh_file = LoadCSV(jh_url)

    # get url
    ny_byte_data = ny_file.get_data()

    # Read data
    ny_data = pd.read_csv(ny_byte_data)
    jh_data = pd.read_csv(jh_url)

    # parse date column to a date object
    ny_data['date'] = pd.to_datetime(ny_data['date'])

    # clean_up: Find which are the recovered cases
    jh_data_frame = pd.DataFrame(jh_data)
    by_country = jh_data_frame[jh_data_frame['Country/Region'] == 'US']
    recover_cases = by_country['Recovered']

    data_frame = pd.DataFrame(ny_data)
    data_frame['recovered'] = pd.Series(cases for cases in recover_cases)

