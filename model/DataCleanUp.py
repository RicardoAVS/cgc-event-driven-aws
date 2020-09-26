from service.LoadCSV import LoadCSV
import pandas as pd


class DataCleanUp(object):
    _data_frame = None

    def __init__(self, url1: str):
        self._dataset_one = LoadCSV(url1).get_data()
        self.create_df()

    def create_df(self):
        _raw_data = self._dataset_one
        self._data_frame = self.byte_pd_df(_raw_data)

    @staticmethod
    def byte_pd_df(_raw_data):
        pd_obj = pd.read_csv(_raw_data)
        return pd.DataFrame(pd_obj)

    def merge_df(self, _url=None):
        if _url is None or not isinstance(_url, str):
            raise Exception('Must provide an valid url format')
        data_frame = self.byte_pd_df(_url)
        recover_cases = self.find_recovered_cases(data_frame)

        self._data_frame['date'] = self.str_to_date(self._data_frame)
        self._data_frame['recovered'] = pd.Series(cases for cases in recover_cases)
        return data_frame

    @staticmethod
    def str_to_date(data_frame):
        return pd.to_datetime(data_frame['date'])

    @staticmethod
    def find_recovered_cases(data_frame):
        by_country = data_frame[data_frame['Country/Region'] == 'US']
        return by_country['Recovered']

    @property
    def get_data_frame(self):
        return self._data_frame


