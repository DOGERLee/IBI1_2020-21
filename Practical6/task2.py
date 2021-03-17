gene_lengths = [9410,394141,4442,105338,19149,76779,126550,36296,842,15981]
exon_counts = [51,1142,42,216,25,650,32533,57,1,523]

import numpy as np 
import matplotlib.pyplot as plt

A = np.array(gene_lengths)
B = np.array(exon_counts)
L = A/B

sorted(L)
L = sorted(L)
L.sort()
print(L)

plt.boxplot(L,
            vert = True,
            whis= 1.5,
            patch_artist= True,
            meanline= False,
            showbox= True,
            showcaps= True,
            showfliers= True,
            notch = False
            )
plt.show()

