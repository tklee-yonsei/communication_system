from communication.demapper_interface import DemapperInterface


class Demapper(DemapperInterface):
    def demap(self, data):
        return (data > 0).astype(int)
