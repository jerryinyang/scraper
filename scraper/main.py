import os
from dotenv import load_dotenv
import openai

# Load environment variables from .env file
load_dotenv()

# Get the OpenAI API key
api_key = os.getenv("OPENAI_API_KEY")

# Set the OpenAI API key
openai.api_key = api_key

# Now you can use the OpenAI API
response = openai.Completion.create(
    engine="text-davinci-003", prompt="Hello, world!", max_tokens=5, model="gpt-4o"
)

print(response.choices[0].text.strip())
