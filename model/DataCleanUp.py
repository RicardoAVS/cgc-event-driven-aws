from service.LoadCSV import LoadCSV
import pandas as pd


class DataCleanUp(object):
    """ A class used to Perform data manipulations

    Attributes
    ----------
    _data_frame: pandas.DataFrame
        used to store csv data as a pandas Data Frame (default None)
    Methods
    -------
    create_df()
        Store in _data_frame the instance of the pandas.DataFrame
    byte_pd_df()
        parse the raw data to a pandas.DataFrame
    merge_df()
        Do the manipulation and data convertion which then will be stored
        in _data_frame
    """

    _data_frame = None

    def __init__(self, url1: str):
        self._dataset_one = LoadCSV(url1).data
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
    def data_frame(self):
        return self._data_frame


if __name__ == '__main__':
    url = 'https://raw.githubusercontent.com/nytimes/covid-19-data/master/us.csv'
    jh_dataset = 'https://raw.githubusercontent.com/datasets/covid-19/master/data/time-series-19-covid-combined.csv?opt_id=oeu1597021073673r0.5796427210291657'
    df = DataCleanUp(url)
    df.merge_df(jh_dataset)
    print(df._data_frame)

    data_f = df._data_frame.to_dict('dict')
    print(data_f['date'])