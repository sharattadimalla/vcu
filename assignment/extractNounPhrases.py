from textblob import TextBlob
from pattern.web import download, plaintext, PDF, URL

# Extracting noun phrases from a local file
path = '/Users/sharattadimalla/github/vcu/assignment/'
file_name = 'President_Obama_Speech_2004.txt'

with open(path+file_name, 'rU') as file:
    content = file.readlines()

blob = TextBlob(str(content))

print "Static Text Noun Phrases"
print blob.noun_phrases

# Extracting noun phrases from the web
weblink = 'http://www.americanrhetoric.com/speeches/convention2004/barackobama2004dnc.htm'
html = download(weblink)

blob1 = TextBlob(plaintext(html))

print "Web Page Content Noun Phrases"
print blob1.noun_phrases

# Extracting noun phrases from pdf document
url = URL('http://www.bellevue.edu/student-support/career-services/pdfs/resume-samples.pdf')
pdfcontent = PDF(url.download())

blob2 = TextBlob(pdfcontent)

print blob2.noun_phrases


