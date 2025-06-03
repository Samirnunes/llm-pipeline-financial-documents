from typing import Dict, Self
import yaml
from pydantic import BaseModel

class Prompt(BaseModel):
    prompt: str
    
    @classmethod
    def from_yaml(cls, yaml_filepath: str) -> Self:
        with open(yaml_filepath, "r") as f:
            content = yaml.safe_load(f)
        return cls(**content)
    
    def format(self, content: Dict[str, str]) -> str:
        return self.prompt.format(**content)
