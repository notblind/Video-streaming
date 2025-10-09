ACCEPTABLE_VIDEO_TYPES = (
    ("mp4", "video/mp4"),
    ("mov", "video/quicktime"),
    ("webm", "video/webm"),
)

ACCEPTABLE_VIDEO_FORMATS = [video_format for video_format, _ in ACCEPTABLE_VIDEO_TYPES]

ACCEPTABLE_CONTENT_TYPES = [content_type for _, content_type in ACCEPTABLE_VIDEO_TYPES]
