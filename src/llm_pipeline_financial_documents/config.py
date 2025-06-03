import os


def configure() -> None:
    os.environ['LM_STUDIO_API_BASE'] = "http://127.0.0.1:1234/v1"
    os.environ['LM_STUDIO_API_KEY'] = "sk-12345"