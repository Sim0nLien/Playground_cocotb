#include <iostream>
#include <boost/multiprecision/cpp_int.hpp>

template <int N>
using uintN_t = boost::multiprecision::number<boost::multiprecision::cpp_int_backend<N, N, boost::multiprecision::unsigned_magnitude, boost::multiprecision::unchecked, void>>;

template <int N>
class Adder {

    public:

    Adder() : (0) {}

    void reset() {
        sum = 0;
    }

    void tick(uintN_t<N> a , uintN_t<N> b) {
        sum = a + b; 
    }

    uintN_t<N> get_sum() const {
        return sum;
    }

    private:
    uintN_t<N> sum;

};