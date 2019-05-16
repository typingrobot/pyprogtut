# table.py
import sys


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

    formatter.headings(colnames)
    for obj in objects:
        rowdata = [str(getattr(obj, colname)) for colname in colnames]
        formatter.row(rowdata)


class TableFormatter():
    def __init__(self, outfile=None):
        if outfile is None:
            outfile = sys.stdout
        self.outfile = outfile

    def headings(self, headers):
        raise NotImplementedError

    def row(self, rowdata):
        raise NotImplementedError


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
