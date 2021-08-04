import numpy as np

from common import get_column_data_from_alias
from common import get_month_string_from_number
from load_data_from_file import load_month_data, load_year_data
from WeatherData import WeatherData


TEXT_STYLE_NORMAL = 0
TEXT_STYLE_BOLD = 1
TEXT_STYLE_LIGHT = 2
TEXT_STYLE_ITALICIZED = 3
TEXT_STYLE_UNDERLINED = 4
TEXT_STYLE_BLINK = 5

TEXT_COLOR_BLACK = 30
TEXT_COLOR_RED = 31
TEXT_COLOR_GREEN = 32
TEXT_COLOR_YELLOW = 33
TEXT_COLOR_BLUE = 34
TEXT_COLOR_PURPLE = 35
TEXT_COLOR_CYAN = 36
TEXT_COLOR_WHITE = 37

BACKGROUND_COLOR_BLACK = 40
BACKGROUND_COLOR_RED = 41
BACKGROUND_COLOR_GREEN = 42
BACKGROUND_COLOR_YELLOW = 43
BACKGROUND_COLOR_BLUE = 44
BACKGROUND_COLOR_PURPLE = 45
BACKGROUND_COLOR_CYAN = 46
BACKGROUND_COLOR_WHITE = 47


def change_text_color(style=0, color=37, background_color=40):
    """
    This functions returns a string. Add this string in the start
    of the string whose color or style you want to change

    change_text_color(style, color, background_color)
    style: changes style, default style "Normal"
    color: changes text color, default color "White"
    background_color: changes background color, default "Black"

    Pass constants in the function, string colors are not allowed
    """
    try:
        style = int(style)
        color = int(color)
        background_color = int(background_color)
    except Exception:
        return ""
    color_string = "\033[" + str(style) + ";" + str(color) + ";"\
                   + str(background_color) + "m"
    return color_string


def get_boundary_element(list_, max_=True, index=0):
    """
    Returns the maximum or minimum element of a 2D-array.

    get_boundary_element(list_, max_, index)
    list_: Input list whose boundary element is required
    max_: Get maximum or minimum, default: True
            Set it to "True" if maximum element is required
            Set it to "False" if minimum element is required
    index: Key of sublist which is used for sorting, default: 0
    """

    list_ = sorted(list_, reverse=max_, key=lambda x: x[index])
    temperature = list_[0][0]
    month = get_month_string_from_number(list_[0][2])
    year = list_[0][1]
    return temperature, month, year


def get_monthly_graph_data(weather_data, path, month, year):
    """
    Loads the month data and returns max temperature,
    min temperature and len to iterate list

    get_monthly_graph_data(weather_data, path, month, year)
    weather_data: Object of class WeatherData
    path: Folder consisting of all data files
    month: int representing month range(1-12)
    year: int representing year

    Returns maximum_temperature_list, minimum_temperature_list, len
    """

    load_month_data(weather_data, path, month, year)

    #  Getting maximum temperature column
    max_temp_column = get_column_data_from_alias(weather_data,
                                                 "max_temperature",
                                                 month, year)

    #  Getting minimum temperature column
    min_temp_column = get_column_data_from_alias(weather_data,
                                                 "min_temperature",
                                                 month, year)

    max_temp_col_len = len(max_temp_column)
    min_temp_col_len = len(min_temp_column)
    len_ = max_temp_col_len
    if max_temp_col_len != min_temp_col_len:
        if min_temp_col_len < max_temp_col_len:
            len_ = min_temp_col_len
            # change color variables
            print_str = "\033[1;31;40m Note: Unequal data of maximum"
            print_str += " and minimum temperature"
            print(print_str)
    return max_temp_column, min_temp_column, len_


def compute_yearly_weather_report(weather_data: WeatherData,
                                  path, year: int):
    """
    Computes highest temperature, lowest temperature and humidity
    compute_yearly_weather_report(weather_data, path, year)
    weather_data: weather data of month
                  WeatherData object
    path: Path to folder where all the data files exist
    year: int that represents a year
    """

    max_temp_list = []
    min_temp_list = []
    max_humidity_list = []
    min_humidity_list = []

    load_year_data(weather_data, path, year)

    # Checking data of all 12 months
    for i in range(0, 12):
        month = i + 1
        # Max temperature
        max_temp_column = get_column_data_from_alias(weather_data,
                                                     "max_temperature",
                                                     month, year)
        if max_temp_column:
            max_index = np.argmax(max_temp_column)
            max_temp_list.append([max_temp_column[max_index],
                                  max_index + 1, month])

        # Min temperature
        min_temp_column = get_column_data_from_alias(weather_data,
                                                     "min_temperature",
                                                     month, year)
        if min_temp_column:
            min_index = np.argmin(min_temp_column)
            min_temp_list.append([min_temp_column[min_index],
                                  min_index + 1, month])

        # Max humidity
        max_humidity_column = get_column_data_from_alias(weather_data,
                                                         "max_humidity",
                                                         month, year)
        if max_humidity_column:
            max_index = np.argmax(max_humidity_column)
            max_humidity_list.append([max_humidity_column[max_index],
                                      max_index + 1, month])

        # Min humidity
        min_humidity_column = get_column_data_from_alias(weather_data,
                                                         "min_humidity",
                                                         month, year)
        if min_humidity_column:
            min_index = np.argmin(min_humidity_column)
            min_humidity_list.append([min_humidity_column[min_index],
                                      min_index + 1, month])

    # Checking largest/smallest in each of the lists
    if len(max_temp_list) > 1:
        temperature, month, year = get_boundary_element(max_temp_list,
                                                        max_=True)
        print("Maximum Temperature:", temperature, "C on", month, year)

    if len(min_temp_list) > 1:
        temperature, month, year = get_boundary_element(min_temp_list,
                                                        max_=False)
        print("Minimum Temperature:", temperature, "C on", month, year)

    if len(max_humidity_list) > 1:
        humidity, month, year = get_boundary_element(max_humidity_list,
                                                     max_=True)
        print("Maximum Humidity:", humidity, "% on", month, year)

    if len(min_humidity_list) > 1:
        humidity, month, year = get_boundary_element(min_humidity_list,
                                                     max_=False)
        print("Minimum Humidity:", humidity, "% on", month, year)
    return


def compute_monthly_weather_report(weather_data: WeatherData,
                                   path, month: int,
                                   year: int):
    """
    Computes average highest and average lowest temperature, and
            average mean humidity

    minus_a(weather_data, path, month, year)
    weather_data: weather data of month
                  WeatherData object
    path: Path to folder where all files exist
    month: integer range(1-12)
    year: int that represents a year
    """

    load_month_data(weather_data, path, month, year)
    #  Getting maximum temperature column
    max_temp_column = get_column_data_from_alias(weather_data,
                                                 "max_temperature",
                                                 month, year)
    if max_temp_column:
        print("Highest Average:", round(sum(max_temp_column)
                                        / len(max_temp_column), 2), "C")

    #  Getting minimum temperature column
    min_temp_column = get_column_data_from_alias(weather_data,
                                                 "min_temperature",
                                                 month, year)
    if min_temp_column:
        print("Lowest Average:", round(sum(min_temp_column)
                                       / len(min_temp_column), 2), "C")

    #  Getting mean humidity column
    mean_humidity_column = get_column_data_from_alias(weather_data,
                                                      "mean_humidity",
                                                      month, year)
    if mean_humidity_column:
        print("Average Mean Humidity:", round(sum(mean_humidity_column)
                                              / len(mean_humidity_column),
                                              2), "%")
    return


# Shows a graph of highest and lowest weather of a month
def compute_monthly_weather_graph_same_line(weather_data: WeatherData,
                                            path, month: int,
                                            year: int):
    """
    Shows a graph of highest and lowest weather of a month
    Displays the max and min in same line

    minus_c(weather_data, month, year)
    weather_data: weather data of month
                  WeatherData object
    path: Path to folder where all files exist
    month: integer range(1-12)
    year: int that represents a year
    """

    max_temp_column, min_temp_column, len_ = get_monthly_graph_data(
                                    weather_data, path, month, year)
    for i in range(0, len_):
        red_color_string = change_text_color(TEXT_STYLE_NORMAL,
                                             TEXT_COLOR_RED,
                                             BACKGROUND_COLOR_BLACK)
        blue_color_string = change_text_color(TEXT_STYLE_NORMAL,
                                              TEXT_COLOR_BLUE,
                                              BACKGROUND_COLOR_BLACK)
        white_color_string = change_text_color(TEXT_STYLE_BOLD,
                                               TEXT_COLOR_WHITE,
                                               BACKGROUND_COLOR_BLACK)
        print_str = white_color_string + str("%.2d) " % (i + 1))
        print_str += blue_color_string
        print_str += "+" * abs(int(min_temp_column[i]))
        print_str += red_color_string
        print_str += "+" * abs(int(max_temp_column[i]))
        print_str += blue_color_string
        print_str += (" " + str(min_temp_column[i]) + "C")
        print_str += white_color_string + "-"
        print_str += red_color_string
        print_str += (str(max_temp_column[i]) + "C")
        print(print_str)
    return


def compute_monthly_weather_graph_two_lines(weather_data: WeatherData,
                                            path, month: int, year: int):
    """
        Shows a graph of highest and lowest weather of a month
        Displays the max and min in separate lines

        minus_c(weather_data, month, year)
        weather_data: weather data of month
                      WeatherData object
        path: Path to folder where all files exist
        month: integer range(1-12)
        year: int that represents a year
    """

    max_temp_column, min_temp_column, len_ = get_monthly_graph_data(
        weather_data, path, month, year)
    red_color_string = change_text_color(TEXT_STYLE_NORMAL,
                                         TEXT_COLOR_RED,
                                         BACKGROUND_COLOR_BLACK)
    blue_color_string = change_text_color(TEXT_STYLE_NORMAL,
                                          TEXT_COLOR_BLUE,
                                          BACKGROUND_COLOR_BLACK)
    white_color_string = change_text_color(TEXT_STYLE_BOLD,
                                           TEXT_COLOR_WHITE,
                                           BACKGROUND_COLOR_BLACK)
    for i in range(0, len_):
        print_str = white_color_string + str("%.2d" % (i + 1)) + ") "
        print_str += red_color_string
        print_str += str("+" * abs(int(max_temp_column[i])))
        print_str += " " + str(int(max_temp_column[i])) + " C\n"
        print_str += white_color_string + str("%.2d" % (i + 1)) + ") "
        print_str += blue_color_string
        print_str += str("+" * abs(int(min_temp_column[i])))
        print_str += " " + str(int(min_temp_column[i])) + " C"
        print(print_str)
    return
