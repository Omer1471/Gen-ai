from pathlib import Path
import openai
import os

# Set your API key from an environment variable
api_key = os.environ.get("OPENAI_API_KEY")
if api_key is None:
    raise ValueError("API key not found in environment variables")

# Set the API key
openai.api_key = api_key

# Define the output file path
speech_file_path = Path(__file__).parent / "speech.mp3"

# Make the API request
response = openai.audio.speech.create(
  model="tts-1",
  voice="alloy",
  input="The quick brown fox jumped over the lazy dog."
)

# Save the audio file
response.stream_to_file(speech_file_path)

