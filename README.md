# OctoDB

OctoDB is a lightweight, in-memory vector database built from scratch with a focus on understanding how fast similarity search works under the hood. Inspired by libraries such as FAISS, the project stores high-dimensional vectors and provides efficient nearest-neighbor queries using a C++ engine with a Python interface.

Currently, it implements a `FlatIndexL2` for exact brute-force search.

## Implementation Plan (HNSW)

Future goals include transitioning to an HNSW (Hierarchical Navigable Small World) index:
- Implement multi-layer graph navigation.
- Add configurable parameters (`M`, `efConstruction`, `efSearch`).
- Support bidirectional-link maintenance and neighbor-pruning.
- Benchmarking against the current brute-force implementation.

## Project Structure

```text
OctoDB/
├── CMakeLists.txt      # C++ build instructions
├── pyproject.toml      # Python project metadata and dependencies
├── uv.lock             # uv lockfile
├── app.py              # Python interface and example usage
├── src/
│   └── index.cpp       # C++ engine source code (my_faiss)
├── build/              # CMake build output directory
└── README.md           # Project documentation
```

## Requirements

- **C++ Compiler**: A compiler supporting C++14 (e.g., GCC, Clang, or MSVC).
- **CMake**: Version 3.14 or higher.
- **Python**: Version 3.14 or higher.
- **Dependencies**:
  - `numpy` (>=2.5.3)
  - `pybind11` (v3.1.0, handled via CMake FetchContent)

## Setup and Installation

### 1. Environment Setup

This project uses `uv` for Python package management, but you can also use `pip`.

**Using uv:**
```bash
uv sync
```

**Using pip:**
```bash
python -m venv venv
# On Windows:
.\venv\Scripts\activate
# On Linux/macOS:
source venv/bin/activate

pip install .
```

### 2. Build the C++ Engine

The C++ engine must be compiled as a Python module named `my_faiss`.

```bash
mkdir build
cd build
cmake ..
cmake --build . --config Release
```

**Note for Windows (MinGW):**
If you are using MinGW, ensure the bin directory (e.g., `C:\mingw64\bin`) is in your PATH, or update the path in `app.py`.

## Running the Application

After building the engine, ensure the compiled `.pyd` (Windows) or `.so` (Linux/macOS) file is in the `build/` directory. `app.py` is configured to look for the module in that location.

```bash
# Ensure your environment is activated
python app.py
```

## Scripts

- `app.py`: Demonstrates initializing the index, adding random vectors, and performing a search.

## Environment Variables

- No specific environment variables are currently required.

## Tests

- [TODO] Add unit tests for both the C++ engine and Python interface.
- [TODO] Add benchmarks for search latency and accuracy.

## License

- [TODO] Define project license.