#ifndef ADDER_HPP
#define ADDER_HPP

#include <iostream>
#include <boost/multiprecision/cpp_int.hpp>
#include "type.hpp"

template <int a_bits, int b_bits, int sum_bits>
class Adder {

    public:

    Adder() : sum(0) {}

    void reset() {
        sum = 0;
    }

    void write(uintN_t<a_bits> a , uintN_t<b_bits> b) {
        a_mem = a;
        b_mem = b;
    }

    void process() {
        sum = a_mem + b_mem;
    }

    void read(uintN_t<sum_bits> &output_sum){
        output_sum = sum;
    }

    private:
    uintN_t<a_bits> a_mem;
    uintN_t<b_bits> b_mem;
    uintN_t<sum_bits> sum;

};

#endif // ADDER_HPP