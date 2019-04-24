# port.py

import reader


def read_portfolio(filename, *, errors='warn'):
    '''
    Computes total shares*price
    '''
    return reader.read_csv(filename, [str, str, int, float], errors=errors)


if __name__ == '__main__':
    portfolio = read_portfolio('portfolio.csv')
    print(portfolio)

    total = 0.0
    for holding in portfolio:
        total += holding['shares'] * holding['price']

    print('Total cost', total)
