import openai
import fitz
import os
import pandas as pd
from dotenv import load_dotenv

filepath = "./2020.acl-demos.30.pdf"
# Load API key from .env file
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0, # this is the degree of randomness of the model's output
    )
    return response.choices[0].message["content"]


# Read the entire PDF document
text = ''
with fitz.open(filepath) as pdf_file:
    for page_num in range(len(pdf_file)):
        page = pdf_file.load_page(page_num)
        text += page.get_text()

# Generate a summary
prompt = f"""
Your task is to summarize the following text into a 500-word summary:

{text}
"""
summary = get_completion(prompt)

# Write the summary to a text file
with open('summary.txt', 'w') as out:
    out.write(summary)
    main()
