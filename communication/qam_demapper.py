import numpy as np

from communication.demapper_interface import DemapperInterface


class QAMDemapper(DemapperInterface):
    def demap(self, data):
        # Example of 16-QAM demapping
        symbol_map = {
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
        demapped_data = [symbol_map[symbol] for symbol in data]
        return np.array(demapped_data).flatten()
