## Octo DB
My very own learning implementation of a in-memory vector DB like FAISS from scratch.

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