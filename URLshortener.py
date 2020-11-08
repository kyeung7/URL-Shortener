# Python URL Shortener
# Kevin Yeung
# November 7, 2020

# Uses Cuttly API
# 1. Create and verify cuttly account.
# 2. Click on edit account in settings.
# 3. Select change api key and copy/paste here. (if invalid)
# 4. Enter target url and submit

# May need to install requests and tkinter modules
import requests
from tkinter import *
import tkinter as tk

# Your cuttly api key here
api_key = "acf982beaeabc9a1bea61079f4df5e41e433c"

def shortenURL():
    
    # Target url to shorten, get from user textbox input
    url = inputText.get()

    # Format of name in the URL
    api_url = f"https://cutt.ly/api/api.php?key={api_key}&short={url}"

    # Make shortening request
    data = requests.get(api_url).json()["url"]

    # If valid get shortened URL
    if data["status"] == 7:
        shortened_url = data["shortLink"]
        print("Shortened URL:", shortened_url)
        textVar.set(shortened_url)
    else:
        print("[!] Error shortening URL:", data)
        textVar.set("Bad link, try again...")

# Create tkinker stage
root = tk.Tk()

# Set widget dimensions
root.geometry("500x100")

# Sets title on form
root.title('Link Shortener')

# Creates and places text labels on root stage
titleText = Label(root, text = "Copy/Paste your target link into the text box below.", width = 50,font = ("bold", 10))
titleText.place(x = 50, y = 5)

bodyText = Label(root, text = "Link: ", width = 20, font = ("bold", 10))
bodyText.place(x = 50, y = 30)

# Positions textbox for user inputs
inputText = Entry(root)
inputText.place(x = 150, y = 30)

# Create/Position submit button, on click runs shortenURL method
submit = tk.Button(root, text = "Submit", command = shortenURL, bg = "black", fg = 'white').place(x = 325, y = 27)

# Creates variable text to update on link submission
textVar = tk.StringVar()
finalText = tk.Label(root, textvariable = textVar, width = 50, font = ("bold", 10)).place(x = 50, y = 65)
textVar.set("Shortened Link: ")

# Run tkinter instance
root.mainloop()







