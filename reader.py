import configparser
import os

import url


class Datareader:
    cur_dir = os.path.dirname(os.path.realpath(__file__))
    _file_path = str(os.path.abspath(cur_dir))[:-8]
    _file = _file_path + "\\" + "data.ini"
    print(_file_path)
    parser =
    parser.read(_file)

