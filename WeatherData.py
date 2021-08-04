import pandas as pd


class WeatherData:
    """
    This class holds all the data of the weather.
    To add data in the structure, use method add_month_data
    To get data use "get_column_data" method with month and year
    To get the column name use method get_column_name_from_alias.
        Valid aliases are
            max_temperature
            min_temperature
            max_humidity
            min_humidity
            mean_humidity
    """

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
        """
        add_month_data(self, month, year, month_data)
        self: object in which you want to add data
        month: integer range(1-12)
        year: integer representing year
        month_data: pandas data frame having data of all days

        Stores month weather information in data structure
        """

        if not (0 < month < 13):
            print("Invalid month ", month, ". Data not added")
            return
        month = str(month)
        year = str(year)
        if year not in self.__complete_data:
            self.__complete_data[year] = {}
        if month not in self.__complete_data[year]:
            self.__complete_data[year][month] = {}
        self.__complete_data[year][month] = month_data
        return

    def get_column_name_from_alias(self, string):
        """
        Pass alias to get column name
        Valid aliases are
            max_temperature
            min_temperature
            max_humidity
            min_humidity
            mean_humidity

        Returns column name for other function from alias
        """

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
        """
        get_column_data(column_name, month, year)

        Get column_name from method get_column_came_from_alias
        month: integer range(1-12)
        year: integer
        """

        if not (0 < month < 13):
            print("Invalid month", month)
            return []
        month = str(month)
        year = str(year)
        try:
            return self.__complete_data[year][month][column_name].tolist()
        except Exception:
            print("Data not found")
        return []
