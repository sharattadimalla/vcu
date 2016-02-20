from pattern.web import Twitter # import required to search Twitter
from textblob import TextBlob # import textblob to extract noun phrases

t = Twitter()
i = None
noun_phrase_list = ()
senti_list = []
for j in range(3):
    for tweet in t.search('snagajob', start=i, count=100):
        blob = TextBlob(tweet.text)
        noun_phrase_list+=(blob.sentiment, blob.noun_phrases, tweet.text)

print "##################################"
print "Extracted Noun Phrases"
print len(noun_phrase_list)
for row in noun_phrase_list:
    print row
    print "\n"

