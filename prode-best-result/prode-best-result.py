import random
from get_results import get_results


def evaluatePrediction(pred, results):
    points = 0
    for r in results:
        if r == pred:
            points += 3
        else:
            points += evaluateNotExactResult(pred, r)
    return points


def evaluateNotExactResult(pred, res):
    pred = pred.split('-')
    res = res.split('-')
    if pred[0] > pred[1] and res[0] > res[1]:
        return 1
    elif pred[0] < pred[1] and res[0] < res[1]:
        return 1
    elif pred[0] == pred[1] and res[0] == res[1]:
        return 1
    return 0


def main(insert_manually=False):
    K = 1000000
    POSS_PREDS = ['1-0', '2-0', '2-1', '3-0', '3-1', '3-2', '4-0', '4-1', '4-2', '4-3',
                  '0-0', '1-1', '2-2', '3-3', '4-4',
                  '0-1', '0-2', '1-2', '0-3', '1-3', '2-3', '0-4', '1-4', '2-4', '3-4']

    weights = []

    url = input('Insert URL for match: ')

    if insert_manually:
        for pred in POSS_PREDS:
            odd = float(
                input(f'Insert odds paid for {pred} and press ENTER: '))
            weights.append(1/odd)
    else:
        odds = get_results(
            url, POSS_PREDS)
        weights = [1/odd for odd in odds]

    res = random.choices(POSS_PREDS, weights=weights,
                         k=K)

    pointsSum = {pred: evaluatePrediction(pred, res) for pred in POSS_PREDS}

    print({k: v/K for k, v in sorted(pointsSum.items(),
          key=lambda item: -item[1])})


if __name__ == '__main__':
    main()
