from parsers.pdf_parser import PDFParser
from parsers.word_parser import WordParser
from coordinator.resume_extractor import ResumeExtractor

class ResumeParserFramework:
    def __init__(self, resume_extractor: ResumeExtractor):
        self.resume_extractor = resume_extractor

    def parse_resume(self, file_path: str):
        if file_path.endswith(".pdf"):
            parser = PDFParser()
        elif file_path.endswith(".docx"):
            parser = WordParser()
        else:
            raise ValueError("Unsupported file format")

        text = parser.parse(file_path)
        # print(text)
        return self.resume_extractor.extract(text)