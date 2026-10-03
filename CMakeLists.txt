cmake_minimum_required(VERSION 3.14)
project(my_faiss)

# Enforce modern C++ and hardware-specific optimization (SIMD)
set(CMAKE_CXX_STANDARD 14)
set(CMAKE_CXX_FLAGS "-O3 -march=native")

# 1. Find the Python installation located in your virtual environment
find_package(Python3 COMPONENTS Interpreter Development REQUIRED)

# 2. Tell CMake to download Pybind11 v3.1.0 directly from GitHub
include(FetchContent)
FetchContent_Declare(
    pybind11
    GIT_REPOSITORY https://github.com/pybind/pybind11.git
    GIT_TAG        v3.1.0
)
FetchContent_MakeAvailable(pybind11)

# 3. Compile the C++ code into a Python module (.so or .pyd)
pybind11_add_module(my_faiss src/index.cpp)