import matplotlib.pyplot as plt

x = [year for year in range(1975, 2016, 5)]
y = [1243, 1543, 1619, 1831, 1960, 2310, 2415, 2270, 1918]

plt.plot(x, y)
plt.show(block=True)
