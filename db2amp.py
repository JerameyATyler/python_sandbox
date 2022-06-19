def decibel_to_amplitude(dB):
    import numpy as np
    return np.exp(dB/20*np.log(10))
