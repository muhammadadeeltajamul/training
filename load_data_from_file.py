import os
import sys

from common import get_month_string_from_number


def clean_file_and_structure_data(param_filename, separator):
    """Cleans the file and return required structure data

    Arguments:
        param_filename: str:
            filename that is to be cleaned
        separator: str:
            used to differentiate between two columns

    Returns:
        file_data_cleaned: list:
            List that contains clean structured data
        column_names: list:
            List that contains all column names
    """

    file_data_cleaned = []
    column_names = []

    # Load and clean the file data
    with open(param_filename, "r") as file:
        file_data = file.readlines()
        if not file_data:
            return [], []
        for line_num in range(0, len(file_data)):
            # Removing useless characters from line
            line = file_data[line_num]
            line = line.replace("\n", '')
            line = line.replace("\t", '')
            line = line.replace("\r", '')

            # Checking if line is empty
            empty_line_flag = True
            for each_character in line:
                if each_character not in ["", "\t", " ", "\n", "\r"]:
                    empty_line_flag = False
                    break
            if empty_line_flag:
                continue

            line_data = line.split(separator)
            if line_num == 0:
                # Creating indexes in dictionary for each column
                # It will be used in the end
                for each in line_data:
                    column_names.append(each)
            else:
                # Changing data from string to integer/float
                # Starting loop from 1 to skip the date column
                for list_index in range(1, len(line_data)):
                    # Column that has text values
                    if list_index == 21:
                        continue
                    if line_data[list_index] == "":
                        line_data[list_index] = 0
                    else:
                        try:
                            line_data[list_index] = float(
                                line_data[list_index])
                        except ValueError:
                            print("Invalid data in ", param_filename)
                            sys.exit()

            # Entering clean line data into list
            file_data_cleaned.append(line_data)
    return column_names, file_data_cleaned


def load_data_from_file(param_filename):
    """Create a dictionary from file data

    Arguments:
        param_filename: str:
            filename that contains data
            uses '.csv', '.tsv' and '.txt'
                '.txt' file must have data similar to .csv

    Returns:
        month_data: dict:
            Dictionary that contains complete data
    """

    filename, file_ext = os.path.splitext(param_filename)
    file_ext = str(file_ext).lower()
    if file_ext == ".csv" or file_ext == ".txt":
        separator = ","
    elif file_ext == ".tsv":
        separator = "\t"
    else:
        print(file_ext + " Invalid input file found")
        return
    if not os.path.exists(param_filename):
        print("Data file not found")
        sys.exit()

    month_dictionary = {}
    column_names, file_data_cleaned = clean_file_and_structure_data(
        param_filename, separator)

    if not column_names:
        return month_dictionary

    if not file_data_cleaned:
        return month_dictionary

    for column in column_names:
        month_dictionary[column] = []

    # Appending clean data in month dictionary
    for i in range(1, len(file_data_cleaned)):
        for j in range(0, len(file_data_cleaned[i])):
            month_dictionary[file_data_cleaned[0][j]].append(
                file_data_cleaned[i][j])
    return month_dictionary


def load_month_data(weather_data, path, month: int, year: int):
    """Loads passed month data into weather data class

    Arguments:
        weather_data: WeatherData:
            object of class WeatherData
        path: str:
            path of the dir where all files are located
        month: int:
            Represents month. range(1-12)
        year: int:
            Represents year
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
    """Loads passed year data into weather data class

    Arguments:
        weather_data: WeatherData:
            object of class WeatherData
        path: str:
            path of the dir where all files are located
        year: int:
            Represents year
    """

    for i in range(1, 13):
        load_month_data(weather_data, path, i, year)
    return
