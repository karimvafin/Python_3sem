import pandas as pd
from matplotlib import pyplot as plt

df = pd.read_csv("flights.csv")

df = df.drop(df.columns[0], axis=1)

CARGO = list(set(df.CARGO))
WEIGHT = []
PRICE = []
FLIGHTS = []

for comp in CARGO:
    WEIGHT.append(df.loc[df.CARGO == comp].WEIGHT.sum())
    PRICE.append(df.loc[df.CARGO == comp].PRICE.sum())
    FLIGHTS.append(df.loc[df.CARGO == comp].shape[0])

fig, ax = plt.subplots(1, 3)
plt.subplots_adjust(wspace=0.5)
fig.set_figwidth(10)

ax[0].bar(CARGO, WEIGHT, color='red')
ax[0].set_title('Weight')
ax[0].set_xlabel('Cargo')

ax[1].bar(CARGO, PRICE, color='orange')
ax[1].set_title('Price')
ax[1].set_xlabel('Cargo')

ax[2].bar(CARGO, FLIGHTS, color='green')
ax[2].set_title('Flights')
ax[2].set_xlabel('Cargo')

plt.savefig('episode2.png')
