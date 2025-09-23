#include <boost/multiprecision/cpp_int.hpp>
#include <iostream>

#include "includes/adder.hpp"

int main() {

    On souhaite déja récupérer les données d'entrées. Sauf que c'est données sont différents signaux. Cela va alors demander que l'on les parses puis on enregistre dans des variables qui peuvent dépenre afin d





    return 0;

}






// Adder<4> adder; // adder 4 bits

// adder.reset();
// std::cout << "Après reset : sum=" << adder.get_sum() << "\n";

// for (int cycle = 0; cycle < 10; cycle++) {
//     uintN_t<4> a = cycle;
//     uintN_t<4> b = 3;
//     adder.tick(a, b);

//     std::cout << "Cycle " << cycle
//               << " : a=" << a
//               << " b=" << b
//               << " sum=" << adder.get_sum() << "\n";
// }