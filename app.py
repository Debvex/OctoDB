#Python Interface containing for manioulating numpy vectors
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

distances, indices = index.search(query_vector, k=5)

print("\nSearch Results (Top 5):")
for dist, idx in zip(distances, indices):
    print(f"Vector ID: {idx} | L2 Distance: {dist:.4f}")