from communication.encoder import Encoder
from communication.mapper import Mapper


class Transmitter:
    def __init__(self, encoder: Encoder, mapper: Mapper):
        self.encoder = encoder
        self.mapper = mapper

    def transmit(self, data):
        encoded_data = self.encoder.encode(data)
        mapped_data = self.mapper.map(encoded_data)
        return mapped_data
