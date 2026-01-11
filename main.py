from extractors.name import NameExtractor
from extractors.email import EmailExtractor
from extractors.skills import SkillsExtractor
from coordinator.resume_extractor import ResumeExtractor
from framework.resume_parser_framework import ResumeParserFramework

extractors = {
    "name": NameExtractor(),
    "email": EmailExtractor(),
    "skills": SkillsExtractor()
}

framework = ResumeParserFramework(ResumeExtractor(extractors))
#For pdf file
result = framework.parse_resume("Shaik.pdf")
#For word file
#result = framework.parse_resume("Shaik.docx")

print(result.to_json())