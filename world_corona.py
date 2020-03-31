from matplotlib import pyplot as plt
from matplotlib.pyplot import figure as fg
fg(num=None, figsize=(10, 8))
import numpy as np
import pandas as pd

date_br = ()
date_it = ()
date_eua = ()

cases_br = ()
cases_it = ()
cases_eua = ()

max_view = 180000

data_br = pd.read_csv('data_brazil.csv')
date_br = data_br['date']
cases_br = data_br['cases']

data_it = pd.read_csv('data_italy.csv')
date_it = data_it['date']
cases_it = data_it['cases']

data_eua = pd.read_csv('data_eua.csv')
date_eua = data_eua['date']
cases_eua = data_eua['cases']

plt.plot(date_br, cases_br, 'k', label="")
plt.plot(date_br, cases_br, 'ro', label="Casos no Brasil")
plt.plot(date_it, cases_it, 'k', label="")
plt.plot(date_it, cases_it, 'bo', label="Casos na Itália")
plt.plot(date_eua, cases_eua, 'k', label="")
plt.plot(date_eua, cases_eua, 'go', label="Casos nos EUA")

plt.legend(prop={"size":15})
plt.xticks(rotation=45, fontsize=10)

ylabel = np.arange(0,max_view,5000)
plt.yticks(ylabel)

ax = plt.gca()
ax.set_ylim([1,max_view])
axes = plt.axes()
axes.yaxis.grid()

plt.title("Avanço do Coronavirus no Mundo")
#plt.show()
plt.savefig('coronavirus_mundo.jpg', dpi=80)
plt.savefig('coronavirus_mundo.pdf')