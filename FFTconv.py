def fft_convolve(x, h):
    from scipy.fft import fft, ifft

    X = fft(x, x.size + h.size - 1)
    H = fft(h, x.size + h.size - 1)
    Y = X * H
    return ifft(Y)
