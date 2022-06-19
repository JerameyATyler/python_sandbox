def cepstrum(x, fs, offset, window_length):
    from scipy.signal.windows import hamming
    from numpy.fft import ifft, fft
    import numpy as np

    w = hamming(window_length, False)

    x = x[offset:offset + window_length] * w

    number_unique_points = int(np.ceil((window_length + 1) / 2))

    c = np.real(ifft(np.log(np.abs(fft(x)))))[0:number_unique_points]
    q = np.arange(0, number_unique_points) / fs
    return c, q
