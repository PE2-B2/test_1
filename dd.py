import xml.etree.ElementTree as ET
import matplotlib.pyplot as plt
import numpy as np

# parsing xml file
tree = ET.parse('sample1.xml')

# IVMeasurement, Fig1
for IVM in tree.iter(tag='IVMeasurement'):
    for item in IVM.iter(tag='Voltage'):
        V = item.text.split(",")
        V_list = list(map(float, V))
    for item in IVM.iter(tag='Current'):
        C = item.text.split(",")
        C_list = list(map(float, C))

C_list1 = np.abs(C_list)

print(V_list)
print(C_list)


#Plot Fig1
plt.plot(V_list, C_list1, 'b', alpha=0.7)
plt.scatter(V_list, C_list1, c='r', alpha=1.0)
plt.title('IV-analysis')
plt.xlabel("Voltage", fontsize=12)
plt.xticks(fontsize=10)
plt.ylabel("Current", fontsize=12)
plt.yticks(fontsize=10)
plt.yscale('logit')
plt.grid(True)
plt.tight_layout()
plt.savefig('VC.png')
plt.show()