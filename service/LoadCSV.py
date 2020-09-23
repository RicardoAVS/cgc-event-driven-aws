import requests
from io import BytesIO


class LoadCSV(object):
    """ A class used to read data from a URL and parse it to BytesIO

    Attributes
    ----------
    _data: str
        a str which will be used to store data <class _io.BytesIO> (default None)
    _url: str
        the url which will be used to retrieve the data (default None)
    Methods
    -------
    load_csv()
        Makes the call to the url
    format_data()
        Convert <class byte> to <class _io.BytesIO> format
    get_data()
        Returns the data retrieved from the URL
    """

    _data = None
    _url = None

    def __init__(self, url: str):
        self._url = url
        self.load_csv()

    def load_csv(self):
        """

        Raises
        ------
        Exception
            If status code is not in 200 range or
            if given URL is wrong.
        """
        if self._url is None:
            raise Exception('An URL must be provided')
        res = requests.get(self._url)
        if res.status_code not in range(200, 299):
            raise Exception('Page not found')
        self.format_data(res.content)

    def format_data(self, raw_data):
        self._data = BytesIO(raw_data)

    def get_data(self):
        return self._data
