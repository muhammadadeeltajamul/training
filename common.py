def get_month_year_from_string(string):
    """Returns month and year from combined string
    month and year should be numbers and separated with /

    Arguments:
        string: str
            String containing month year in format mm/yyyy

    Returns:
        month: int, year: int
            Month and year separated in integer
    """

    month, year = string.split('/')
    try:
        month = int(month)
        year = int(year)
    except Exception:
        print("Invalid month/year. Input must be of format yyyy/mm")
        return None, None
    return month, year


def get_month_number_from_string(string):
    """
    Converts 3 characters month name to string

    Arguments:
        string: str
            String containing month

    Returns:
        month: int
            Returns month as number from string
    """

    string = str(string).lower()
    # Map month name to number
    mapping_dictionary = {
        "jan": 1,
        "feb": 2,
        "mar": 3,
        "apr": 4,
        "may": 5,
        "jun": 6,
        "jul": 7,
        "aug": 8,
        "sep": 9,
        "oct": 10,
        "nov": 11,
        "dec": 12
    }
    return mapping_dictionary.get(string, None)


def get_month_string_from_number(number: int):
    """Converts integer number to 3 character month name

    Argument:
        number: int

    Returns:
        string: str:
            String of length 3 that represents month
    """

    # Maps month number to month name
    mapping_dictionary = {
        1: "Jan",
        2: "Feb",
        3: "Mar",
        4: "Apr",
        5: "May",
        6: "Jun",
        7: "Jul",
        8: "Aug",
        9: "Sep",
        10: "Oct",
        11: "Nov",
        12: "Dec"
    }
    return mapping_dictionary.get(number, "")


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
