import pyshorteners

long_url = input("Enter the URL to shorten: ")

shorten_url = pyshorteners.Shortener()
short_url = shorten_url.tinyurl.short(long_url)

print("The shortened URL is: " + short_url)