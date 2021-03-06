import configparser
import os


def ConfigSectionMap(section):
    Config = configparser.ConfigParser()
    config_file = os.path.join(os.path.dirname(__file__), '../app_configs/settings.ini')
    Config.read(config_file)

    dict1 = {}
    options = Config.options(section)
    for option in options:
        try:
            dict1[option] = Config.get(section, option)
            if dict1[option] == -1:
                DebugPrint("skip: %s" % option)
        except:
            print("exception on %s!" % option)
            dict1[option] = None
    return dict1
