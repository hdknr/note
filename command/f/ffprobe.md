# ffprobe

- [ffmpeg](ffmpeg.md)
- [ffprobe Documentation](https://www.ffmpeg.org/ffprobe.html)

## 例

~~~bash
$ ffprobe -v quiet -print_format json -show_format -show_streams ~/Downloads/Video/Blurred\ Bokeh\ Video.mp4
...
~~~

~~~json
{
    "streams": [
        {
            "index": 0,
            "codec_name": "h264",
            "codec_long_name": "H.264 / AVC / MPEG-4 AVC / MPEG-4 part 10",
            "profile": "High",
            "codec_type": "video",
            "codec_time_base": "1001/60000",
            "codec_tag_string": "avc1",
            "codec_tag": "0x31637661",
            "width": 1920,
            "height": 1080,
            "coded_width": 1920,
            "coded_height": 1088,
            "has_b_frames": 2,
            "sample_aspect_ratio": "1:1",
            "display_aspect_ratio": "16:9",
            "pix_fmt": "yuv420p",
            "level": 40,
            "color_range": "tv",
            "color_space": "bt709",
            "color_transfer": "bt709",
            "color_primaries": "bt709",
            "chroma_location": "left",
            "refs": 1,
            "is_avc": "true",
            "nal_length_size": "4",
            "r_frame_rate": "30000/1001",
            "avg_frame_rate": "30000/1001",
            "time_base": "1/30000",
            "start_pts": 0,
            "start_time": "0.000000",
            "duration_ts": 219219,
            "duration": "7.307300",
            "bit_rate": "4475901",
            "bits_per_raw_sample": "8",
            "nb_frames": "219",
            "disposition": {
                "default": 1,
                "dub": 0,
                "original": 0,
                "comment": 0,
                "lyrics": 0,
                "karaoke": 0,
                "forced": 0,
                "hearing_impaired": 0,
                "visual_impaired": 0,
                "clean_effects": 0,
                "attached_pic": 0,
                "timed_thumbnails": 0
            },
            "tags": {
                "creation_time": "2017-02-07T06:24:56.000000Z",
                "language": "und",
                "handler_name": "L-SMASH Video Handler",
                "encoder": "AVC Coding"
            }
        }
    ],
    "format": {
        "filename": "/Users/hide/Downloads/Video/Blurred Bokeh Video.mp4",
        "nb_streams": 1,
        "nb_programs": 0,
        "format_name": "mov,mp4,m4a,3gp,3g2,mj2",
        "format_long_name": "QuickTime / MOV",
        "start_time": "0.000000",
        "duration": "7.307300",
        "size": "4091272",
        "bit_rate": "4479106",
        "probe_score": 100,
        "tags": {
            "major_brand": "mp42",
            "minor_version": "0",
            "compatible_brands": "mp42mp41isomavc1",
            "creation_time": "2017-02-07T06:24:56.000000Z"
        }
    }
}
~~~