import os
import sys
from commands import execute_command

def main():
    print(" Welcome to Python Command Terminal")
    print("Type 'exit' to quit.\n")

    while True:
        try:
            command = input("py-terminal $ ").strip()
            if command.lower() == "exit":
                print("Exiting terminal... ")
                break
            if command:
                execute_command(command)
        except KeyboardInterrupt:
            print("\nKeyboardInterrupt detected. Type 'exit' to quit.")
        except Exception as e:
            print(f" Error: {e}")

if __name__ == "__main__":
    main()
