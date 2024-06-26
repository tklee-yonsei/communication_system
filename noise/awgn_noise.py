import numpy as np

from noise.noise_interface import NoiseInterface


class AWGNNoise(NoiseInterface):
    def __init__(self, snr_db):
        raise NotImplementedError("AWGNNoise의 생성자를 구현하여야 합니다.")

    def apply(self, signal):
        raise NotImplementedError("AWGNNoise의 apply 메소드를 구현하여야 합니다.")
