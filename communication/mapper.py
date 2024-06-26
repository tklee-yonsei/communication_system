from communication.mapper_interface import MapperInterface


class Mapper(MapperInterface):
    def map(self, data):
        return 2 * data - 1
