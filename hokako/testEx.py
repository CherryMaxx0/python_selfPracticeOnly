
from datetime import date
import time

# ANSI escape codes for colors
GREEN = "\033[92m"
CYAN = "\033[96m"
YELLOW = "\033[93m"
RESET = "\033[0m"

def happy_birthday(name):
    print(GREEN + f"🎂 Happy Birthday, {name}! 🎂" + RESET)
    time.sleep(1)
    print(CYAN + "Wishing you a bug-free life and an infinite loop of happiness 💻💙" + RESET)
    time.sleep(1.5)
    print(YELLOW + "May your code always compile and your dreams always execute successfully!" + RESET)
    time.sleep(2)
    print()
    print(GREEN + "Arik, you're not just my best friend, you're the best sove brother." + RESET)
    time.sleep(1.5)
    print(CYAN + "May your life run smoother than Python, faster than C, and cooler than JavaScript 🚀💙" + RESET)

if __name__ == "__main__":
    today = date.today()
    if today.day == 21 and today.month == 9:
        happy_birthday("Arik")
    else:
        print("Waiting for Arik's birthday...")