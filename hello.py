import os
from datetime import datetime

def main():
    # Read the name from the environment variable, defaulting if unavailable
    name = os.environ.get("WHO_TO_GREET", "Guest")
    
    # Print the required greetings
    print(f"Hello {name}!")
    print("This program is running inside GitHub Actions.")
    
    # Optional Challenge: Display the current date and time
    current_time = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")
    print(f"Current Date and Time: {current_time}")

if __name__ == "__main__":
    main()
