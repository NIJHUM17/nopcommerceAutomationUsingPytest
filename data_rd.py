import configparser
import os


class Data:

    def data(self):
        cur_dir = os.path.dirname(os.path.realpath(__file__))
        _file_path = str(os.path.abspath(cur_dir))
        _file = _file_path + "\\" + "test_data.ini"
        print(_file_path)
        parser = configparser.ConfigParser()
        parser.read(_file)
        return parser