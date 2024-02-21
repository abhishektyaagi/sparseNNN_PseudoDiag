import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import pdb
#from dataProcessing import read_diagonal_positions

def read_accuracies(file_path):
    max_acc_list = []
    i=0
    with open(file_path, 'r') as file:
        for line in file:
            print(i)
            try:
                accuracy = float(line.strip())
                if 0 <= accuracy <= 1:
                    max_acc_list.append(accuracy)
            except ValueError:
                pass  # Ignore lines that cannot be converted to float
            i = i+1
    return max_acc_list

def read_diagonal_positions(filename):
    layer1PosLists = []
    layer2PosLists = []
    layer3PosLists = []
    i = 0

    with open(filename, 'r') as file:
        while True:
            print(i)
            # Attempt to read the next four lines (one block)
            block = [next(file, '').strip() for _ in range(4)]
            # If the first line of the block is empty, we've reached the end
            if not block[0]:
                break
            
            # Combine and clean the lines for the first matrix (removing brackets and splitting)
            layer1Lines = block[0] + ' ' + block[1]
            layer1Pos = [int(pos) for pos in layer1Lines.replace('[', '').replace(']', '').split()]
            
            # Clean the lines for the second and third matrices and split
            layer2Pos = [int(pos) for pos in block[2].replace('[', '').replace(']', '').split()]
            layer3Pos = [int(pos) for pos in block[3].replace('[', '').replace(']', '').split()]
            
            # Append the positions to the respective lists
            layer1PosLists.append(layer1Pos)
            layer2PosLists.append(layer2Pos)
            layer3PosLists.append(layer3Pos)
            i = i+1
    print("Done reading the starting diag positions")
    return layer1PosLists, layer2PosLists, layer3PosLists

# Paths to your files (adjust these paths to your actual files)
starting_positions_file = './diagPos.txt'
accuracies_file = './netAcc.txt'

# Reading data from files
print("Compiling the list of diagonals")
layer1PosList, layer2PosList, layer3PosList = read_diagonal_positions(starting_positions_file)
print("Compiling the list of accuracies")
accuracies = read_accuracies(accuracies_file)
pdb.set_trace()
#Get the average position of the diagonal for the three layers
layer1PosListAvg = [sum(layer1PosList[i])/len(layer1PosList[i]) for i in range(len(layer1PosList))]
layer2PosListAvg = [sum(layer2PosList[i])/len(layer2PosList[i]) for i in range(len(layer2PosList))]
layer3PosListAvg = [sum(layer3PosList[i])/len(layer3PosList[i]) for i in range(len(layer3PosList))]

plt.figure(figsize=(10, 6))
plt.scatter(layer1PosListAvg, accuracies, color='blue', alpha=0.5)
plt.title('Scatter Plot of Accuracy vs. Avg diagonal position Layer 1')
plt.xlabel('Avg diagonal position')
plt.ylabel('Accuracy')
plt.grid(True)
plt.savefig('avgDiagvsAccLayer1.pdf')

plt.figure(figsize=(10, 6))
plt.scatter(layer2PosListAvg, accuracies, color='blue', alpha=0.5)
plt.title('Scatter Plot of Accuracy vs. Avg diagonal position Layer 2')
plt.xlabel('Avg diagonal position')
plt.ylabel('Accuracy')
plt.grid(True)
plt.savefig('avgDiagvsAccLayer2.pdf')

plt.figure(figsize=(10, 6))
plt.scatter(layer3PosListAvg, accuracies, color='blue', alpha=0.5)
plt.title('Scatter Plot of Accuracy vs. Avg diagonal position Layer 3')
plt.xlabel('Avg diagonal position')
plt.ylabel('Accuracy')
plt.grid(True)
plt.savefig('avgDiagvsAccLayer3.pdf')

'''# Preparing the data matrix
data_matrix = np.array([row + [accuracy] for row, accuracy in zip(layer1PosList, accuracies)])

# Plotting the heatmap
plt.figure(figsize=(10, 8))
ax = sns.heatmap(data_matrix, annot=True, cmap="viridis", fmt="g")
ax.set_title('Heatmap of Diagonal Starting Positions and Accuracies')
ax.set_xlabel('Diagonal Position / Accuracy')
ax.set_ylabel('Set Number')
plt.savefig('heatmapLayer1.pdf')'''