import webbrowser

keywords = [
    'catan',
    'fender',
    'artificial intelligence'
]

for keyword in keywords:
    url = "https://www.google.com/search?q={}".format(keyword)
    webbrowser.open_new(url)