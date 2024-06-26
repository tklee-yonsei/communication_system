import numpy as np

from noise.awgn_noise import AWGNNoise


def test_awgn_noise():
    """
    AWGN 노이즈가 붙으면, 원본 신호와는 달라짐을 테스트합니다.
    """
    signal = np.array([1, 2, 3, 4], dtype=np.float32)
    noise = AWGNNoise(snr_db=10)
    noisy_signal = noise.apply(signal)
    assert not np.array_equal(signal, noisy_signal), "AWGNNoise failed"


def test_awgn_noise_statistics():
    """
    AWGN 노이즈가 붙을 시, 
    
    1. 가우시안 분포를 따르는지, 평균과 분산이 예상과 일치하는지를 검증합니다.
    """
    signal = np.ones(10000, dtype=np.float32)
    noise = AWGNNoise(snr_db=10)
    noisy_signal = noise.apply(signal)
    noise_only = noisy_signal - signal
    mean = np.mean(noise_only)
    variance = np.var(noise_only)
    assert abs(mean) < 0.1, f"Noise mean is not near zero: {mean}"
    expected_variance = np.mean(np.abs(signal) ** 2) / (10 ** (10 / 10))
    assert (
        abs(variance - expected_variance) < expected_variance * 0.1
    ), f"Noise variance is not as expected: {variance}"
