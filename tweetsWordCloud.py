from PIL import Image
from wordcloud import WordCloud, STOPWORDS
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import re
import random

def grey_color_func(word, font_size, position, orientation, random_state=None, **kwargs):
    return "hsl(0, 0%%, %d%%)" % random.randint(40, 80)

twitterdata = pd.read_csv("tweets.csv")
df = twitterdata["text"]

stopwords = set(STOPWORDS)
stopwords.add("RT")


_mask = np.array(Image.open("twitter.png"))
_edited = np.invert(_mask)

wc = WordCloud(background_color="white", max_words=2000,stopwords=stopwords, mask=_edited)

text = df.str.cat()
filtered = re.findall(r'(?:\b\w{4,}\b)', text)

text = ','.join(map(str, filtered))

wc.generate(text)
plt.imshow(wc.recolor(color_func=grey_color_func, random_state=3))
wc.to_file("myTweets.png")
plt.axis("off")
plt.figure()
plt.axis("off")
plt.show()
