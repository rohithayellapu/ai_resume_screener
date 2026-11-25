from skill_extractor import extract_skills

def get_missing_skills(resume_text, jd_text):
    resume_skills = extract_skills(resume_text)
    jd_skills = extract_skills(jd_text)

    missing_skills = []

    for skill in jd_skills:
        if skill not in resume_skills:
            missing_skills.append(skill)

    return missing_skills