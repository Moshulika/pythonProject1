import pandas as pd
from matplotlib import pyplot as plt

fig, axs = plt.subplots(3)
fig.suptitle('Grafice')

columns = ["Durata", "Puls", "MaxPuls", "Calorii"]
df = pd.read_csv("data.csv") #Se

#Scriem in consola fisierul pentru a vedea ca citeste corect
print("Contents in csv file:", df)

axs[0] = df[['Calorii', 'Durata', 'Puls', 'MaxPuls']].plot()
axs[1] = df[['Calorii', 'Durata', 'Puls', 'MaxPuls']].head(7).plot()
axs[2] = df[['Durata', 'Puls']].tail(12).plot()

plt.show()
