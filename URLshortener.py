# Python URL Shortener
# Kevin Yeung

# Uses Cuttly API
# 1. Create and verify cuttly account.
# 2. Click on edit account in settings.
# 3. Select change api key and copy/paste here. (if invalid)
# 4. Enter target url and submit

import requests
from tkinter import *
import tkinter as tk

# Guest cuttly key
api_key = "acf982beaeabc9a1bea61079f4df5e41e433c"

# Gets target url and requests for shortened one via cuttly
def shortenURL():
    url = inputText.get()

    # Formats URL
    api_url = f"https://cutt.ly/api/api.php?key={api_key}&short={url}"

    # Make shortening request, if valid displays new link
    data = requests.get(api_url).json()["url"]

    if data["status"] == 7:
        shortened_url = data["shortLink"]
        print("Shortened URL:", shortened_url)
        textVar.set(shortened_url)
    else:
        print("[!] Error shortening URL:", data)
        textVar.set("Bad link, try again...")

# Tkinker init
root = tk.Tk()

# Set widget dimensions
root.geometry("500x100")
root.title('Link Shortener')

# Text labels on root stage
titleText = Label(root, text = "Copy/Paste your target link into the text box below.", width = 50,font = ("bold", 10))
titleText.place(x = 50, y = 5)

bodyText = Label(root, text = "Link: ", width = 20, font = ("bold", 10))
bodyText.place(x = 50, y = 30)

# Input textbox
inputText = Entry(root)
inputText.place(x = 150, y = 30)

# User submit button
submit = tk.Button(root, text = "Submit", command = shortenURL, bg = "black", fg = 'white').place(x = 325, y = 27)

# Variable text to update on link submission
textVar = tk.StringVar()
finalText = tk.Label(root, textvariable = textVar, width = 50, font = ("bold", 10)).place(x = 50, y = 65)
textVar.set("Shortened Link: ")

root.mainloop()
