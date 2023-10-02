# Data-Driven Control of Power Grid
This repository contains the conversion of MATLAB codes used in the following paper into Python:

G. Baggio, D. S. Bassett, F. Pasqualetti "Data-Driven Control of Complex Networks", Nature Communications, vol. 12, no. 1, pp. 1-13, 2021.

The codes compute optimal data-driven controls for fault recovery in power grid networks.

- The main.py file computes optimal data-driven control input for fault recovery in the New England 10-unit 39-bus Test case. It requires NE_test_parameters.py, swing.py, and custom_matlab_functions.py.
- NE_test_parameters.py file contains all the parameters of New England 39-bus 10-generator Test case.
- The swing.py file Simulates power generators swing dynamics.
- The custom_matlab_functions.py file contains two customized MATLAB functions.
