import pandas as pd
from matplotlib import pyplot as plt

# Initializam graficele
fig, axs = plt.subplots(3)

columns = ["Durata", "Puls", "MaxPuls", "Calorii"]  # Setam coloanele
df = pd.read_csv("data.csv")  # Se citeste fisierul

# Scriem in consola fisierul pentru a vedea ca citeste corect
print("Contents in csv file:", df)

# Cream graficele
axs[0] = df[['Calorii', 'Durata', 'Puls', 'MaxPuls']].plot()
axs[1] = df[['Calorii', 'Durata', 'Puls', 'MaxPuls']].head(7).plot()
axs[2] = df[['Durata', 'Puls']].tail(12).plot()

# Se arata graficul
plt.show()
