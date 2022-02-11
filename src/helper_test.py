# Test de las funciones helper MV
import helper
dist={'A':0.50,'B':0.25,'C':0.125, 'D':0.125}
tree = helper.huffman(dist)
print(tree)

# Segunda parte del test
from matplotlib import pyplot as plt
import numpy as np
pregs=6
aux=dist.copy()
acl_list=list()
entropy_list=list()
for idx in range(1,pregs):
    tree=helper.huffman(aux)
    acl=0
    for key,value in tree.items():
        acl += len(value)*aux[key]/len(key) # El ACL es bits/caracter por eso divido por el len
    acl=np.around(acl,decimals=2)
    print("Average code length: {}".format(acl))
    key=list(aux.keys())[0]
    print("Entropy per symbol: {}".format(helper.entropy(aux)/len(key)))
    acl_list.append(acl)
    entropy_list.append(helper.entropy(dist))
    aux=helper.combine(aux,dist)
plt.plot(range(1,pregs),acl_list)
plt.scatter(range(1,pregs),acl_list)
plt.plot(range(1,pregs),entropy_list)
plt.show()