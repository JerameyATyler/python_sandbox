def cepbimo(x, fs):
    from scipy.signal import convolve
    import numpy as np
    from cepstrum import cepstrum
    from ncorr import ncorr, xcorr

    left = x[:, 0]
    right = x[:, 1]

    offset = 1024
    window_length = 1024 * 64 * 4

    left_cepstrum, left_quefrency = cepstrum(left, fs, offset, window_length)
    right_cepstrum, right_quefrency = cepstrum(right, fs, offset, window_length)

    left_filter = np.concatenate([np.ones((1,)), np.zeros((298,)), -left_cepstrum[300:4000]])
    right_filter = np.concatenate([np.ones((1,)), np.zeros((298,)), -right_cepstrum[300:4000]])

    left_y = convolve(left[offset:offset + window_length], left_filter)
    right_y = convolve(right[offset:offset + window_length], right_filter)

    taps = int(np.ceil(1 * fs / 1000))

    xn = ncorr(left[offset:offset + window_length], right[offset:offset + window_length], taps)
    xr = xcorr(left[offset:offset + window_length], right[offset:offset + window_length], taps)
    xd = xcorr(left_y, right_y, taps)
    xnd = ncorr(left_y, right_y, taps)

    return left_cepstrum, left_quefrency, right_cepstrum, right_quefrency, xn, xr, xd, xnd
