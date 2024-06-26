import openai
import time

# Set up the OpenAI API client
openai.api_key = "YOUR_API_KEY_HERE"

# Define the Chatbot class
class Chatbot:
    def __init__(self, id, name, api_key):
        self.id = id
        self.name = name
        self.conversation_history = ""
        self.active = False
        self.api_key = api_key

    def generate_response(self, user_input):
        # Get the conversation history for this chatbot
        history = self.conversation_history

        # Concatenate the user input and conversation history into a prompt
        prompt = history + user_input

        # Set up the OpenAI API client for this chatbot's API key
        openai.api_key = self.api_key

        # Generate a response from the OpenAI API
        completions = openai.Completion.create(
            engine="davinci",
            prompt=prompt,
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.7,
        )

        # Extract the response from the API output
        message = completions.choices[0].text.strip()

        # Store the conversation history for this chatbot
        self.conversation_history = prompt + message

        return message

# Create six instances of Chatbot
chatbots = [
    Chatbot("chatbot1", "Alice", "API_KEY_1_HERE"),
    Chatbot("chatbot2", "Bob", "API_KEY_2_HERE"),
    Chatbot("chatbot3", "Charlie", "API_KEY_3_HERE"),
    Chatbot("chatbot4", "David", "API_KEY_4_HERE"),
    Chatbot("chatbot5", "Eve", "API_KEY_5_HERE"),
    Chatbot("chatbot6", "Frank", "API_KEY_6_HERE"),
]

# Set the first chatbot to be active by default
chatbots[0].active = True

# Example usage when user clicks on a chatbot to use
def activate_chatbot(chatbot_id):
    # Set all chatbots to inactive
    for chatbot in chatbots:
        chatbot.active = False
        
    # Set the clicked chatbot to active
    active_chatbot = next(chatbot for chatbot in chatbots if chatbot.id == chatbot_id)
    active_chatbot.active = True

# Example usage when user sends a message to the active chatbot
def send_message(user_input):
    # Get the active chatbot
    active_chatbot = next(chatbot for chatbot in chatbots if chatbot.active)
    
    # Generate a response from the active chatbot
    response = active_chatbot.generate_response(user_input)
    
    return response

# Uncomment this code and replace the API keys with your own
# if you want to use the openai_secret_manager to retrieve your API keys which you 100% do.
"""
import openai_secret_manager

# Set up the OpenAI API clients for each chatbot
for chatbot in chatbots:
    chatbot.api_key = openai_secret_manager.get_secret("openai")["api_key"]
"""
