import urllib

url = "https://www.linkedin.com/"

content = urllib.urlopen(url)

print content.read()