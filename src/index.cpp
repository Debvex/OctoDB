#include <pybind11/pybind11.h>
#include <pybind11/numpy.h>
#include <vector>
#include <queue>

namespace py = pybind11;

class FlatIndexL2 {
private:
    int d;                     // Dimensionality of the vectors
    int ntotal;                // Total number of vectors indexed
    std::vector<float> data;   // Flattened 1D array for absolute memory locality

public:
    FlatIndexL2(int dimension) : d(dimension), ntotal(0) {}

    void add(py::array_t<float> py_vectors) {
        py::buffer_info buf = py_vectors.request();
        int num_new_vectors = buf.shape[0];
        float* ptr = static_cast<float*>(buf.ptr);

        data.insert(data.end(), ptr, ptr + (num_new_vectors * d));
        ntotal += num_new_vectors;
    }

    py::tuple search(py::array_t<float> py_query, int k) {
        py::buffer_info buf = py_query.request();
        float* q_ptr = static_cast<float*>(buf.ptr);
        
      
        auto dists_out = py::array_t<float>(k);
        auto idxs_out = py::array_t<int>(k);
        float* dists_ptr = static_cast<float*>(dists_out.request().ptr);
        int* idxs_ptr = static_cast<int*>(idxs_out.request().ptr);
        
       
        std::priority_queue<std::pair<float, int>> max_heap;

       
        for (int i = 0; i < ntotal; i++) {
            float dist = 0;
            for (int j = 0; j < d; j++) {
                float diff = q_ptr[j] - data[i * d + j];
                dist += diff * diff;
            }
            
            max_heap.push({dist, i});
            if (max_heap.size() > k) {
                max_heap.pop(); 
            }
        }

        for (int i = k - 1; i >= 0; i--) {
            dists_ptr[i] = max_heap.top().first;
            idxs_ptr[i] = max_heap.top().second;
            max_heap.pop();
        }

        return py::make_tuple(dists_out, idxs_out);
    }
    
    int get_ntotal() const { return ntotal; }
};


PYBIND11_MODULE(my_faiss, m) {
    m.doc() = "Custom Vector DB Engine written in C++";

    py::class_<FlatIndexL2>(m, "FlatIndexL2")
        .def(py::init<int>(), py::arg("dimension"))
        .def("add", &FlatIndexL2::add, "Add vectors to the index")
        .def("search", &FlatIndexL2::search, "Search for k nearest neighbors")
        .def_property_readonly("ntotal", &FlatIndexL2::get_ntotal);
}