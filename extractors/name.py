from extractors.base import FieldExtractor

class NameExtractor(FieldExtractor):
    def extract(self, text: str) -> str | None:
        lines = text.splitlines()
        return lines[0].strip() if lines else None