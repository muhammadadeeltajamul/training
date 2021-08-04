def get_month_year_from_string(string):
    """
    return month and year from combined string

    month and year should be numbers and separated with /
    Examples:
        input string: 12/2006
            output: 12, 2006
        input string: jan/2006
            output: None, None
    """

    month, year = string.split('/')
    try:
        month = int(month)
        year = int(year)
    except Exception:
        print("Invalid input")
        return None, None
    return month, year


def get_month_number_from_string(string):
    """
    Converts 3 characters month name to string
    Example
        input: "jan"
            output: 1
        input: "feb"
            output: 2
        input: "January":
            output: None
    """

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
    """
    converts integer number to 3 character month name
    Examples
        input: 1
            output: "Jan"
        input: 2
            output: "Feb"
        input: 100
            output: ""
    """

    if number == 1:
        return "Jan"
    elif number == 2:
        return "Feb"
    elif number == 3:
        return "Mar"
    elif number == 4:
        return "Apr"
    elif number == 5:
        return "May"
    elif number == 6:
        return "Jun"
    elif number == 7:
        return "Jul"
    elif number == 8:
        return "Aug"
    elif number == 9:
        return "Sep"
    elif number == 10:
        return "Oct"
    elif number == 11:
        return "Nov"
    elif number == 12:
        return "Dec"
    return ""


def get_column_data_from_alias(weather_data, alias, month, year):
    """
    get_column_data_from_alias(weather_data, alias)
    alias: Alias of column
    Returns complete column data from alias
    """
    attrib_name = weather_data.get_column_name_from_alias(alias)
    if attrib_name is None:
        return []
    return weather_data.get_column_data(attrib_name, month, year)
