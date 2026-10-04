## Octo DB
Implementation of a in-memory vector DB like FAISS from scratch.

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