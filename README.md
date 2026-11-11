# HelloActions-MatthewRakay
basic hello program

37. Repository URL: https://github.com/Msettlerak/HelloActions-MatthewRakay
38. Source-code file: Hello.py
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
39. Workflow fileL: hello.yml
name: Hello World with Python

on:
  push:
    branches:
      - main
  workflow_dispatch:

jobs:
  hello-python:
    name: Run the Python Hello World program
    runs-on: ubuntu-latest

    steps:
      - name: Check out the repository
        uses: actions/checkout@v4

      - name: Run the Python program
        env:
          WHO_TO_GREET: 'GitHub Actions Student'
        run: python hello.py
40. Screenshot of a successful automatic run: <img width="1324" height="344" alt="image" src="https://github.com/user-attachments/assets/7f535a47-5305-422f-97a7-e60df2d5bcfc" />

41. Screenshot of a successful manual run:<img width="1373" height="348" alt="image" src="https://github.com/user-attachments/assets/d12d97ea-fec8-4bc7-b809-6e2425a2fb89" />
<img width="1859" height="697" alt="image" src="https://github.com/user-attachments/assets/b37cdac2-7525-4963-a3bd-4342cc350050" />

42. Screenshot showing the program output: <img width="1542" height="250" alt="image" src="https://github.com/user-attachments/assets/4828c9dd-dfb8-4302-9c41-c23a102767f9" />

43. README.md.
44. # HelloActions-MatthewRakay

basic hello program

45. Short explanation of the workflow.
  This GitHub Actions workflow automates the process of running our Python script inside a clean cloud environment. It is configured to run automatically whenever new code is pushed to the main branch, or manually when triggered through the GitHub Actions web interface using workflow_dispatch. 
46. A statement explaining whether AI was used:
    AI was used to help with any coding errors and to set up formatting templates. Ai was also used to find the specfic locations for screenshot of work completed.
