import numpy as np
import pandas as pd

from pandas import DataFrame
# Create a DataFrame with random data
df = DataFrame(np.random.randn(5, 3), columns=['A', 'B', 'C'])

# Display the DataFrame
print("DataFrame with random data:")
print(df)
# Display the first few rows of the DataFrame
print("\nFirst few rows of the DataFrame:")
print(df.head())
