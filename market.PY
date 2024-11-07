from openai import OpenAI
from dotenv import load_dotenv
import os 

# Load environment variables
load_dotenv()

# Initialize OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Start a loop for continuous input
while True:
    # Prompt user to enter the YouTube channel topic or 'quit' to stop
    topic = input("Please enter the game and the guildline you want!\n")
    
    # Check if the user wants to exit
    if topic.lower() == 'quit':
        print("Exiting the program. Goodbye!")
        break
    
    # Stream the response from the model
    stream = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {   "role":"system",
                 "content":"you are a gamer who always post game guildline on internet"
            },
            {
                "role": "user",
                "content": topic
            }
        ],
        stream=True,
    )

    # Print the streamed response
    print("Generating ...")
    for chunk in stream:
        if chunk.choices[0].delta.content is not None:
            print(chunk.choices[0].delta.content, end="")
    print("\n")  # Add a newline after each response for better readability