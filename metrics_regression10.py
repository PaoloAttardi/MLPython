from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

y = np.random.random(size=100) * 10
errors = 2 * (np.random.random(size=100)) - 1 # andiamo a valutare l'impatto di alcuni errori messi a caso
p = y + errors

mse = mean_squared_error(y, p)
mea = mean_absolute_error(y, p)
r2 = r2_score(y, p)

res = y - p # calcolo dei residui e li grafico
sns.scatterplot(x=y, y=res)
plt.show()