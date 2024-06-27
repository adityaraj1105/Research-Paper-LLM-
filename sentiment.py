from textblob import TextBlob

text = "My modem has been offline for a week now... God bless the 3g network. Tim just left... Again!! May schedule has been brutal"

blob = TextBlob(text)
polarity_score = blob.sentiment.polarity

print("Polarity Score:", polarity_score)
