import sys
import requests
from bs4 import BeautifulSoup


def get_official_sell_price():
    response = requests.get('https://www.bna.com.ar/Personas')
    res = BeautifulSoup(response.text, 'lxml').findAll(
        'tr', {"class": None})[1].findAll()[2].text.replace(",", ".")
    return(float(res))


def get_blue_prices():
    response = requests.get('https://dolarhoy.com/cotizaciondolarblue')
    res = BeautifulSoup(response.text, 'lxml').findAll(
        'div', {"class": "tile cotizacion_value"})[0].findAll('div', {"class": "value"})
    return (float(res[0].text[1:]), float(res[1].text[1:]))


def main(amount_to_buy):

    blue_prices = get_blue_prices()

    OFFICIAL_SELL = get_official_sell_price()
    BLUE_BUY = blue_prices[0]
    BLUE_SELL = blue_prices[1]
    TAXES_OVER_OFFICIAL = 1.65
    AMOUNT_TO_BUY = amount_to_buy

    print(
        f'\nOfficial USD price is ARS {OFFICIAL_SELL}.')
    print(
        f'Adding taxes ({round((TAXES_OVER_OFFICIAL - 1) * 100)}%), this price goes up to ARS {OFFICIAL_SELL * TAXES_OVER_OFFICIAL}.\n')
    print(
        f'Blue USD buying price is ARS {BLUE_BUY} and selling price {BLUE_SELL}.\n')
    print(f'You want to buy USD {AMOUNT_TO_BUY}.\n\n')

    ARS_BUY_BLUE = AMOUNT_TO_BUY * BLUE_SELL
    print(
        f'You will spend ARS {ARS_BUY_BLUE} and you will get USD {AMOUNT_TO_BUY} (bought at blue price).\n')

    ARS_TO_GET_USD_OFFICIAL = AMOUNT_TO_BUY * OFFICIAL_SELL * TAXES_OVER_OFFICIAL
    BLUE_NEEDED_TO_SELL_TO_BUY_OFFICIAL = round(
        ARS_TO_GET_USD_OFFICIAL / BLUE_BUY, 2)
    print(
        f'You will then spend USD {BLUE_NEEDED_TO_SELL_TO_BUY_OFFICIAL} to buy ARS {ARS_TO_GET_USD_OFFICIAL} (sold at blue price).')
    print(
        f'You will have ARS {ARS_TO_GET_USD_OFFICIAL} and USD {round(AMOUNT_TO_BUY - BLUE_NEEDED_TO_SELL_TO_BUY_OFFICIAL, 2)}.\n')

    print(
        f'Then, you will buy USD {AMOUNT_TO_BUY} spending those ARS {ARS_TO_GET_USD_OFFICIAL} (bought at official price).\n')

    FINAL_USD = 2 * AMOUNT_TO_BUY - BLUE_NEEDED_TO_SELL_TO_BUY_OFFICIAL
    FINAL_USD_PRICE = round(ARS_BUY_BLUE/FINAL_USD, 2)
    print(
        f'You will end with USD {FINAL_USD}.\n')
    print(
        f'If you take into account that you spent ARS {ARS_BUY_BLUE} and got USD {FINAL_USD}, you will have bought each USD at a price of ARS {FINAL_USD_PRICE}.')
    EXTRA_PERC_VALUE_OVER_OFFICIAL = round(((FINAL_USD_PRICE - OFFICIAL_SELL *
                                           TAXES_OVER_OFFICIAL) / (OFFICIAL_SELL * TAXES_OVER_OFFICIAL)) * 100, 2)
    WIN_PERC_OVER_BLUE = round(
        ((BLUE_SELL - FINAL_USD_PRICE) / BLUE_SELL) * 100, 2)
    print(
        f'You will be buying USD at a price {EXTRA_PERC_VALUE_OVER_OFFICIAL}% greater than official value, but at a price {WIN_PERC_OVER_BLUE}% lower than blue value.\n')


if __name__ == '__main__':
    AMOUNT_TO_BUY = int(sys.argv[1]) if len(sys.argv) > 1 else 200
    main(AMOUNT_TO_BUY)
