from noise.noise_interface import NoiseInterface


class NoNoise(NoiseInterface):
    def apply(self, signal):
        raise NotImplementedError("NoNoise의 apply 메소드를 구현하여야 합니다.")
