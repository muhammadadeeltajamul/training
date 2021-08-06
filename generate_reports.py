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
    except Exception:
        return ""
    color_string = "\033[" + str(style) + ";" + str(color) + ";"\
                   + str(background_color) + "m" + str(text)
    return color_string


def arg_max(list_):
    """Returns the index of maximum element of list

    Arguments:
        list_:
            list whose maximum index is required

    Returns:
        index: int:
            The index whose value is maximum
    """

    if not list_:
        return None
    max_index = 0
    max_value = list_[max_index]
    for i in range(0, len(list_)):
        if list_[i] > max_value:
            max_value = list_[i]
            max_index = i
    return max_index


def arg_min(list_):
    """Returns the index of minimum element of list

    Arguments:
        list_:
            list whose minimum index is required

    Returns:
        index: int:
            The index whose value is minimum
    """

    if not list_:
        return None
    min_index = 0
    min_value = list_[min_index]
    for i in range(0, len(list_)):
        if list_[i] < min_value:
            min_value = list_[i]
            min_index = i
    return min_index


def get_boundary_element(list_, max_=True, index=0):
    """Returns the maximum or minimum element of a 2D-array.

    Arguments:
        list_: list:
            Input list whose boundary element is required
        max_: Bool:
            Maximum or minimum value.
            True for maximum and False for minimum
            default: True
        index: int:
            Key of 2nd dimension of array
            default: 0

    Returns:
        value: int:
            boundary value
    """

    list_ = sorted(list_, reverse=max_, key=lambda x: x[index])
    temperature = list_[0][0]
    month = get_month_string_from_number(list_[0][2])
    year = list_[0][1]
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
            max_index = arg_max(max_temp_column)
            max_temp_list.append([max_temp_column[max_index],
                                  max_index + 1, month])

        # Min temperature
        min_temp_column = get_column_data_from_alias(weather_data,
                                                     "min_temperature",
                                                     month, year)
        if min_temp_column:
            min_index = arg_min(min_temp_column)
            min_temp_list.append([min_temp_column[min_index],
                                  min_index + 1, month])

        # Max humidity
        max_humidity_column = get_column_data_from_alias(weather_data,
                                                         "max_humidity",
                                                         month, year)
        if max_humidity_column:
            max_index = arg_max(max_humidity_column)
            max_humidity_list.append([max_humidity_column[max_index],
                                      max_index + 1, month])

        # Min humidity
        min_humidity_column = get_column_data_from_alias(weather_data,
                                                         "min_humidity",
                                                         month, year)
        if min_humidity_column:
            min_index = arg_min(min_humidity_column)
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
