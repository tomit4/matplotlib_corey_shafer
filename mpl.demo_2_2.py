import csv
from collections import Counter

import numpy as np
from matplotlib import pyplot as plt

plt.style.use("fivethirtyeight")

with open("data.csv") as csv_file:
    csv_reader = csv.DictReader(csv_file)

    language_counter = Counter()

    #  row = next(csv_reader)
    #  print(row["LanguagesWorkedWith"].split(";"))

    for row in csv_reader:
        language_counter.update(row["LanguagesWorkedWith"].split(";"))

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
