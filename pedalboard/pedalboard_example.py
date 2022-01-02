#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import soundfile as sf
from pedalboard import (
    Pedalboard,
    Convolution,
    Compressor,
    Chorus,
    Gain,
    Reverb,
    Limiter,
    LadderFilter,
    Phaser,
)

audio, sample_rate = sf.read('just_what_is_it.wav')

# Make a Pedalboard object, containing multiple plugins:
board = Pedalboard([
    Compressor(threshold_db=-50, ratio=25),
    Gain(gain_db=30),
    Chorus(),
    LadderFilter(mode=LadderFilter.Mode.HPF12, cutoff_hz=900),
    Phaser(),
    Reverb(room_size=0.25),
], sample_rate=sample_rate)

# Pedalboard objects behave like lists, so you can add plugins:
board.append(Compressor(threshold_db=-25, ratio=10))
board.append(Gain(gain_db=10))
board.append(Limiter())

# Run the audio through this pedalboard!
effected = board(audio)

# Write the audio back as a wav file:
with sf.SoundFile('./processed_just_what_is_it_p.wav', 'w', samplerate=sample_rate, channels=len(effected.shape)) as f:
    f.write(effected)