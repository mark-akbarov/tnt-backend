import requests

# Replace 'YOUR_API_TOKEN' with your actual Telegram bot API token
api_token = 'YOUR_API_TOKEN'
api_url = f'https://api.telegram.org/bot6679449901:AAFLyALftzJ_ichNLWu0AON3vSRqqOWTw30/'

# Function to get the latest updates from the bot
def get_updates():
    response = requests.get(api_url + 'getUpdates')
    data = response.json()
    return data['result']

# Function to get the chat ID of the group
def get_group_chat_id():
    updates = get_updates()
    if updates:
        chat = updates[0]['message']['chat']
        chat_id = chat['id']
        return chat_id
    return None

if __name__ == '__main__':
    group_chat_id = get_group_chat_id()
    if group_chat_id:
        print(f"The chat ID of the group is: {group_chat_id}")
    else:
        print("No updates found. Make sure your bot is added to the group and someone has sent a message.")
