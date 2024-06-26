import numpy as np
from noise.noise_interface import NoiseInterface

def apply_noise_and_test(noise_instance, signal, should_equal):
    noisy_signal = noise_instance.apply(signal)
    if should_equal:
        assert np.array_equal(signal, noisy_signal), f"{noise_instance.__class__.__name__} failed"
    else:
        assert not np.array_equal(signal, noisy_signal), f"{noise_instance.__class__.__name__} failed"
