import pyshorteners

def shortening():
    url = input("Digit the url you want to make shorter:")
    shortened_url = pyshorteners.Shortener().tinyurl.short(url)
    print(shortened_url)


shortening()
