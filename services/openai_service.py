import os

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()


MODEL_NAME = "google/gemini-2.5-flash-lite"

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY"),
    default_headers={
        "HTTP-Referer": "http://localhost:8501",
        "X-Title": "AI Resume Analyzer",
    },
)

import json
import re

from models.analysis_model import ResumeAnalysis


def analyze_resume(resume_text, job_description):

    prompt = f"""
You are an expert ATS recruiter.

Analyze the resume against the job description.

Return ONLY valid JSON.

Schema:

{{
    "ats_score": 0,
    "strengths": [],
    "weaknesses": [],
    "missing_skills": [],
    "suggestions": [],
    "professional_summary": ""
}}

Resume:
{resume_text}

Job Description:
{job_description}
"""

    try:

        response = client.chat.completions.create(
            model=MODEL_NAME,
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0
        )

        result = response.choices[0].message.content.strip()

        # Remove Markdown code fences if present
        result = re.sub(r"^```json\s*", "", result)
        result = re.sub(r"^```\s*", "", result)
        result = re.sub(r"\s*```$", "", result)

        data = json.loads(result)

        return ResumeAnalysis(**data)

    except json.JSONDecodeError as e:
        print("❌ JSON Decode Error")
        print(result)
        print(e)
        return None

    except Exception as e:
        print(f"❌ Unexpected Error: {e}")
        return None
    