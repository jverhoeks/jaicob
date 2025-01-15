from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
from dotenv import load_dotenv
import os

load_dotenv()

SLACK_OAUTH_TOKEN = os.getenv('SLACK_OAUTH_TOKEN')


def main():
    
    # Your Slack OAuth token
    client = WebClient(token=SLACK_OAUTH_TOKEN)

    try:
        # Send a message in a channel as the authenticated user
        response = client.chat_postMessage(
            channel="C030YAPGQNQ",  # Replace with the channel ID
            text="Hello from the bot acting as me!",
            as_user=True  # Post as the authenticated user (you)
        )
        print("Message sent: ", response["message"]["text"])
    except SlackApiError as e:
        print(f"Error sending message: {e.response['error']}")
    
    
    
if __name__ == "__main__":
    main()