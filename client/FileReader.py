import requests
import os

class FileReader(object):
    """ A class used to read data from a URL or local file 
    
    Attributes
    ----------
    _file_name : str
        a str where data will be stored (default None)
    _url: str
        The url which will be used to retreive the data (default None)
    Methods
    -------
    get_url_data()
        Returns the data from the URL
    create_file(file_name=covid_data.csv)
        Creates the file in the current directory 
    write_to_file()
        Put the data from URL into the previously created file
    get_file()
        Returns the file name
    """
    
    _file_data = None
    _url = None
    _file_name = None
    
    def __init__(self, url: str):
        self._url = url
    
    def get_url_data(self):
        """Retrieves the data from the URL.

        Raises
        ------
        Exception
            If status code is not in 200 range.
        """
        
        if self._url is None:
            raise Exception('An URL must be provided')
        res = requests.get(self._url)
        print(type(res.content))
        return res.content


    def create_file(self, file_name='covid_data.csv'):
        """Create a file in the current directory

        If the argument `file_name` isn't passed in, the default covid_data.csv
        file_name is used

        Parameters
        ----------
        file_name : str, optional
            The name which will be used to create the file (default is covid_data.csv)
        """
        
        self._file_name = file_name
        if not os.path.exists(file_name):
            os.mknod(file_name)
        
    def write_to_file(self):
        if self._file_name is None:
            self.create_file()
        with open(self._file_name, 'wb') as file:
            url_data = self.get_url_data()
            self._file_data = file.write(url_data)
        
    def get_file(self):
        if self._file_name is None:
            self.write_to_file()        
        return self._file_name