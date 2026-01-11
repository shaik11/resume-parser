# Resume Parser
This repository contains the code related resume parser.

## Clone Repository
```
git clone <repository URL>
cd resume-parser
``` 

## Create Virtual Environment (As per requirement)
```
python -m venv .venv
source .venv/bin/activate (MAC)
.venv\Scripts\activate (Windows)
```

## Install Dependencies
```
pip install pdfplumber python-docx
```
## Usage
```
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

result = framework.parse_resume("test-resume.pdf")
# OR
result = framework.parse_resume("test-resume.docx")

print(result.to_json())
```

## Run through Code
```
python main.py
```

## Sample Output
```
{
  "name": "XXXXX",
  "email": "xxxxx@gmail.com",
  "skills": [
    "Python",
    "AWS",
    "Docker",
    "Kubernetes"
  ]
}
```