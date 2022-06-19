def apply_reverberation(x, fs, amplitude, delay, time):
    import numpy as np
    from FFTconv import fft_convolve
    from MixTracks import mix_tracks

    taps = int(np.ceil(delay * fs / 1000))
    t = np.linspace(0, fs * time * 2) / fs
    envelope = np.exp(-t/time*60/20*np.log(10)).T

    carrier_left = np.random.randn(len(t)) * envelope
    carrier_right = np.random.randn(len(t)) * envelope

    left = np.concatenate((np.zeros((taps,)), fft_convolve(x[:, 0], carrier_left)))
    right = np.concatenate((np.zeros((taps,)), fft_convolve(x[:, 1], carrier_right)))
    left = amplitude * left * np.sqrt(np.sum(left ** 2)) / np.sqrt(np.sum(x[:, 0] ** 2))
    right = amplitude * right * np.sqrt(np.sum(right ** 2)) / np.sqrt(np.sum(x[:, 1] ** 2))

    y = np.array([left, right]).T
    y, fs = mix_tracks(x, fs, y, fs)

    return y, fs
