Librería con Operaciones para Números Complejos
Esta es una librería creada en el lenguaje Python, en la que puede realizar algunas operaciones con los números complejos, las cuales son:
1) complex_sum(a, b): Esta función se encarga de sumar dos números complejos, retornando un arreglo el cual tendrá una parte entera y una parte compleja compleja de la operación. 
(a1,b1) + (a2,b2) = (a1 + a2, b1 + b2)
2)complex_rest(a,b): Esta función se encarga de realizar la resta entre dos números complejos, retornando un arreglo el cual tendrá una parte entera y una parte compleja compleja de la operación.
(a1,b1) - (a2,b2) = (a1 - a1, b1 - b2)
3) complex_multiplication(a, b): Esta función se encarga de multiplicar dos números complejos, retornando un arreglo el cual tendrá una parte entera y una parte compleja compleja de la operación.
(a1,b1) x (a2,b2) = (a1,b1)(a2,b2) = (a1a2 - b1b2, a1b2 + a2b1)
4)complex_division(a, b):Esta función realiza la división de dos números complejos,  retornando un arreglo el cual tendrá una parte entera y una parte compleja compleja de la operación.
((a1a2 + b1+b2) / (a2^2) + (b2^2), (a2b1 - a1b2) / (a2^2) + (b2^2))

5) complex_module(a): Esta función calcula el módulo, el cual es encontrar la raíz de los dos valores y elevándolo al cuadrado, recordando que el valor del complejo no tomara la i sino solo el número. 
√(a^2+b^2 )
6) complex_conjugated(a): Esta función lo que hace es cambiarle el sigo al valor del número complejo, pasando de positivo a negativo y lo mismo, al contrario, dejando el valor entero igual.
(a,-b)
7) Cartesian_to_polar(a): Esta función lo que realiza es el cambio de coordenadas cartesianas a polares.
〖(√(a^2+b^2 ),tan〗^(-1)⁡〖(b/a))〗
8) polar_to_Cartesian(a, b): Esta función lo que realiza es el cambio de coordenadas polares a cartesianas.
(a cos⁡〖(b),a sin⁡〖(b))〗 〗
9) fase(a): Retorna la fase cartesiana.
tan^(-1)⁡(b/a)
