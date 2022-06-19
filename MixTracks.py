def mix_tracks(a, fs_a, b, fs_b):
    import numpy as np
    import librosa

    fs = np.max((fs_a, fs_b))

    assert a.ndim == b.ndim

    if fs > fs_a:
        a = librosa.resample(a, orig_sr=fs_a, target_sr=fs)
    if fs > fs_b:
        b = librosa.resample(b, orig_sr=fs_b, target_sr=fs)

    max_length = max(a.size, b.size)

    y = np.zeros((max_length, a.ndim))
    for i in range(a.ndim):
        ax = librosa.util.fix_length(a[:, i], size=max_length)
        bx = librosa.util.fix_length(b[:, i], size=max_length)

        y[:, i] = ax + bx
    return y, fs
