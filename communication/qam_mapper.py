import numpy as np

from communication.mapper_interface import MapperInterface


class QAMMapper(MapperInterface):
    def map(self, data):
        # Example of 16-QAM mapping
        symbol_map = {
            (0, 0, 0, 0): -3 - 3j,
            (0, 0, 0, 1): -3 - 1j,
            (0, 0, 1, 0): -3 + 3j,
            (0, 0, 1, 1): -3 + 1j,
            (0, 1, 0, 0): -1 - 3j,
            (0, 1, 0, 1): -1 - 1j,
            (0, 1, 1, 0): -1 + 3j,
            (0, 1, 1, 1): -1 + 1j,
            (1, 0, 0, 0): 3 - 3j,
            (1, 0, 0, 1): 3 - 1j,
            (1, 0, 1, 0): 3 + 3j,
            (1, 0, 1, 1): 3 + 1j,
            (1, 1, 0, 0): 1 - 3j,
            (1, 1, 0, 1): 1 - 1j,
            (1, 1, 1, 0): 1 + 3j,
            (1, 1, 1, 1): 1 + 1j,
        }
        mapped_data = [symbol_map[tuple(bits)] for bits in data.reshape(-1, 4)]
        return np.array(mapped_data)
