def variables():
    from pathlib import Path
    import os
    import librosa

    path = str(Path('data/anechoic_recordings/denon6.wav'))
    assert os.path.isfile(path)
    x, fs = librosa.load(path, sr=48000, mono=False)

    return dict(
        x=x,
        fs=fs,
        source_azimuths=[300, 0, 30, 45, 60],
        source_zeniths=[0, 0, 0, 0, 0],
        reflection_azimuths=[45, 315, 60, 300],
        reflection_zeniths=[0, 0, 0, 0],
        reflection_amplitudes=[0.8, 0.6, 0.55, 0.5],
        reflection_delays=[20, 26, 36, 44],
        reverberation_amplitude=0.025,
        reverberation_delay=46,
        reverberation_time=2)
