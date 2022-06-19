def apply_hrtf(x, fs, azimuth, zenith):
    from pathlib import Path
    import os
    import librosa
    from scipy.signal import convolve
    import numpy as np

    if fs < 48000:
        x = librosa.resample(x, orig_sr=fs, target_sr=48000)
        fs = 48000

    if x.ndim > 1:
        x_left = x[:, 0]
        x_right = x[:, 0]
    else:
        x_left = x
        x_right = x

    file_string = f'{zenith}e{azimuth:03d}a.wav'
    left = str(Path(f'data/hrtfs/L{file_string}'))
    right = str(Path(f'data/hrtfs/R{file_string}'))

    assert(os.path.isfile(left))
    assert(os.path.isfile(right))

    hrtf_left, left_fs = librosa.load(left, sr=fs, mono=False)
    hrtf_right, right_fs = librosa.load(right, sr=fs, mono=False)

    y_left = convolve(x_left, hrtf_left)
    y_right = convolve(x_right, hrtf_right)

    y = np.array([y_left, y_right]).T

    return y, fs
