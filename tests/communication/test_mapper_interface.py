import numpy as np

from communication.mapper_interface import MapperInterface


def map_and_test(mapper_interface: MapperInterface, data, mapped_data):
    data_with_map = mapper_interface.map(data)
    assert np.array_equal(
        data_with_map, mapped_data
    ), "f{mapper_interface.__class__.__name__} failed"
