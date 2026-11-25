import spacy

# Load spaCy English model
nlp = spacy.load("en_core_web_sm")

# Skills list
skills = [
    "python",
    "java",
    "c",
    "c++",
    "sql",
    "html",
    "css",
    "javascript",
    "react",
    "node.js",
    "mongodb",
    "machine learning",
    "deep learning",
    "data analysis",
    "git",
    "docker",
    "aws"
]

def extract_skills(text):
    text = text.lower()

    found_skills = []

    for skill in skills:
        if skill.lower() in text:
            found_skills.append(skill)

    return found_skills