import csv
from copy import copy


def save_preds_to_csv(filename, preds, home_team, away_team):
    with open(filename, 'r') as file:
        fieldnames = file.readline().split(',')

    with open(filename, 'a', newline='') as file:
        data = copy(preds)
        data['Home'] = home_team
        data['Away'] = away_team
        data['Res'] = None

        writer = csv.DictWriter(file, delimiter=',',
                                fieldnames=fieldnames + ['Res'])
        writer.writerow(data)
