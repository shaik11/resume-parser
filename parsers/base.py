from abc import ABC, abstractmethod

class FileParser(ABC):
    @abstractmethod
    def parse(self, file_path: str) -> str:
        """Extract raw text from a resume file"""
        pass