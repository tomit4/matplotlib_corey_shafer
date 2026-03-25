from matplotlib import pyplot as plt

#  print(plt.style.available) # comment out plt.show() when using
plt.style.use("fivethirtyeight")

ages_x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]

dev_y = [38496, 52000, 46752, 49320, 53200, 56000, 62316, 64928, 67317, 68748, 73752]

py_dev_y = [45372, 48876, 53850, 57287, 63016, 65998, 70003, 40000, 71496, 75370, 83640]

js_dev_y = [37810, 43515, 46823, 49293, 53437, 56373, 62375, 66674, 68745, 68746, 74583]


plt.plot(ages_x, py_dev_y, color="#5a7d9a", marker="o", linewidth=3, label="Python")

plt.plot(ages_x, js_dev_y, color="#adad3b", marker="o", linewidth=3, label="JavaScript")

plt.plot(ages_x, dev_y, color="#444444", linestyle="--", marker=".", label="All Devs")

plt.xlabel("Ages")
plt.ylabel("Median Salary (USD)")
plt.title("Median Salary (USD) by Age")

# plt.legend(["All Devs", "Python"])
plt.legend()

plt.grid(True)
plt.tight_layout()

plt.savefig("plot.png")
plt.show()
