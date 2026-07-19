def compare_skills(resume_skills, jd_skills):

    resume = set(resume_skills)
    jd = set(jd_skills)

    matched = sorted(resume & jd)
    missing = sorted(jd - resume)

    return matched, missing