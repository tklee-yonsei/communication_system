import numpy as np

from communication.decoder import Decoder
from communication.demapper import Demapper
from communication.encoder import Encoder
from communication.mapper import Mapper
from communication.qam_demapper import QAMDemapper
from communication.qam_mapper import QAMMapper
from communication.receiver import Receiver
from communication.transmitter import Transmitter
from noise.awgn_noise import AWGNNoise
from noise.no_noise import NoNoise


def main():
    data = np.random.randint(0, 2, 100)
    encoder = Encoder()
    # mapper = Mapper()
    # demapper = Demapper()
    mapper = QAMMapper()
    demapper = QAMDemapper()
    decoder = Decoder()

    transmitter = Transmitter(encoder, mapper)
    receiver = Receiver(demapper, decoder)
    no_noise = NoNoise()
    awgn_noise = AWGNNoise(snr_db=10)

    print("Testing NoNoise...")
    transmitted_signal = transmitter.transmit(data)
    noisy_signal = no_noise.apply(transmitted_signal)
    received_data = receiver.receive(noisy_signal)
    print("Original data:    ", data)
    print("Received data:    ", received_data)
    assert np.array_equal(data, received_data), "NoNoise test failed"

    print("--------------")

    print("Testing AWGNNoise...")
    transmitted_signal = transmitter.transmit(data)
    noisy_signal = awgn_noise.apply(transmitted_signal)
    received_data = receiver.receive(noisy_signal)
    print("Original data:    ", data)
    print("Received data:    ", received_data)
    # With AWGN, errors might occur
    # So, we are not asserting equality here, just printing results


if __name__ == "__main__":
    main()
