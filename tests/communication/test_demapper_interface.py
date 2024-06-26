import numpy as np

from communication.demapper_interface import DemapperInterface


def demap_and_test(demapper_interface: DemapperInterface, data, demapped_data):
    data_with_demap = demapper_interface.demap(data)
    assert np.array_equal(
        data_with_demap, demapped_data
    ), "f{demapper_interface.__class__.__name__} failed"
