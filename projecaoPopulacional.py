import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn
from sklearn.impute import SimpleImputer

regioes = pd.read_csv("projPopulacao.csv")
print(regioes.head())

latitude, longitude = regioes["latd"], regioes["longd"]
populacao, area = regioes["population_total"], regioes["area_total_km2"]

seaborn.set
plt.scatter(longitude, latitude, label=None, c=np.log10(populacao), cmap='viridis', s=area, linewidth=0, alpha=0.5)

def si():
    sip = SimpleImputer(missing_values=np.nan, strategy='mean')
    data = sip.fit_transform([[1, 2],
                             [np.nan, 3],
                             [7, 6]]
                            )
    print(data)
si()
plt.xlabel('Longitude')
plt.ylabel('Longitude')
plt.colorbar(label='log$_{10}$(populacao)')
plt.clim(3, 7)

for area in [100, 300, 500]:
    plt.scatter([], [], c='k', alpha=0.3, s=area, label=str(area) + 'km$^2$')

plt.legend(scatterpoints=1, frameon=False, labelspacing=1, title='Areas de cidades')
plt.title("Area e população das cidades do Estado da California-EUA")
plt.show()