from typing import Any
import os
from moviepy.editor import VideoFileClip
from enumerations import Formats, FORMATS, FOLDERS, CODECS


class VideoConverter:
    def __init__(self) -> None:
        self.inp: int = Formats.MKV
        self.out: int = Formats.MP4
    
    def convert(self) -> None:
        if self.inp == self.out:
            return
        inp_folder: str = FOLDERS[self.inp]
        out_folder: str = FOLDERS[self.out]
        for file in os.listdir(inp_folder):
            if not file.endswith(FORMATS[self.inp]):
                continue
            out: str = file.replace(FORMATS[self.inp], FORMATS[self.out])
            out_file: str = f'{out_folder}/{out}'
            inp_file: str = f'{inp_folder}/{file}'
            cdec: str = CODECS[self.out]
            source: VideoFileClip = VideoFileClip(inp_file)
            source.write_videofile(out_file, codec=cdec)
