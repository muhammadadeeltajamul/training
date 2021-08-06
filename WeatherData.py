class WeatherData:
    """This class holds all the data of the weather.

    Methods:
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

    def add_month_data(self, month: int, year: int, month_data):
        """Stores month weather information in data structure

        Arguments:
            month: int:
                integer range(1-12)
            year: int:
                integer representing year
            month_data: dict:
                dictionary having data of all days
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
        """Returns column name from alias

        Arguments:
            string: str:
                Pass alias to get column name
                Valid aliases are
                    max_temperature
                    min_temperature
                    max_humidity
                    min_humidity
                    mean_humidity
        """

        string = string.lower()
        mapping_dictionary = {
            "max_temperature": self.__max_temp_c,
            "min_temperature": self.__min_temp_c,
            "max_humidity": self.__max_humidity,
            "min_humidity": self.__min_humidity,
            "mean_humidity": self.__mean_humidity
        }
        return mapping_dictionary.get(string, None)

    def get_column_data(self, column_name, month: int, year: int):
        """Returns column data from column name, month and year

        Arguments:
            column_name: str:
                column name whose data is required
            month: int:
                month in integer range(1-12)
            year: int:
                integer representing year

        Returns:
            column_data: list:
                list that contains the whole month data
        """

        if not (0 < month < 13):
            print("Invalid month", month)
            return []
        month = str(month)
        year = str(year)
        try:
            return self.__complete_data[year][month][column_name]
        except Exception:
            print("Data not found for " + year + "/" + month)
        return []
