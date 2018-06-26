# Program to find jokes from the web
# Accept the word from user and find jokes on that word on web
from random import choice
import requests
from pyfiglet import figlet_format
from termcolor import colored

text = "JOKE BUDDY"
text = figlet_format(text)
print(colored(text, color="green"))

user_term = input("Enter a word you want the joke for: ")
url = "https://www.icanhazdadjoke.com/search"
response = requests.get(url, headers={
                        "Accept": "application/json"}, params={"term": user_term, "limit": 20})

data = response.json()
total_j = data["total_jokes"]
print("There are {} jokes available for {} ".format(total_j, user_term))
data = data["results"]

if data:
    q_input = "con"
    lst = []
    inc = 1
    count = 1
    while q_input != "quit":
        pass
        for d in data:
            lst.append(d["joke"])
        colour = choice(["red", "blue", "cyan", "green", "magenta"])
        joke = colored("JOKE", color=colour)
        inc = colored(str(inc), color=colour)
        print(joke, inc,":", choice(lst))
        q_input = input("\nEnter quit to exit and next for next joke: ").lower()
        count += 1
        inc = count
else:
    print("We could'nt find joke for {}!.Sorry ".format(user_term))
