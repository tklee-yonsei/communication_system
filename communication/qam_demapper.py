import numpy as np

from communication.demapper_interface import DemapperInterface


class QAMDemapper(DemapperInterface):
    def __init__(self):
        self.symbol_map = {
            -3 - 3j: (0, 0, 0, 0),
            -3 - 1j: (0, 0, 0, 1),
            -3 + 3j: (0, 0, 1, 0),
            -3 + 1j: (0, 0, 1, 1),
            -1 - 3j: (0, 1, 0, 0),
            -1 - 1j: (0, 1, 0, 1),
            -1 + 3j: (0, 1, 1, 0),
            -1 + 1j: (0, 1, 1, 1),
            3 - 3j: (1, 0, 0, 0),
            3 - 1j: (1, 0, 0, 1),
            3 + 3j: (1, 0, 1, 0),
            3 + 1j: (1, 0, 1, 1),
            1 - 3j: (1, 1, 0, 0),
            1 - 1j: (1, 1, 0, 1),
            1 + 3j: (1, 1, 1, 0),
            1 + 1j: (1, 1, 1, 1),
        }

    def __closest_symbol(self, symbol):
        """Return the closest symbol from the symbol map."""
        return min(self.symbol_map.keys(), key=lambda x: np.abs(x - symbol))

    def demap(self, data):
        demapped_data = [
            self.symbol_map[self.__closest_symbol(symbol)] for symbol in data
        ]
        return np.array(demapped_data).flatten()
