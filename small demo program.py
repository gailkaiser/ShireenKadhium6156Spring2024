import openai

# Set up your OpenAI API key
openai.api_key = 'sk-proj-VEddPZgz6J34XiUD6hHjT3BlbkFJFgjtDNbOgipEJ851onI5'

def summarize_article(article_text, max_tokens=100):
    # Define the prompt
    prompt = "Summarize the following news article:\n\n" + article_text + "\n\nSummary:"

    # Generate the summary using GPT
    response = openai.Completion.create(
      engine="text-davinci-003",
      prompt=prompt,
      max_tokens=max_tokens
    )

    # Extract the summary from the response
    summary = response.choices[0].text.strip()

    return summary

def main():
    # Example news article text
    article_text = """
    Insert your news article here.
    """

    # Summarize the article
    summary = summarize_article(article_text)

    # Print the summary
    print("Summary:", summary)

if __name__ == "__main__":
    main()
