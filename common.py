from constants import month_number_string_mapping


def get_month_year_from_string(month_year_string):
    """Returns month and year from combined string
    month and year should be numbers and separated with "/"

    Arguments:
        month_year_string: str
            String containing month year in format mm/yyyy

    Returns:
        month: int, year: int
            Month and year separated in integer
    """

    try:
        month, year = month_year_string.split('/')
        month = int(month)
        year = int(year)
    except ValueError:
        print("Invalid month/year. Input must be of format yyyy/mm")
        return None, None
    return month, year


def get_month_number_from_string(month_string):
    """
    Converts 3 characters month name to month number

    Arguments:
        month_string: str
            String containing month

    Returns:
        month: int
            Returns month as number from string
    """

    month_string = str(month_string).lower()
    month_key_list = list(month_number_string_mapping.keys())
    month_values_list = list(month_number_string_mapping.values())
    month_values_list = [value.lower() for value in month_values_list]

    try:
        index_to_retrieve = month_values_list.index(month_string)
    except ValueError:
        return None
    return month_key_list[index_to_retrieve]


def get_month_string_from_number(month_number: int):
    """Converts integer number to 3 character month name

    Argument:
        number: int

    Returns:
        string: str:
            String of length 3 that represents month
    """

    return month_number_string_mapping.get(month_number, "")


def get_column_data_from_alias(weather_data, alias, month, year):
    """Returns column data from alias

    Arguments:
        weather_data: dict:
            Contains complete weather data
        alias: str:
            Alias of column
        month: int:
            Month whose data is required
        year: int:
            Year whose data is required

    Returns:
        list_: list:
            Complete column data from alias
    """
    attrib_name = weather_data.get_column_name_from_alias(alias)
    if attrib_name is None:
        return []
    return weather_data.get_column_data(attrib_name, month, year)
