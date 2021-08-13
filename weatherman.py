import argparse
import os
import sys

from common import get_month_year_from_string
from generate_reports import compute_monthly_weather_report
from generate_reports import compute_monthly_weather_graph_two_lines
from generate_reports import compute_monthly_weather_graph_same_line
from generate_reports import compute_yearly_weather_report
from WeatherData import WeatherData

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
                            temperature of a month in two lines""")
    parser.add_argument('-b', action='append', type=str,
                        help="""Draws highest and lowest
                        temperature of a month in same line""")

    args = parser.parse_args()
    os.system("clear")
    if len(sys.argv) < 3:
        print("No argument given for reports output")
        sys.exit()
    if not os.path.isdir(args.path):
        raise "Invalid path to dir given"

    weather_data = WeatherData()
    path = args.path
    if weather_data is None:
        raise "Weather Data doesn't exist"

    if args.e is not None:
        for each in args.e:
            print("\n====================> Year Report ", each)
            try:
                year = int(each)
            except Exception:
                raise "Invalid year \"" + str(each) + "\""
            compute_yearly_weather_report(weather_data, path, year)

    if args.a is not None:
        for each in args.a:
            print("\n====================> Month Report ", each)
            try:
                year, month = get_month_year_from_string(each)
            except Exception:
                raise "Invalid month/year \"" + str(each) + "\""
            compute_monthly_weather_report(weather_data, path, month,
                                           year)

    if args.c is not None:
        for each in args.c:
            print("\n====================> Month Graph ", each)
            try:
                year, month = get_month_year_from_string(each)
            except Exception:
                raise "Invalid month/year \"" + str(each) + "\""
            compute_monthly_weather_graph_two_lines(weather_data,
                                                    path, month, year)

    if args.b is not None:
        for each in args.b:
            print("\n====================> Month Graph", each)
            try:
                year, month = get_month_year_from_string(each)
            except Exception:
                raise "Invalid month/year \"" + str(each) + "\""
            compute_monthly_weather_graph_same_line(weather_data,
                                                    path, month, year)
