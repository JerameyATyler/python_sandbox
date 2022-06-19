def apply_reflection(x, fs, azimuth, zenith, amplitude, delay):
    from ApplyHRTF import apply_hrtf
    import numpy as np

    y, fs = apply_hrtf(x, fs, azimuth, zenith)

    left = y[:, 0]
    right = y[:, 1]

    left = amplitude * left
    right = amplitude * right

    taps = int(np.ceil(delay * fs / 1000))

    left = np.concatenate((np.zeros((taps,)), left))
    right = np.concatenate((np.zeros((taps,)), right))

    y = np.array([left, right]).T

    return y, fs
