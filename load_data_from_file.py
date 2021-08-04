import os
import pandas as pd
import sys

from common import get_month_string_from_number


def load_data_from_file(param_filename):
    """
    load_data_from_file(param_filename)
    param_filename: filename that contains data
        uses '.xlsx', '.xls', '.csv', '.tsv' and '.txt'
            '.txt' file must have data similar to .csv
        if invalid extension found, program quits
    Create a dataframe from file
    """

    filename, file_ext = os.path.splitext(param_filename)
    file_ext = str(file_ext).lower()
    if file_ext == ".xlsx" or file_ext == "xls":
        month_dataframe = pd.read_excel(param_filename)
    elif file_ext == ".csv" or file_ext == ".txt":
        month_dataframe = pd.read_csv(param_filename)
    elif file_ext == ".tsv":
        month_dataframe = pd.read_csv(param_filename, sep='\t')
    else:
        print(file_ext + " Invalid input file found")
        sys.exit()
    if not os.path.exists(param_filename):
        print("Data file not found")
        sys.exit()
    month_dataframe.fillna(0, inplace=True)
    return month_dataframe


def load_month_data(weather_data, path, month: int, year: int):
    """
    Loads passed month data into weather data class

    load_month_data(weather_data, path, month, year)
    weather_data: object of class WeatherData
    path: path of the dir where all files are located
    month: int representing month. range(1-12)
    year: int representing year
    """
    if not (0 < month < 13):
        print("Invalid month")
        sys.exit()
    filename_prefix = "Murree_weather_"
    filename = path + "/" + filename_prefix + str(year) + "_"\
                    + get_month_string_from_number(month)
    extension_list = [".txt", ".csv", ".tsv", ".xlsx", ".xls"]
    for extension in extension_list:
        if os.path.exists(filename + extension):
            filename += extension
            month_data = load_data_from_file(filename)
            weather_data.add_month_data(month, year, month_data)
    return


def load_year_data(weather_data, path, year: int):
    """
        Loads passed year data into weather data class

        load_year_data(weather_data, path, year)
        weather_data: object of class WeatherData
        path: path of the dir where all files are located
        year: int representing year
    """

    for i in range(1, 13):
        load_month_data(weather_data, path, i, year)
    return
