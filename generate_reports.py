from common import get_column_data_from_alias
from common import get_month_string_from_number
from constants import TEXT_STYLE_NORMAL, TEXT_STYLE_BOLD
from constants import TEXT_COLOR_RED, TEXT_COLOR_BLUE
from constants import TEXT_COLOR_WHITE
from load_data_from_file import load_month_data, load_year_data
from WeatherData import WeatherData


def change_text_color(text, style=0, color=37, background_color=40):
    """This functions returns a string whose color is changed

    Arguments:
        text: str:
            Text data whose color you want to change
        style: int:
            Changes style, default style "Normal"
        color: int:
            Changes text color, default color "White"
        background_color: int:
            Changes background color, default "Black"

    Returns:
        Returns the string with colored text
    """

    try:
        style = int(style)
        color = int(color)
        background_color = int(background_color)
    except ValueError:
        return ""
    color_string = "\033[" + str(style) + ";" + str(color) + ";"\
                   + str(background_color) + "m" + str(text)
    return color_string


def get_boundary_element(year_data_list, get_maximum=True, key_index=0):
    """Returns the maximum or minimum element of a 2D-array.

    Arguments:
        year_data_list: list:
            Input 2D list whose boundary element is required.
        get_maximum: Bool:
            Maximum or minimum value.
            True for maximum and False for minimum
            default: True
        key_index: int:
            Key of 2nd dimension of array for sorting
            default: 0

    Returns:
        value: int:
            boundary value
    """

    year_data_list = sorted(year_data_list, reverse=get_maximum,
                            key=lambda x: x[key_index])
    temperature = year_data_list[0][0]
    month = get_month_string_from_number(year_data_list[0][2])
    year = year_data_list[0][1]
    return temperature, month, year


def get_monthly_graph_data(weather_data, path, month, year):
    """Loads the month data and returns max temperature,
    min temperature and len to iterate list

    Arguments:
        weather_data: dict:
            Object of class WeatherData
        path: str:
            Folder consisting of all data files
        month: int:
            Representing month range(1-12)
        year: int:
            Representing year

    Returns:
        maximum_temperature_list: list:
            List that contains maximum temperature of month
        minimum_temperature_list: list:
            List that contains minimum temperature of month
        len_: int:
            Returns the length of the list
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
    """Generate yearly weather report

    Arguments:
        weather_data: dict:
            Object of class WeatherData
        path: str:
            Folder consisting of all data files
        year: int:
            Representing year
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
            max_temperature_index = max_temp_column.index(max(
                max_temp_column))
            max_temp_of_month = max_temp_column[max_temperature_index]
            day = max_temperature_index + 1
            max_temp_list.append([max_temp_of_month, day, month])

        # Min temperature
        min_temp_column = get_column_data_from_alias(weather_data,
                                                     "min_temperature",
                                                     month, year)
        if min_temp_column:
            min_temperature_index = min_temp_column.index(min(
                min_temp_column))
            min_temp_of_month = min_temp_column[min_temperature_index]
            day = min_temperature_index + 1
            min_temp_list.append([min_temp_of_month, day, month])

        # Max humidity
        max_humidity_column = get_column_data_from_alias(weather_data,
                                                         "max_humidity",
                                                         month, year)
        if max_humidity_column:
            max_humidity_index = max_humidity_column.index(max(
                max_humidity_column))
            max_humidity_of_month = max_humidity_column[
                max_humidity_index]
            day = max_humidity_index + 1
            max_humidity_list.append([max_humidity_of_month, day,
                                      month])

        # Min humidity
        min_humidity_column = get_column_data_from_alias(weather_data,
                                                         "min_humidity",
                                                         month, year)
        if min_humidity_column:
            min_humidity_index = min_humidity_column.index(min(
                min_humidity_column))
            min_humidity_of_month = min_humidity_column[
                min_humidity_index]
            day = min_humidity_index + 1
            min_humidity_list.append([min_humidity_of_month, day,
                                      month])

    # Checking largest/smallest in each of the lists
    if len(max_temp_list) > 1:
        temperature, month, year = get_boundary_element(max_temp_list,
                                                        get_maximum=True)
        print("Maximum Temperature:", temperature, "C on", month, year)

    if len(min_temp_list) > 1:
        temperature, month, year = get_boundary_element(min_temp_list,
                                                        get_maximum=False)
        print("Minimum Temperature:", temperature, "C on", month, year)

    if len(max_humidity_list) > 1:
        humidity, month, year = get_boundary_element(max_humidity_list,
                                                     get_maximum=True)
        print("Maximum Humidity:", humidity, "% on", month, year)

    if len(min_humidity_list) > 1:
        humidity, month, year = get_boundary_element(min_humidity_list,
                                                     get_maximum=False)
        print("Minimum Humidity:", humidity, "% on", month, year)
    return


def compute_monthly_weather_report(weather_data: WeatherData,
                                   path, month: int,
                                   year: int):
    """Generates monthly weather report

    Arguments:
        weather_data: dict:
            Object of class WeatherData
        path: str:
            Folder consisting of all data files
        month: int:
            Representing month range(1-12)
        year: int:
            Representing year
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
    """Generates monthly weather graph on same line

    Arguments:
        weather_data: dict:
            Object of class WeatherData
        path: str:
            Folder consisting of all data files
        month: int:
            Representing month range(1-12)
        year: int:
            Representing year
    """

    max_temp_column, min_temp_column, len_ = get_monthly_graph_data(
                                    weather_data, path, month, year)
    for i in range(0, len_):
        print_str = change_text_color(str("%.2d) " % (i + 1)),
                                      style=TEXT_STYLE_BOLD,
                                      color=TEXT_COLOR_WHITE)
        print_str += change_text_color("+" * abs(int(min_temp_column[i])),
                                       style=TEXT_STYLE_NORMAL,
                                       color=TEXT_COLOR_BLUE)
        print_str += change_text_color("+" * abs(int(max_temp_column[i])),
                                       color=TEXT_COLOR_RED)
        print_str += change_text_color(" " + str(min_temp_column[i]) + "C",
                                       color=TEXT_COLOR_BLUE)
        print_str += change_text_color("-",
                                       style=TEXT_STYLE_BOLD,
                                       color=TEXT_COLOR_WHITE)
        print_str += change_text_color(str(max_temp_column[i]) + "C",
                                       style=TEXT_STYLE_NORMAL,
                                       color=TEXT_COLOR_RED)
        print(print_str)
    return


def compute_monthly_weather_graph_two_lines(weather_data: WeatherData,
                                            path, month: int, year: int):
    """Generates monthly weather graph on two lines

    Arguments:
        weather_data: dict:
            Object of class WeatherData
        path: str:
            Folder consisting of all data files
        month: int:
            Representing month range(1-12)
        year: int:
            Representing year
    """

    max_temp_column, min_temp_column, len_ = get_monthly_graph_data(
        weather_data, path, month, year)
    for i in range(0, len_):
        print_str = change_text_color(str("%.2d) " % (i + 1)),
                                      style=TEXT_STYLE_BOLD,
                                      color=TEXT_COLOR_WHITE)
        print_str += change_text_color(str("+"
                                           * abs(int(max_temp_column[i]))),
                                       style=TEXT_STYLE_NORMAL,
                                       color=TEXT_COLOR_RED)
        print_str += change_text_color(" "
                                       + str(int(max_temp_column[i])) + " C\n",
                                       style=TEXT_STYLE_NORMAL,
                                       color=TEXT_COLOR_RED)
        print_str += change_text_color(str("%.2d) " % (i + 1)),
                                       style=TEXT_STYLE_BOLD,
                                       color=TEXT_COLOR_WHITE)
        print_str += change_text_color(str("+"
                                           * abs(int(min_temp_column[i]))),
                                       style=TEXT_STYLE_NORMAL,
                                       color=TEXT_COLOR_BLUE)
        print_str += change_text_color(" "
                                       + str(int(min_temp_column[i])) + " C",
                                       style=TEXT_STYLE_NORMAL,
                                       color=TEXT_COLOR_BLUE)
        print(print_str)
    return
