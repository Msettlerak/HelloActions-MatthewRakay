import os
from datetime import datetime, timezone

def main():
    # Read the name from the environment variable, defaulting if unavailable
    name = os.environ.get("WHO_TO_GREET", "Guest")
    
    # Print the required greetings
    print(f"Hello {name}!")
    print("This program is running inside GitHub Actions.")
    
    # Updated Challenge: Display the current date and time without deprecation warnings
    current_time = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
    print(f"Current Date and Time: {current_time}")

if __name__ == "__main__":
    main()
