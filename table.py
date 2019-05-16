# table.py
import sys
from abc import ABC, abstractmethod


def print_table(objects, colnames):
    '''
    Make a nicely formatted table showing attributes
    from a list of objects
    '''

    # emit table headers
    for colname in colnames:
        print('{:>10s}'.format(colname), end=' ')
    print()
    for obj in objects:
        # emit a row of data
        for colname in colnames:
            print('{:>10s}'.format(str(getattr(obj, colname))), end=' ')
        print()


def print_table(objects, colnames, formatter):
    '''
    Make a nicely formatted table showing attributes
    from a list of objects
    '''

    if not isinstance(formatter, TableFormatter):
        raise TypeError('formatter must be a table formatter')

    formatter.headings(colnames)
    for obj in objects:
        rowdata = [str(getattr(obj, colname)) for colname in colnames]
        formatter.row(rowdata)


class TablePrinter():
    def __init__(self, formatter):
        self.formatter = formatter

    def print_table(self, objects, colnames):
        '''
        Make a nicely formatted table showing attributes
        from a list of objects
        '''

        self.formatter.headings(colnames)
        for obj in objects:
            rowdata = [str(getattr(obj, colname)) for colname in colnames]
            self.formatter.row(rowdata)


class TableFormatter(ABC):
    def __init__(self, outfile=None):
        if outfile is None:
            outfile = sys.stdout
        self.outfile = outfile

    @abstractmethod
    def headings(self, headers):
        pass

    @abstractmethod
    def row(self, rowdata):
        pass


class TextTableFormatter(TableFormatter):

    def __init__(self, outfile=None, width=10):
        super().__init__(outfile)
        self.width = width

    def headings(self, headers):
        for header in headers:
            print('{:>{}s}'.format(header, self.width),
                  end=' ', file=self.outfile)
        print(file=self.outfile)

    def row(self, rowdata):
        for item in rowdata:
            print('{:>{}s}'.format(item, self.width),
                  end=' ', file=self.outfile)
        print(file=self.outfile)


class CSVTableFormatter(TableFormatter):
    def headings(self, headers):
        print(','.join(headers), end=' ')
        print()

    def row(self, rowdata):
        print(','.join(rowdata), end=' ')
        print()


class HTMLTableFormatter(TableFormatter):
    def headings(self, headers):
        print('<tr>', end='')
        for header in headers:
            print('<th>{}</th>'.format(header), end=' ')
        print('<tr>')

    def row(self, rowdata):
        print('<tr>', end='')
        for item in rowdata:
            print('<tr>{}</tr>'.format(item), end=' ')
        print('<tr>')


class QuotedMixin():
    def row(self, rowdata):
        quoted = ['"{}"'.format(d) for d in rowdata]
        super().row(quoted)
