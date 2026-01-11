import re
from extractors.base import FieldExtractor

class EmailExtractor(FieldExtractor):
    def extract(self, text: str) -> str | None:
        match = re.search(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", text)
        return match.group(0) if match else None