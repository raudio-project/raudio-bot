from dataclasses import dataclass
import json
import os


@dataclass
class RaudioConfig:
    authenticated: list[int]
    stream_url: str


def raudio_config_from_json(file_name) -> RaudioConfig:
    if os.path.exists(file_name):
        with open(file_name) as f:
            data = json.load(f)

        return RaudioConfig(**data)
