# port.py

import csv


def read_portfolio(filename, *, errors='warn'):
    '''
    Computes total shares*price
    '''
    if errors not in {'warn', 'silent', 'raise'}:
        raise ValueError("errors must be warn, silent, or raise")

    portfolio = []
    with open(filename, 'r') as f:
        rows = csv.reader(f)
        headers = next(f)
        for rowno, row in enumerate(rows, start=1):
            try:
                row[2] = int(row[2])
                row[3] = float(row[3])
            except ValueError as err:
                if errors == 'warn':
                    print('Row:', rowno, 'Bad row:', row)
                    print('Row:', rowno, 'Reason:', err)
                elif errors == 'raise':
                    raise
                else:
                    pass

                continue
            record = tuple(row)
            portfolio.append(record)
    return portfolio


portfolio = read_portfolio('portfolio.csv')

total = 0.0
for name, date, shares, price in portfolio:
    total += shares * price

print('Total cost', total)
