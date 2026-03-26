from collections import Counter

import pandas as pd
from matplotlib import pyplot as plt

plt.style.use("fivethirtyeight")

data = pd.read_csv("data.csv")
ids = data["Responder_id"]
lang_responses = data["LanguagesWorkedWith"]

language_counter = Counter()

#  row = next(csv_reader)
#  print(row["LanguagesWorkedWith"].split(";"))

for response in lang_responses:
    language_counter.update(response.split(";"))

languages = []
popularity = []

#  print(language_counter)
for item in language_counter.most_common(15):
    languages.append(item[0])
    popularity.append(item[1])

languages.reverse()
popularity.reverse()

#  print(languages)
#  print(popularity)

#  plt.bar(languages, popularity)
plt.barh(languages, popularity)

plt.title("Most Popular Languages")
#  plt.xlabel("Programming Languages")
#  plt.ylabel("Number of People Who Use")

#  plt.ylabel("Programming Languages")
plt.xlabel("Number of People Who Use")

#  plt.legend()

plt.tight_layout()

plt.show()
