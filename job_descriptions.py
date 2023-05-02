import openai

openai.api_key="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"

#Get user input for the type of role
role_type=input("Enter the position name: \n")
experience=input("Enter the years of experience: \n")
jd_format=f"""
Position:
Overview:
Functional Accountabilities:
General Responsibilities:
Leadership Responsibilities:
Qualifications:
Behavioral Competencies:
"""
user_message=f""""Develop a job description for {role_type} with {experience} years of experience. Provide the output in the following format: :{jd_format}"""

prompt=openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[{"role":"system","content":"You are a Human Resource administration expert for an Information Technology Services company",
              "role":"user","content":user_message}]
)

print(prompt.choices[0].message.content)