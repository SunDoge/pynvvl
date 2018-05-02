#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pynvvl

loader = pynvvl.NVVLVideoLoader(device_id=0)

n_frames = loader.frame_count('examples/sample.mp4')

print(n_frames)

video = loader.read_sequence('examples/sample.mp4')

print(video.shape)

print(video.dtype)

import matplotlib.pyploy as plt

frame = video[0].get().transpose(1, 2, 0)
plt.imshow(frame)
plt.savefig('test.png')
