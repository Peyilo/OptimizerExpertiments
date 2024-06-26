import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


data_folder = '../../data/exp_weight_decay_gradient_norm/'
lr = 0.001
# LR=0.001
data_files = {
    "AdamW WD=1e-3": "VGG16WithoutBN_AdamW_LR0.001_WD0.001.csv",
    "AdamW WD=5e-4": "VGG16WithoutBN_AdamW_LR0.001_WD0.0005.csv",
    "AdamW WD=1e-4": "VGG16WithoutBN_AdamW_LR0.001_WD0.0001.csv",
    "AdamW WD=0": "VGG16WithoutBN_AdamW_LR0.001_WD0.csv"
}

colors = {
    "AdamW WD=0": "orange",
    "AdamW WD=1e-3": "red",
    "AdamW WD=1e-4": "green",
    "AdamW WD=5e-4": "blue"
}

gradient_norm, squared_gradient_norm = {}, {}
for n_item, file in data_files.items():
    reader = pd.read_csv(data_folder + file)
    data = np.array(reader.values.tolist())
    gradient_norm[n_item] = data[:, 4]
    squared_gradient_norm[n_item] = data[:, 5]

epochs = range(1, 200 + 1)

plt.rcParams['figure.figsize'] = (10, 8.0)
plt.rcParams['image.cmap'] = 'gray'
axes = plt.gca()
axes.set_ylim([0, 200])
axes.set_xlim([0, 200])
for n_item, data in gradient_norm.items():
    plt.plot(epochs, data, label=n_item, color=colors[n_item])
plt.grid()
plt.xlabel("Epochs")
plt.ylabel("Gradient Norm")
plt.title(f'VGG16WithoutBN With AdamW On CIFAR10, lr={lr}')
plt.legend()
plt.show()


plt.subplot()
axes = plt.gca()
axes.set_ylim([0, 8000])
axes.set_xlim([0, 200])
for n_item, data in squared_gradient_norm.items():
    plt.plot(epochs, data, label=n_item,  color=colors[n_item])
plt.grid()
plt.title(f'VGG16WithoutBN With AdamW On CIFAR10, lr={lr}')
plt.xlabel("Epochs")
plt.ylabel("Squared gradient Norm")
plt.legend()
plt.show()

# LR=0.001
data_files = {
    "AdamW WD=1e-3": "VGG16WithBN_AdamW_LR0.001_WD0.001.csv",
    "AdamW WD=5e-4": "VGG16WithBN_AdamW_LR0.001_WD0.0005.csv",
    "AdamW WD=1e-4": "VGG16WithBN_AdamW_LR0.001_WD0.0001.csv",
    "AdamW WD=0": "VGG16WithBN_AdamW_LR0.001_WD0.csv"
}

gradient_norm, squared_gradient_norm = {}, {}
for n_item, file in data_files.items():
    reader = pd.read_csv(data_folder + file)
    data = np.array(reader.values.tolist())
    gradient_norm[n_item] = data[:, 4]
    squared_gradient_norm[n_item] = data[:, 5]

plt.subplot()
axes = plt.gca()
axes.set_ylim([0, 70])
axes.set_xlim([0, 200])
for n_item, data in gradient_norm.items():
    plt.plot(epochs, data, label=n_item, color=colors[n_item])
plt.grid()
plt.xlabel("Epochs")
plt.ylabel("Gradient Norm")
plt.title(f'VGG16WithBN With AdamW On CIFAR10, lr={lr}')
plt.legend()
plt.show()


plt.subplot()
axes = plt.gca()
axes.set_ylim([0, 350])
axes.set_xlim([0, 200])
for n_item, data in squared_gradient_norm.items():
    plt.plot(epochs, data, label=n_item,  color=colors[n_item])
plt.grid()
plt.title(f'VGG16WithBN With AdamW On CIFAR10, lr={lr}')
plt.xlabel("Epochs")
plt.ylabel("Squared gradient Norm")
plt.legend()
plt.show()
