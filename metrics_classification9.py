import numpy as np
import scikitplot as skplt
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, classification_report
import matplotlib.pyplot as plt

# funzione per generare dei valori casuali, nell'80% dei casi copia l'elemento così com'è nel 20% lo sostituisce con uno casuale
def randomize(v, lab, prob=0.2):
    v2 = []
    for el in v:
        if np.random.random() > prob: # random.random estrae un valore a caso tra 0 e 1
            v2.append(el)
        else:
            v2.append(np.random.choice(lab))
    return v2

labels = ['cronaca', 'politica', 'sport']
y = np.random.choice(labels, 1000)

p = randomize(y, labels) # così p è per l'80% simile a y e per il 20% diverso, misuriamo ora l'accuratezza

cla = classification_report(y, p) # il classification esegue tutte le classificazione viste nell'import
print(cla)

skplt.metrics.plot_confusion_matrix(y, p)
plt.show()