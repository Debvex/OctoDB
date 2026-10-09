cmake_minimum_required(VERSION 3.14)
project(my_faiss LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 14)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)

# C++ does not use a Python virtual environment. Python is required here only
# because this target is a Python extension module.
find_package(Python3 COMPONENTS Interpreter Development REQUIRED)

include(FetchContent)
FetchContent_Declare(
    pybind11
    GIT_REPOSITORY https://github.com/pybind/pybind11.git
    GIT_TAG        v3.1.0
)
FetchContent_MakeAvailable(pybind11)

pybind11_add_module(my_faiss src/index.cpp)

if (MSVC)
    target_compile_options(my_faiss PRIVATE /O2)
else()
    target_compile_options(my_faiss PRIVATE -O3)
endif()
