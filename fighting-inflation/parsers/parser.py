from parsers.blue_rates_parser import parse_blue_rates_download
from parsers.inflation_rates_parser import parse_inflation_rates_download
from parsers.official_rates_parser import parse_bna_rates_download


def parse_files():
    parse_blue_rates_download()
    parse_inflation_rates_download()
    parse_bna_rates_download()
