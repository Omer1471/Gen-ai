import os
from dotenv import load_dotenv
import requests

# Load environment variables from .env file
load_dotenv()

# Access the environment variable
api_key = os.getenv("OPENAI_API_KEY")

# Check if the API key is available
if api_key is None:
    raise ValueError("API key not found in environment variables")

def generate_image(prompt):
    api_url = 'https://api.openai.com/v1/images/generations'
    headers = {
        'Authorization': f'Bearer {api_key}',
        'Content-Type': 'application/json'
    }
    payload = {
        'prompt': prompt,
        'n': 1  # Number of images to generate
    }

    response = requests.post(api_url, json=payload, headers=headers)
    if response.status_code == 200:
        image_url = response.json()['data'][0]['url']
        return image_url
    else:
        print("Error:", response.status_code, response.text)

# Example usage
prompt = "A futuristic city skyline at sunset"
image_url = generate_image(prompt)
print("Generated Image URL:", image_url)

