def generate_stimuli(x, fs, source_azimuth, source_zenith, reflection_azimuths, reflection_zeniths,
                     reflection_amplitudes, reflection_delays, reverberation_amplitude, reverberation_delay,
                     reverberation_time):
    import numpy as np
    from ApplyHRTF import apply_hrtf
    import soundfile as sf
    from pathlib import Path
    from ApplyReflection import apply_reflection
    from MixTracks import mix_tracks
    from ApplyReverberation import apply_reverberation
    from db2amp import decibel_to_amplitude

    calibration = np.sqrt(np.mean(x ** 2))

    x, fs = apply_hrtf(x, fs, source_azimuth, source_zenith)
    sf.write(str(Path(f'output/a{source_azimuth:04d}e{source_zenith:04d}_hrtf.wav')), x, fs, format='wav',
             subtype='PCM_24')

    y = x
    for i in range(len(reflection_azimuths)):
        r, r_fs = apply_reflection(x, fs, reflection_azimuths[i], reflection_zeniths[i], reflection_amplitudes[i],
                                   reflection_delays[i])
        y, fs = mix_tracks(y, fs, r, r_fs)
    y /= np.max(abs(y)) * 0.9
    sf.write(str(Path(f'output/a{source_azimuth:04d}e{source_zenith:04d}_reflections.wav')), y, fs, format='wav',
             subtype='PCM_24')

    y, fs = apply_reverberation(x, fs, reverberation_amplitude, reverberation_delay, reverberation_time)
    y /= np.max(abs(y)) * 0.9
    sf.write(str(Path(f'output/a{source_azimuth:04d}e{source_zenith:04d}_reverberation.wav')), y, fs, format='wav',
             subtype='PCM_24')

    left = y[:, 0] + calibration * np.random.randn(y.shape[0]) * decibel_to_amplitude(-30)
    right = y[:, 1] + calibration * np.random.randn(y.shape[0]) * decibel_to_amplitude(-30)
    y = np.array([left, right]).T
    y /= np.max(abs(y)) * 0.9

    return y, fs
