def binaural_activity_pattern(left_cepstrum, right_cepstrum, fs, xnd):
    import numpy as np
    from scipy.signal import convolve
    from scipy.signal.windows import hann

    taps = int(np.ceil(1 * fs / 1000))

    left = left_cepstrum[0:4000]
    right = right_cepstrum[0:4000]

    left_maxi = max(left[700:4000])
    right_maxi = max(right[700:4000])

    left_maxi_d = max(left[0:700])
    right_maxi_d = max(right[0:700])

    left[0:700] *= left_maxi/left_maxi_d
    right[0:700] *= right_maxi/right_maxi_d

    max_index = np.argmax(xnd)
    max_index -= taps + 1

    left_y = np.concatenate([np.zeros((taps,)), left, np.zeros((np.abs(max_index)))])
    right_y = np.concatenate([np.zeros((taps,)), np.zeros((np.abs(max_index))), right])

    signal_left = convolve(left_y, hann(5, sym=False))
    signal_right = convolve(right_y, hann(5, sym=False))

    y = []
    for k in range(-taps, taps):
        y.append(np.sqrt(np.abs(signal_left[taps + 1: taps * 50] * signal_right[taps + 1 + k: taps * 50 + k])).T)
    y = np.array(y)

    return y
