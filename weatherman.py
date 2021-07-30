import pandas as pd
import os
import argparse
import sys
import numpy as np


os.system("clear")


class WeatherData:
    def __init__(self):
        self.__complete_data = {}
        # column names mapping from text to variables
        self.__max_temp_c = "Max TemperatureC"
        self.__min_temp_c = "Min TemperatureC"
        self.__max_humidity = "Max Humidity"
        self.__min_humidity = " Min Humidity"
        self.__mean_humidity = " Mean Humidity"
        return

    def add_month_data(self, month: int, year: int,
                       month_data: pd.DataFrame):
        if not (0 < month < 13):
            print("Invalid month ", month, ". Data not added")
        month = str(month)
        year = str(year)
        if year not in self.__complete_data:
            self.__complete_data[year] = {}
        if month not in self.__complete_data[year]:
            self.__complete_data[year][month] = {}
        self.__complete_data[year][month] = month_data
        return

    def get_column_name_from_alias(self, string):
        string = string.lower()
        if string == "max_temperature":
            return self.__max_temp_c
        elif string == "min_temperature":
            return self.__min_temp_c
        elif string == "max_humidity":
            return self.__max_humidity
        elif string == "min_humidity":
            return self.__min_humidity
        elif string == "mean_humidity":
            return self.__mean_humidity
        return None

    def get_column_data(self, column_name, month: int, year: int):
        if not (0 < month < 13):
            print("Invalid month", month)
            return []
        month = str(month)
        year = str(year)
        try:
            return self.__complete_data[year][month][column_name].tolist()
        except Exception:
            pass
        return []


def get_month_number_from_string(string):
    string = str(string).lower()
    if string == "jan":
        return 1
    elif string == "feb":
        return 2
    elif string == "mar":
        return 3
    elif string == "apr":
        return 4
    elif string == "may":
        return 5
    elif string == "jun":
        return 6
    elif string == "jul":
        return 7
    elif string == "aug":
        return 8
    elif string == "sep":
        return 9
    elif string == "oct":
        return 10
    elif string == "nov":
        return 11
    elif string == "dec":
        return 12
    return None


def get_month_string_from_number(number: int):
    if number == 1:
        return "Jan"
    if number == 2:
        return "Feb"
    if number == 3:
        return "Mar"
    if number == 4:
        return "Apr"
    if number == 5:
        return "May"
    if number == 6:
        return "Jun"
    if number == 7:
        return "Jul"
    if number == 8:
        return "Aug"
    if number == 9:
        return "Sep"
    if number == 10:
        return "Oct"
    if number == 11:
        return "Nov"
    if number == 12:
        return "Dec"
    return ""


def get_month_year_from_string(string):
    month, year = string.split('/')
    try:
        month = int(month)
        year = int(year)
    except Exception:
        raise "Invalid input"
        return None, None
    return month, year


def average(lis):
    sum_ = sum(lis)
    return sum_ / len(lis)


# Computes highest temperature, lowest temperature and humidity
def minus_e(weather_data: WeatherData, year: int):
    max_temp_list = []
    min_temp_list = []
    max_humidity_list = []
    min_humidity_list = []

    # Checking data of all 12 months
    for i in range(0, 12):
        month = i + 1
        # Max temperature
        col_name = weather_data.get_column_name_from_alias(
                                "max_temperature")
        if col_name is None:
            print("Invalid column data")
        else:
            max_temp_column = weather_data.get_column_data(col_name,
                                                           month, year)
            if max_temp_column != []:
                max_index = np.argmax(max_temp_column)
                max_temp_list.append([max_temp_column[max_index],
                                      max_index + 1, month])

        # Min temperature
        col_name = weather_data.get_column_name_from_alias(
                                "min_temperature")
        if col_name is None:
            print("Invalid column alias")
        else:
            min_temp_column = weather_data.get_column_data(col_name,
                                                           month, year)
            if min_temp_column != []:
                min_index = np.argmin(min_temp_column)
                min_temp_list.append([min_temp_column[min_index],
                                      min_index + 1, month])

        # Max humidity
        col_name = weather_data.get_column_name_from_alias(
                                "max_humidity")
        if col_name is None:
            print("Invalid column alias")
        else:
            max_humidity_column = weather_data.get_column_data(col_name,
                                                               month, year)
            if max_humidity_column != []:
                max_index = np.argmax(max_humidity_column)
                max_humidity_list.append([max_humidity_column[max_index],
                                          max_index + 1, month])

        # Min humidity
        col_name = weather_data.get_column_name_from_alias(
                                "min_humidity")
        if col_name is None:
            print("Invalid column alias")
        else:
            min_humidity_column = weather_data.get_column_data(col_name,
                                                               month, year)
            if min_humidity_column != []:
                min_index = np.argmin(min_humidity_column)
                min_humidity_list.append([min_humidity_column[min_index],
                                          min_index + 1, month])

    # Checking largest/smallest in each of the lists
    if len(max_temp_list) > 1:
        max_temp_list = sorted(max_temp_list, reverse=True,
                               key=lambda x: x[0])
        print("Maximum Temperature:", max_temp_list[0][0], "C on",
              get_month_string_from_number(max_temp_list[0][2]),
              max_temp_list[0][1])

    if len(min_temp_list) > 1:
        min_temp_list = sorted(min_temp_list, key=lambda x: x[0])
        print("Minimum Temperature:", min_temp_list[0][0], "C on"
              get_month_string_from_number(min_temp_list[0][2]),
              min_temp_list[0][1])

    if len(max_humidity_list) > 1:
        max_humidity_list = sorted(max_humidity_list, reverse=True,
                                   key=lambda x: x[0])
        print("Maximum Humidity:", max_humidity_list[0][0], "% on",
              get_month_string_from_number(max_humidity_list[0][2]),
              max_humidity_list[0][1])

    if len(min_humidity_list) > 1:
        min_humidity_list = sorted(min_humidity_list,
                                   key=lambda x: x[0])
        print("Minimum Humidity:", min_humidity_list[0][0], "% on",
              get_month_string_from_number(min_humidity_list[0][2]),
              min_humidity_list[0][1])
    return


# Computes average higest and average lowest temperature, and
# average mean humidity
def minus_a(weather_data: WeatherData, month: int, year: int):
    #  Getting maximum temperature column
    col_name = weather_data.get_column_name_from_alias("max_temperature")
    if col_name is None:
        print("Invalid column alias")
    else:
        max_temp_column = weather_data.get_column_data(col_name,
                                                       month, year)
        print("Highest Average:", round(average(
              max_temp_column), 2), "C")

    #  Getting minimum temperature column
    col_name = weather_data.get_column_name_from_alias("min_temperature")
    if col_name is None:
        print("Invalid column alias")
    else:
        min_temp_column = weather_data.get_column_data(col_name,
                                                       month, year)
        print("Lowest Average:", round(average(
              min_temp_column), 2), "C")

    #  Getting mean humidity column
    col_name = weather_data.get_column_name_from_alias("mean_humidity")
    if col_name is None:
        print("Invalid column alias")
    else:
        mean_humidity_column = weather_data.get_column_data(col_name,
                                                            month, year)
        print("Average Mean Humidity:",
              round(average(mean_humidity_column), 2), "%")
    return


# Shows a graph of highest and lowest weather of a month
def minus_c(weather_data: WeatherData, month: int, year: int):
    #  Getting maximum temperature column
    col_name = weather_data.get_column_name_from_alias("max_temperature")
    if col_name is None:
        print("Invalid column alias")
        sys.exit()
    else:
        max_temp_column = weather_data.get_column_data(col_name,
                                                       month, year)

    #  Getting minimum temperature column
    col_name = weather_data.get_column_name_from_alias("min_temperature")
    if col_name is None:
        print("Invalid column alias")
        sys.exit()
    else:
        min_temp_column = weather_data.get_column_data(col_name,
                                                       month, year)
    max_len = len(max_temp_column)
    min_len = len(min_temp_column)
    len_ = max_len
    if max_len != min_len:
        if min_len < max_len:
            len_ = min_len
        print_str = "\033[1;31;40m Note: Unequal data of maximum"
        print_str += " and minimum temperature"
        print(print_str)
    for i in range(0, len_):
        suffix_text = str("\033[0;37;40m%.2d " % (i+1))
        low_print = "\033[0;34;40m" + "+"*abs(int(min_temp_column[i]))
        high_print = "\033[0;31;40m" + "+"*abs(int(max_temp_column[i]))
        add_text = "\033[0;34;40m "
        add_text += (str(min_temp_column[i]) + "C\033[1;37;40m-")
        add_text += ("\033[0;31;40m" + str(max_temp_column[i]) + "C")
        text = suffix_text + low_print + high_print + add_text
        print(text)
    return


def list_all_files(path):
    total_files = 0
    flag = False
    weather_data = WeatherData()
    for file in os.listdir(path):
        if file.startswith(".") or len(file) < 24:
            print(file, """File not load because month and year could
                not be extracted""")
            flag = True
            continue
        name_split = os.path.splitext(file)[0].split('_')
        try:
            year = int(name_split[2])
            month = int(get_month_number_from_string(name_split[3]))
        except Exception:
            print("""File not load because month and year could not
                  be extracted""")
            continue
        if year == "" or month == "":
            print(file, """File not load because month and year
                  could not be extracted""")
            continue
        total_files += 1
        data = load_data_from_file(path + "/" + file)
        weather_data.add_month_data(month, year, data)
    print("Total files processed =", total_files)
    return weather_data


def load_data_from_file(filename):
    name, ext = os.path.splitext(filename)
    ext = str(ext).lower()
    if ext == ".xlsx" or ext == "xls":
        df = pd.read_excel(filename)
    elif ext == ".csv" or ext == ".txt":
        df = pd.read_csv(filename)
    elif ext == ".tsv":
        df = pd.read_csv(filename, sep='\t')
    else:
        print(ext + " Invalid input file found")
        sys.exit()
    df.fillna(0, inplace=True)
    return df


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('path', metavar="path", type=str,
                        help="Path to list")
    parser.add_argument('-e', action='append', type=str,
                        help="""Displays highest temperature,
                        lowest temperature and humidity of a
                        year""")
    parser.add_argument('-a', action='append', type=str,
                        help="""Displays average highest
                        temperature, average lowest temperature
                        and average humidity of a month""")
    parser.add_argument('-c', action='append', type=str,
                        help="""Draws highest and lowest
                        temperature of a month""")
    args = parser.parse_args()
    if len(sys.argv) < 3:
        print("No argument given for reports output")
        sys.exit()
    if not os.path.isdir(args.path):
        raise "Invalid path to dir given"

    weather_data = list_all_files(args.path)
    if weather_data is None:
        raise "Weather Data doesn't exist"

    if args.e is not None:
        for each in args.e:
            print("\n============================> -e ", each)
            try:
                year = int(each)
            except Exception:
                raise "Invalid year \"" + str(year) + "\""
            minus_e(weather_data, year)

    if args.a is not None:
        for each in args.a:
            print("\n============================> -a ", each)
            try:
                year, month = get_month_year_from_string(each)
            except Exception:
                raise "Invalid month/year \"" + str(each) + "\""
            minus_a(weather_data, month, year)

    if args.c is not None:
        for each in args.c:
            print("\n============================> -c ", each)
            try:
                year, month = get_month_year_from_string(each)
            except Exception:
                raise "Invalid month/year \"" + str(each) + "\""
            minus_c(weather_data, month, year)
