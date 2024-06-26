import numpy as np

from noise.noise_interface import NoiseInterface


class AWGNNoise(NoiseInterface):
    def __init__(self, snr_db):
        self.snr_db = snr_db

    def apply(self, signal):
        # 데시벨 단위의 SNR 값을 선형 단위로 변환합니다.
        snr_linear = 10 ** (self.snr_db / 10)
        # 신호의 평균 전력을 계산합니다.
        power_signal = np.mean(np.abs(signal) ** 2)
        # 신호 전력을 SNR로 나누어 노이즈 전력을 계산합니다.
        noise_power = power_signal / snr_linear
        # 노이즈를 생성합니다.
        # 여기서 np.random.randn(*signal.shape)는 신호와 동일한 형태의 가우시안 분포를 따르는 랜덤한 실수 배열을 생성합니다.
        # 이 값에 복소수 1j를 곱하여 복소수 노이즈를 만듭니다.
        # 노이즈 전력의 제곱근을 곱하여 노이즈의 크기를 조절합니다.
        noise = np.sqrt(noise_power / 2) * (
            np.random.randn(*signal.shape) + 1j * np.random.randn(*signal.shape)
        )
        # *signal.shape는 Python의 unpacking 연산자입니다. 예를 들어, signal.shape가 (4, 4)라면, *signal.shape는 4, 4로 변환됩니다.
        return signal + noise
