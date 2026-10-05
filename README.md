## Octo DB

Octo DB is a lightweight, in-memory vector database built from scratch with a focus on understanding how fast similarity search works under the hood. Inspired by libraries such as FAISS, the project stores high-dimensional vectors and provides efficient approximate nearest-neighbor queries without relying on an external database engine.

Implementation plan:
> - Implement an HNSW (Hierarchical Navigable Small World) index using skip-list-style, multi-layer graph navigation.
> - Add configurable construction and search parameters, including the maximum number of neighbors (`M`), construction breadth (`efConstruction`), and search breadth (`efSearch`).
> - Support insertion by selecting an entry point, searching progressively through each graph layer, and connecting each new vector to its closest neighbors.
> - Implement approximate nearest-neighbor search from the top layer down to layer zero, returning the requested number of nearest vectors and their distances.
> - Add neighbor-pruning and bidirectional-link maintenance to keep the graph navigable as the index grows.
> - Add tests and benchmarks to validate search accuracy, insertion behavior, and performance against the current brute-force implementation.

### Folder structure:
```text
my_vector_db/
├── CMakeLists.txt        # the C++ build instructions
├── src/
│   └── index.cpp         # the C++ engine source code
├── app.py                # the Python API
├── requirements.txt      # python dependencies
├── build/                # where CMake outputs the .so/.pyd file
└── venv/                 # the isolated Python environment
```

### Get Started

## 1. Create and Activate the Virtual Environment

**On Linux**

```bash
python3 -m venv venv
source venv/bin/activate

```
## 2. Install Dependencies

The `requirements.txt` file in your root folder:

```text
numpy>=2.5.0
pybind11==3.1.0
```

installing them into your venv:

```bash
pip install -r requirements.txt

```

## 3. Build the C++ Engine (Inside the Venv)

for the CMake build:

```bash
mkdir build
cd build
cmake ..

```

**On Linux / macOS:**

```bash
make

```

**On Windows (Visual Studio / MSVC):**

```cmd
cmake --build . --config Release

```

## 4. Link and Run

Copy the single compiled .so file out of the `build/` directory and place it in your root directory next to `app.py`.

```text
my_vector_db/
├── app.py
├── my_faiss.cpython-310-x86_64-linux-gnu.so  <-- The compiled C++ engine
...

```

Run your Python script:

```bash
python app.py

```