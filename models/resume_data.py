from dataclasses import dataclass, asdict
from typing import List, Optional
import json

@dataclass
class ResumeData:
    name: Optional[str]
    email: Optional[str]
    skills: List[str]

    def to_dict(self) -> dict:
        return asdict(self)

    def to_json(self, indent: int = 2) -> str:
        return json.dumps(self.to_dict(), indent=indent)