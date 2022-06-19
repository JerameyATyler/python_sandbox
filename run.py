def run():
    from variables import variables
    from GenerateStimuli import generate_stimuli
    import soundfile as sf
    from pathlib import Path
    from Cepbimo import cepbimo
    from PlotICC import icc
    from PlotBAP import plot_bap
    from BinauralActivityPattern import binaural_activity_pattern

    v = variables()
    x = v['x']
    fs = v['fs']
    source_azimuths = v['source_azimuths']
    source_zeniths = v['source_zeniths']

    reflection_azimuths = v['reflection_azimuths']
    reflection_zeniths = v['reflection_zeniths']
    reflection_amplitudes = v['reflection_amplitudes']
    reflection_delays = v['reflection_delays']
    reverberation_amplitude = v['reverberation_amplitude']
    reverberation_delay = v['reverberation_delay']
    reverberation_time = v['reverberation_time']

    assert len(source_azimuths) == len(source_zeniths)
    assert len(reflection_azimuths) == len(reflection_zeniths) == len(reflection_amplitudes) == len(reflection_delays)

    for i in range(len(source_azimuths)):
        y, fs_y = generate_stimuli(x, fs, source_azimuths[i], source_zeniths[i], reflection_azimuths,
                                   reflection_zeniths, reflection_amplitudes, reflection_delays,
                                   reverberation_amplitude, reverberation_delay, reverberation_time)
        sf.write(str(Path(f'output/a{source_azimuths[i]:04d}e{source_zeniths[i]:04d}_final.wav')), y, fs_y,
                 format='wav', subtype='PCM_24')

        left_cepstrum, left_quefrency, right_cepstrum, right_quefrency, xn, xr, xd, xnd = cepbimo(y, fs_y)
        icc(left_cepstrum, left_quefrency, right_cepstrum, right_quefrency, fs_y, xr, xd)
        bap = binaural_activity_pattern(left_cepstrum, right_cepstrum, fs_y, xnd)
        plot_bap(bap, fs_y)


if __name__ == '__main__':
    run()
