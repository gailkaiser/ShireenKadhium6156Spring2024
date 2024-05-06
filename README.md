# HOWTO

How to use this code to summarize a PDF document:

1. Install the required libraries by running (use copy paste):
pip install openai PyMuPDF python-dotenv


2. Create a `.env` file in the project directory and add your OpenAI API key to it:
OPENAI_API_KEY=your_openai_api_key_here


3. Run the `summary_pdf.py` script with Python:
python summary_pdf.py



4. The generated summary will be saved in the `summary.txt` file.

Note: Make sure you have Python installed on your system.
