 #ifndef TYPE_HPP
#define TYPE_HPP

#include <iostream>
#include <boost/multiprecision/cpp_int.hpp>
 
using namespace boost::multiprecision;
template <int N>
using uintN_t = boost::multiprecision::number<boost::multiprecision::cpp_int_backend<N, N, boost::multiprecision::unsigned_magnitude, boost::multiprecision::unchecked, void>>;


#endif // TYPE_HPP
