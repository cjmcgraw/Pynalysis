from math import sqrt
from bisect import insort

class Statistics(object):

    def __init__(self):
        self._sum = 0.0
        self._mean = 0.0
        self._data = []
        self._std_dev = 0.0
        self.__recalc_mean = False
        self.__recalc_std_dev = False
    
    @property
    def n(self):
        return len(self._data)

    @property
    def sum(self):
        return self._sum

    @property
    def mean(self):
        if self.__recalc_mean:
            self._calculate_mean()
        return self._mean

    @property
    def median(self):
        if len(self._data) <= 0:
            raise IndexError("Cannot find median with empty data set")

        q = self._data
        mid = int(len(q) / 2)
        if len(q) % 2 is 0:
            return (q[mid - 1] + q[mid]) / 2
        return q[mid]

    def _calculate_mean(self):
        self._mean = self._sum / len(self._data)
        self.__recalc_mean = False

    @property
    def std_dev(self):
        if self.__recalc_std_dev and len(self._data) > 1:
            self._calculate_std_dev()
        return self._std_dev

    def _calculate_std_dev(self):
        square_mean_diffs = self._calculate_square_of_mean_diffs()
        self._std_dev = sqrt(sum(square_mean_diffs) / (len(self._data) - 1))
        self.__recalc_std_dev = False
    
    def _calculate_square_of_mean_diffs(self):
        for x in self._data:
            yield (x - self.mean) ** 2

    def update(self, values):
        try:
            self._update_list(values)
        except TypeError:
            self._update_value(values)

    def _update_list(self, values):
        for x in values:
            self._update_value(x)

    def _update_value(self, value):
        self._sum += value
        self._update_data(value)
        self.__recalc_mean = True
        self.__recalc_std_dev = True
    
    def _update_data(self, value):
        insort(self._data, value)
