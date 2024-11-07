from enum import IntEnum
from config import MKV_FOLDER, OGV_FOLDER, MP4_FOLDER, AVI_FOLDER, WEBM_FOLDER


class Formats(IntEnum):
    """Formats of audio: mkv = 0, ogv = 1, mp4 = 2, avi = 3, webm = 4"""
    MKV = 0
    OGV = 1
    MP4 = 2
    AVI = 3
    WEBM = 4
    

# Linked constants
FOLDERS: tuple[str, ...] = MKV_FOLDER, OGV_FOLDER, MP4_FOLDER, AVI_FOLDER, WEBM_FOLDER
FORMATS: tuple[str, ...] = 'mkv', 'ogv', 'mp4', 'avi', 'webm'
CODECS: tuple[str, ...] = 'libx264', 'libtheora', 'libx264', 'rawvideo', 'libvpx'