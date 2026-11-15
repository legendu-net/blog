---
title: Tips on FFmpeg
created: '2013-09-06T15:19:20-07:00'
date: '2026-11-15T09:14:59-08:00'
authors:
  - bendu
label: tips-on-ffmpeg
license: CC-BY-4.0
tags:
  - programming
  - multimedia
  - Linux
  - video
  - audio
  - image
  - FFmpeg
---

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

It is suggested that you use
[OpenCV for Python](https://github.com/skvark/opencv-python)
and
[moviepy](https://github.com/Zulko/moviepy)
(instead of [FFmpeg](https://ffmpeg.org/))
to manipulate multimedia.

1. extract audio from video

1. convert between different formats of audios

## Record Screen

The command below record screen into a MP4 video named `out.mp4` in Linux.

```
:::bash
ffmpeg -f x11grab -r 25 -s cif -i :0.0 $(date +%m%d%H%M%S).mp4
```

The command below record screen into a MP4 video named `out.mp4` in macOS.

```
:::bash
ffmpeg -f avfoundation -i "1" -pix_fmt yuv420p -r 25 $(date +%m%d%H%M%S).mp4
```

## Convert Video Files

Convert a MOV video file to a MP4 video file.

```
ffmpeg -i my-video.mov -vcodec h264 -acodec mp2 my-video.mp4
```

## References

- https://ffmpeg.org/

- [Capturing your Desktop / Screen Recording](https://trac.ffmpeg.org/wiki/Capture/Desktop)

- [How to record the desktop with FFmpeg on Linux](https://www.internalpointers.com/post/record-desktop-ffmpeg-linux)

- [Capture Windows screen with ffmpeg](https://stackoverflow.com/questions/6766333/capture-windows-screen-with-ffmpeg)

- [How to create a video from images with FFmpeg?](https://stackoverflow.com/questions/24961127/how-to-create-a-video-from-images-with-ffmpeg)

- [Convert video to images with FFmpeg in Linux](https://averagelinuxuser.com/convert-video-to-images-with-ffmpeg-in-linux/)

- https://www.labnol.org/internet/useful-ffmpeg-commands/28490/

- https://catswhocode.com/ffmpeg-commands/

- https://opensource.com/article/17/6/ffmpeg-convert-media-file-formats

- https://www.ostechnix.com/20-ffmpeg-commands-beginners/

- https://averagelinuxuser.com/convert-video-to-images-with-ffmpeg-in-linux/
