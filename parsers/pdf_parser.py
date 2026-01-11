import pdfplumber
from parsers.base import FileParser

class PDFParser(FileParser):
    """
    Extracts text from PDF file resumes using pdfplumber.
    """

    def parse(self, file_path: str) -> str:
        extracted_text = []

        try:
            with pdfplumber.open(file_path) as pdf:
                for page_number, page in enumerate(pdf.pages, start=1):
                    text = page.extract_text()
                    if text:
                        extracted_text.append(text)
        except Exception as exc:
            raise RuntimeError(f"Failed to parse PDF file: {exc}") from exc

        return "\n".join(extracted_text)