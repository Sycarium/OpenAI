import openai
import requests

# Set up the OpenAI API client with your API key
openai.api_key = "zWqA5Y1vdAlW1tt01cvPT3BlbkFJBFVnu1BL9afxrUoAv7t4"

# Make a request to the API using the models list endpoint
response = requests.get("https://api.openai.com/v1/models", headers={"Authorization": f"Bearer {openai.api_key}"})

# Check if the request was successful
if response.status_code == 200:
    print("API key is valid")
else:
    print("API key is invalid")