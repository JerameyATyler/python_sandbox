def xcorr(x, y, lag):
    from scipy.signal import correlate

    nx = len(x)
    if nx != len(y):
        raise ValueError('x and y must have the same length')

    c = correlate(x, y)

    if lag is None:
        lag = nx - 1

    if lag >= nx or lag < 1:
        raise ValueError('invalid lag')

    return c[nx - 1 - lag: nx + lag]


def ncorr(x, y, lag):
    import numpy as np

    c = xcorr(x, y, lag)

    s = np.sqrt(sum(x ** 2) * sum(y ** 2))

    if s == 0:
        c *= 0
    else:
        c /= s
    return c
