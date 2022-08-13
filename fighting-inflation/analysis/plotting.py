# plotting.ipynb is used as documentation for this file.

import pandas as pd
import numpy as np
from copy import deepcopy


def plot_and_save_charts():
    official_rates_raw = pd.read_csv(
        'in/csv/official_rates/official_rates.csv')

    official_rates = deepcopy(official_rates_raw)
    official_rates['date'] = pd.to_datetime(official_rates['date'],
                                            format='%d/%m/%Y')
    official_rates['buy'] = official_rates['buy'].astype(np.float16)
    official_rates['sell'] = official_rates['sell'].astype(np.float16)

    blue_rates_raw = pd.read_csv('in/csv/blue_rates/blue_rates.csv')

    blue_rates = deepcopy(blue_rates_raw)
    blue_rates['date'] = pd.to_datetime(blue_rates['date'],
                                        format='%d-%m-%Y')
    blue_rates['buy'] = blue_rates['buy'].astype(np.float16)
    blue_rates['sell'] = blue_rates['sell'].astype(np.float16)

    inflation_rates_raw = pd.read_csv(
        'in/csv/inflation_rates/inflation_rates.csv')

    inflation_rates = deepcopy(inflation_rates_raw)
    inflation_rates['year'] = inflation_rates['month'].str[3:].astype(np.int)
    inflation_rates['month'] = inflation_rates['month'].str[:2].astype(np.int8)
    inflation_rates['rate'] = inflation_rates['rate'].astype(
        np.float16).round(1)
    inflation_rates = inflation_rates[['month', 'year', 'rate']]

    income_raw = pd.read_csv('in/csv/income/income.csv')

    income = deepcopy(income_raw)
    income['year'] = income['month'].str[3:].astype(np.int)
    income['month'] = income['month'].str[:2].astype(np.int8)
    income['income'] = income['income'].astype(np.uint16)
    income = income[['month', 'year', 'income']]

    official_rates['month'] = official_rates['date'].dt.month
    official_rates['year'] = official_rates['date'].dt.year
    official_rate_by_month = official_rates.groupby(
        ['month', 'year']).agg({'buy': 'mean'})
    official_rate_by_month.reset_index()

    official_rate_income = official_rate_by_month.merge(
        income, how='inner', left_on=['month', 'year'], right_on=['month', 'year'])

    official_rate_income['income_ars'] = official_rate_income['buy'] * \
        official_rate_income['income']

    official_rate_income_inflation =\
        official_rate_income.merge(inflation_rates, how='left', left_on=[
            'month', 'year'], right_on=['month', 'year'])

    official_rate_income_inflation['inflation_rate'] = official_rate_income_inflation['rate']
    del official_rate_income_inflation['rate']

    official_rate_income_inflation['inflation_factor'] = official_rate_income_inflation['inflation_rate'] / 100 + 1
    official_rate_income_inflation['cumm_inflation_factor'] =\
        official_rate_income_inflation['inflation_factor'].cumprod()
    del official_rate_income_inflation['inflation_rate']

    blue_rates['month'] = blue_rates['date'].dt.month
    blue_rates['year'] = blue_rates['date'].dt.year
    blue_rates['avg_rate'] = (blue_rates['buy'] + blue_rates['sell']) / 2
    avg_blue_rate_by_month = blue_rates.groupby(
        ['month', 'year']).agg({'avg_rate': 'mean'}).reset_index()

    data =\
        official_rate_income_inflation.merge(avg_blue_rate_by_month, how='left', left_on=[
            'month', 'year'], right_on=['month', 'year'])
    data['blue_usd_avg_rate'] = data['avg_rate']
    del data['avg_rate']

    data.index = [str(int(row['month'])) + '-' + str(int(row['year']))
                  for i, row in data.iterrows()]
    data['month_year'] = '0' + data.index

    data['income_blue_usd'] = data['income_ars'] / data['blue_usd_avg_rate']

    data['income_ars_adj_inflation'] = data['income_ars'] / \
        data['cumm_inflation_factor']

    ax1 = data.rename(columns={'month_year': 'Month', 'income_ars_adj_inflation': 'ARS income adjusted by inflation'})\
        .plot(x='Month', y='ARS income adjusted by inflation', color='orange', figsize=(15, 7), style='.-')
    ylim = ax1.get_ylim()
    ax1.set_ylim(ylim[0] * 0.975, ylim[1] * 1.025)

    ax2 = data.rename(columns={'month_year': 'Month', 'income_blue_usd': 'Blue USD income'})\
        .plot(x='Month', y='Blue USD income', color='blue', figsize=(15, 7), style='.-')
    ylim = ax2.get_ylim()
    ax2.set_ylim(ylim[0] * 0.975, ylim[1] * 1.025)

    first_official_usd_buy_value = data.iloc[0].loc['buy']
    first_inflation_rate = data.iloc[0].loc['cumm_inflation_factor']
    first_usd_value = data.iloc[0].loc['blue_usd_avg_rate']

    data['normalized_official_usd'] = data['buy'] / \
        first_official_usd_buy_value
    data['normalized_inflation'] = data['cumm_inflation_factor'] / \
        first_inflation_rate
    data['normalized_blue_usd'] = data['blue_usd_avg_rate'] / first_usd_value

    ax3 = data.dropna().plot(x='month_year', y='normalized_official_usd',
                             color='lightgreen', figsize=(15, 7))
    data.dropna().plot(x='month_year', y='normalized_blue_usd', color='blue', ax=ax3)
    data.dropna().plot(x='month_year', y='normalized_inflation', color='red', ax=ax3)
    ylim = ax3.get_ylim()
    ax3.set_ylim(ylim[0] * 0.975, ylim[1] * 1.025)

    ax1.get_figure().savefig('out/inflation.png')
    ax2.get_figure().savefig('out/blue.png')
    ax3.get_figure().savefig('out/comparison.png')
