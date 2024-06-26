from communication.decoder import Decoder
from communication.demapper import Demapper


class Receiver:
    def __init__(self, demapper: Demapper, decoder: Decoder):
        self.demapper = demapper
        self.decoder = decoder

    def receive(self, data):
        demapped_data = self.demapper.demap(data)
        decoded_data = self.decoder.decode(demapped_data)
        return decoded_data
