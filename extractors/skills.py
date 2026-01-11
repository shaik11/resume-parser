from extractors.base import FieldExtractor

class SkillsExtractor(FieldExtractor):
    def extract(self, text: str) -> list[str]:
        """
        Gemini API can be used here instead.
        """
        known_skills = [
            "Python", "Machine Learning", "Deep Learning",
            "LLM", "AWS", "Docker", "Kubernetes"
        ]
        return [skill for skill in known_skills if skill.lower() in text.lower()]