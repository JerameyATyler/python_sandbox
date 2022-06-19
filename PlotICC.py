def icc(left_cepstrum, left_quefrency, right_cepstrum, right_quefrency, fs, xr, xd):
    import numpy as np
    import matplotlib.pyplot as plt

    taps = int(np.ceil(1 * fs / 1000))

    fig, ax = plt.subplots(3, 1)

    ax[0].plot(left_quefrency * 1000, left_cepstrum, 'r')
    ax[0].set_xlim((1, 40))
    ax[0].set_ylim((-0.3, 0.3))
    ax[0].set_xlabel('Quefrency [ms]', **dict(fontsize=14))
    ax[0].set_ylabel('Amp./Left', **dict(fontsize=14))
    ax[0].set_title('Amplitude cepstrum of the signal segment (quefrencies from 1 ms to 20 ms)')

    ax[1].plot(right_quefrency * 1000, right_cepstrum, 'r')
    ax[1].set_xlim((1, 40))
    ax[1].set_ylim((-0.3, 0.3))
    ax[1].set_xlabel('Quefrency [ms]', **dict(fontsize=14))
    ax[1].set_ylabel('Amp./Right', **dict(fontsize=14))
    ax[1].set_title('Amplitude cepstrum of the signal segment (quefrencies from 1 ms to 20 ms)')

    ax[2].plot(np.linspace(-taps, taps, xr.shape[0]) / taps, xr / 200)
    ax[2].plot(np.linspace(-taps, taps, xd.shape[0]) / taps, xd / 200, 'r')
    ax[2].set_xlabel('ITD [ms]', **dict(fontsize=14))
    ax[2].set_ylabel('Correlation', **dict(fontsize=14))
    ax[2].set_title('Interaural Cross Correlation')

    plt.show()
