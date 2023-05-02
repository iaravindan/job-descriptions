from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import openai

app = FastAPI()

templates = Jinja2Templates(directory="templates")

openai.api_key = "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"


@app.get("/", response_class=HTMLResponse)
async def get_form(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/generate_jd")
async def generate_jd(request: Request, role_type: str = Form(...), experience: str = Form(...)):
    jd_format = f"""
    Position:
    Overview:
    Functional Accountabilities:
    General Responsibilities:
    Leadership Responsibilities:
    Qualifications:
    Behavioral Competencies:
    """
    user_message = f"""Develop a job description for {role_type} with {experience} years of experience. Provide the output in the following format: :{jd_format}"""

    prompt = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": "You are a Human Resource administration expert for an Information Technology Services company",
            },
            {"role": "user", "content": user_message},
        ],
    )

    return {"generated_jd": prompt.choices[0].message.content}
