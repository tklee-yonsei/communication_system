from communication.mapper_interface import MapperInterface


class QAMMapper(MapperInterface):
    def map(self, data):
        raise NotImplementedError("QAMMapper map 메소드를 구현하여야 합니다.")
