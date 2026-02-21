import pandas as pd
import numpy as np
import matplotlib.pylab as plt

def main():
    # Load the data
    data = pd.read_csv('data.csv')
    
    # Display the first few rows of the data
    print(data.head())
    
    # Plot the data
    plt.figure(figsize=(10, 6))
    plt.scatter(data['x'], data['y'], color='blue', label='Data Points')
    plt.title('Scatter Plot of Data')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.show()