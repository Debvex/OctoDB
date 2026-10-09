#Python Interface containing for manipulating numpy vectors
import os
import sys

# Ensure the build directory is in the path for the compiled module
build_path = os.path.join(os.path.dirname(__file__), 'build')
if os.path.exists(build_path):
    sys.path.append(build_path)

# On Windows, we need to explicitly add the MinGW bin directory to the DLL search path
# if the module was compiled with MinGW and depends on its runtime libraries.
mingw_bin = r'C:\mingw64\bin'
if os.name == 'nt' and os.path.exists(mingw_bin):
    os.add_dll_directory(mingw_bin)

import numpy as np
import my_faiss # This is your compiled C++ engine

DIMENSIONS = 128
NUM_VECTORS = 10_000

# 1. Initialize the C++ index
index = my_faiss.FlatIndexL2(DIMENSIONS)

# 2. Generate random embeddings in NumPy
# Memory is allocated in Python, but accessed directly by C++ without copying
vectors = np.random.rand(NUM_VECTORS, DIMENSIONS).astype(np.float32)

# 3. Add to index
print(f"Adding {NUM_VECTORS} vectors...")
index.add(vectors)
print(f"Index now contains {index.ntotal} vectors.")

# 4. Search
query_vector = np.random.rand(DIMENSIONS).astype(np.float32)

# The C++ search function expects a 1D array for a single query vector 
# because it accesses it using a single loop over 'd' dimensions.
distances, indices = index.search(query_vector, 5)

print("\nSearch Results (Top 5):")
for dist, idx in zip(distances, indices):
    print(f"Vector ID: {idx} | L2 Distance: {dist:.4f}")