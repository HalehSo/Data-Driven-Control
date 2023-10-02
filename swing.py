# Swing - Simulating Power Generators Swing Dynamics
# from Y. Susuki, I. Mezic, T. Hikihara, "Coherent Swing Instability of
# Power Grids", J Nonlinear Sci, 2011
# Converted to Python by Haleh Soleimany, September 2023

import numpy as np
import math
import NE_test_parameters

H = NE_test_parameters.H
P = NE_test_parameters.P
D = NE_test_parameters.D
E = NE_test_parameters.E
Y_3 = NE_test_parameters.Y_3
Y_32 = NE_test_parameters.Y_32

# fault initial time
T_fault_in = 2
# fault final time
T_fault_end = 2.525

def solving_swing(t,delta_t,y,u):
    """Simulate power generators swing dynamics."""
    y_p = np.zeros(18)

    Y = Y_3

    k = [delta_t*(1/H[1][1])*(P[1]-Y[1][1].real*E[1]**2-E[1]*E[0]*Y[1][0].real-E[1]*E[2]*Y[1][2].real-E[1]*E[3]*Y[1][3].real-E[1]*E[4]*Y[1][4].real-E[1]*E[5]*Y[1][5].real-E[1]*E[6]*Y[1][6].real-E[1]*E[7]*Y[1][7].real-E[1]*E[8]*Y[1][8].real-E[1]*E[9]*Y[1][9].real),
         delta_t*(1/H[2][2])*(P[2]-Y[2][2].real*E[2]**2-E[2]*E[0]*Y[2][0].real-E[2]*E[1]*Y[2][1].real-E[2]*E[3]*Y[2][3].real-E[2]*E[4]*Y[2][4].real-E[2]*E[5]*Y[2][5].real-E[2]*E[6]*Y[2][6].real-E[2]*E[7]*Y[2][7].real-E[2]*E[8]*Y[2][8].real-E[2]*E[9]*Y[2][9].real),
         delta_t*(1/H[3][3])*(P[3]-Y[3][3].real*E[3]**2-E[3]*E[0]*Y[3][0].real-E[3]*E[1]*Y[3][1].real-E[3]*E[2]*Y[3][2].real-E[3]*E[4]*Y[3][4].real-E[3]*E[5]*Y[3][5].real-E[3]*E[6]*Y[3][6].real-E[3]*E[7]*Y[3][7].real-E[3]*E[8]*Y[3][8].real-E[3]*E[9]*Y[3][9].real),
         delta_t*(1/H[4][4])*(P[4]-Y[4][4].real*E[4]**2-E[4]*E[0]*Y[4][0].real-E[4]*E[1]*Y[4][1].real-E[4]*E[2]*Y[4][2].real-E[4]*E[3]*Y[4][3].real-E[4]*E[5]*Y[4][5].real-E[4]*E[6]*Y[4][6].real-E[4]*E[7]*Y[4][7].real-E[4]*E[8]*Y[4][8].real-E[4]*E[9]*Y[4][9].real),
         delta_t*(1/H[5][5])*(P[5]-Y[5][5].real*E[5]**2-E[5]*E[0]*Y[5][0].real-E[5]*E[1]*Y[5][1].real-E[5]*E[2]*Y[5][2].real-E[5]*E[3]*Y[5][3].real-E[5]*E[4]*Y[5][4].real-E[5]*E[6]*Y[5][6].real-E[5]*E[7]*Y[5][7].real-E[5]*E[8]*Y[5][8].real-E[5]*E[9]*Y[5][9].real),
         delta_t*(1/H[6][6])*(P[6]-Y[6][6].real*E[6]**2-E[6]*E[0]*Y[6][0].real-E[6]*E[1]*Y[6][1].real-E[6]*E[2]*Y[6][2].real-E[6]*E[3]*Y[6][3].real-E[6]*E[4]*Y[6][4].real-E[6]*E[5]*Y[6][5].real-E[6]*E[7]*Y[6][7].real-E[6]*E[8]*Y[6][8].real-E[6]*E[9]*Y[6][9].real),
         delta_t*(1/H[7][7])*(P[7]-Y[7][7].real*E[7]**2-E[7]*E[0]*Y[7][0].real-E[7]*E[1]*Y[7][1].real-E[7]*E[2]*Y[7][2].real-E[7]*E[3]*Y[7][3].real-E[7]*E[4]*Y[7][4].real-E[7]*E[5]*Y[7][5].real-E[7]*E[6]*Y[7][6].real-E[7]*E[8]*Y[7][8].real-E[7]*E[9]*Y[7][9].real),
         delta_t*(1/H[8][8])*(P[8]-Y[8][8].real*E[8]**2-E[8]*E[0]*Y[8][0].real-E[8]*E[1]*Y[8][1].real-E[8]*E[2]*Y[8][2].real-E[8]*E[3]*Y[8][3].real-E[8]*E[4]*Y[8][4].real-E[8]*E[5]*Y[8][5].real-E[8]*E[6]*Y[8][6].real-E[8]*E[7]*Y[8][7].real-E[8]*E[9]*Y[8][9].real),
         delta_t*(1/H[9][9])*(P[9]-Y[9][9].real*E[9]**2-E[9]*E[0]*Y[9][0].real-E[9]*E[1]*Y[9][1].real-E[9]*E[2]*Y[9][2].real-E[9]*E[3]*Y[9][3].real-E[9]*E[4]*Y[9][4].real-E[9]*E[5]*Y[9][5].real-E[9]*E[6]*Y[9][6].real-E[9]*E[7]*Y[9][7].real-E[9]*E[8]*Y[9][8].real) ]

    if t < 2:
        Y = Y_3
    elif t >= T_fault_in and t < T_fault_end:
        Y = Y_32
    else:
        Y = Y_3

    y_p[0] = delta_t*y[9]+y[0]+u[0]
    y_p[1] = delta_t*y[10]+y[1]+u[1]
    y_p[2] = delta_t*y[11]+y[2]+u[2]
    y_p[3] = delta_t*y[12]+y[3]+u[3]
    y_p[4] = delta_t*y[13]+y[4]+u[4]
    y_p[5] = delta_t*y[14]+y[5]+u[5]
    y_p[6] = delta_t*y[15]+y[6]+u[6]
    y_p[7] = delta_t*y[16]+y[7]+u[7]
    y_p[8] = delta_t*y[17]+y[8]+u[8]

    y_p[9] = delta_t*(1/H[1][1])*(-1*D[1][1]*(y[9]+u[0])+P[1]-Y[1][1].real*E[1]**2-\
    E[1]*E[0]*(Y[1][0].real*math.cos(y[0])+Y[1][0].imag*math.sin(y[0]))-\
    E[1]*E[2]*(Y[1][2].real*math.cos(y[0]-y[1])+Y[1][2].imag*math.sin(y[0]-y[1]))-\
    E[1]*E[3]*(Y[1][3].real*math.cos(y[0]-y[2])+Y[1][3].imag*math.sin(y[0]-y[2]))-\
    E[1]*E[4]*(Y[1][4].real*math.cos(y[0]-y[3])+Y[1][4].imag*math.sin(y[0]-y[3]))-\
    E[1]*E[5]*(Y[1][5].real*math.cos(y[0]-y[4])+Y[1][5].imag*math.sin(y[0]-y[4]))-\
    E[1]*E[6]*(Y[1][6].real*math.cos(y[0]-y[5])+Y[1][6].imag*math.sin(y[0]-y[5]))-\
    E[1]*E[7]*(Y[1][7].real*math.cos(y[0]-y[6])+Y[1][7].imag*math.sin(y[0]-y[6]))-\
    E[1]*E[8]*(Y[1][8].real*math.cos(y[0]-y[7])+Y[1][8].imag*math.sin(y[0]-y[7]))-\
    E[1]*E[9]*(Y[1][9].real*math.cos(y[0]-y[8])+Y[1][9].imag*math.sin(y[0]-y[8])))+y[9]-k[0]

    y_p[10] = delta_t*(1/H[2][2])*(-D[2][2]*(y[10]+u[1])+P[2]-Y[2][2].real*E[2]**2-\
    E[2]*E[0]*(Y[2][0].real*math.cos(y[1])+Y[2][0].imag*math.sin(y[1]))-\
    E[2]*E[1]*(Y[2][1].real*math.cos(y[1]-y[0])+Y[2][1].imag*math.sin(y[1]-y[0]))-\
    E[2]*E[3]*(Y[2][3].real*math.cos(y[1]-y[2])+Y[2][3].imag*math.sin(y[1]-y[2]))-\
    E[2]*E[4]*(Y[2][4].real*math.cos(y[1]-y[3])+Y[2][4].imag*math.sin(y[1]-y[3]))-\
    E[2]*E[5]*(Y[2][5].real*math.cos(y[1]-y[4])+Y[2][5].imag*math.sin(y[1]-y[4]))-\
    E[2]*E[6]*(Y[2][6].real*math.cos(y[1]-y[5])+Y[2][6].imag*math.sin(y[1]-y[5]))-\
    E[2]*E[7]*(Y[2][7].real*math.cos(y[1]-y[6])+Y[2][7].imag*math.sin(y[1]-y[6]))-\
    E[2]*E[8]*(Y[2][8].real*math.cos(y[1]-y[7])+Y[2][8].imag*math.sin(y[1]-y[7]))-\
    E[2]*E[9]*(Y[2][9].real*math.cos(y[1]-y[8])+Y[2][9].imag*math.sin(y[1]-y[8])))+y[10]-k[1]

    y_p[11] = delta_t*(1/H[3][3])*(-D[3][3]*(y[11]+u[2])+P[3]-Y[3][3].real*E[3]**2-\
    E[3]*E[0]*(Y[3][0].real*math.cos(y[2])+Y[3][0].imag*math.sin(y[2]))-\
    E[3]*E[1]*(Y[3][1].real*math.cos(y[2]-y[0])+Y[3][1].imag*math.sin(y[2]-y[0]))-\
    E[3]*E[2]*(Y[3][2].real*math.cos(y[2]-y[1])+Y[3][2].imag*math.sin(y[2]-y[1]))-\
    E[3]*E[4]*(Y[3][4].real*math.cos(y[2]-y[3])+Y[3][4].imag*math.sin(y[2]-y[3]))-\
    E[3]*E[5]*(Y[3][5].real*math.cos(y[2]-y[4])+Y[3][5].imag*math.sin(y[2]-y[4]))-\
    E[3]*E[6]*(Y[3][6].real*math.cos(y[2]-y[5])+Y[3][6].imag*math.sin(y[2]-y[5]))-\
    E[3]*E[7]*(Y[3][7].real*math.cos(y[2]-y[6])+Y[3][7].imag*math.sin(y[2]-y[6]))-\
    E[3]*E[8]*(Y[3][8].real*math.cos(y[2]-y[7])+Y[3][8].imag*math.sin(y[2]-y[7]))-\
    E[3]*E[9]*(Y[3][9].real*math.cos(y[2]-y[8])+Y[3][9].imag*math.sin(y[2]-y[8])))+y[11]-k[2]                          

    y_p[12] = delta_t*(1/H[4][4])*(-D[4][4]*(y[12]+u[3])+P[4]-Y[4][4].real*E[4]**2-\
    E[4]*E[0]*(Y[4][0].real*math.cos(y[3])+Y[4][0].imag*math.sin(y[3]))-\
    E[4]*E[1]*(Y[4][1].real*math.cos(y[3]-y[0])+Y[4][1].imag*math.sin(y[3]-y[0]))-\
    E[4]*E[2]*(Y[4][2].real*math.cos(y[3]-y[1])+Y[4][2].imag*math.sin(y[3]-y[1]))-\
    E[4]*E[3]*(Y[4][3].real*math.cos(y[3]-y[2])+Y[4][3].imag*math.sin(y[3]-y[2]))-\
    E[4]*E[5]*(Y[4][5].real*math.cos(y[3]-y[4])+Y[4][5].imag*math.sin(y[3]-y[4]))-\
    E[4]*E[6]*(Y[4][6].real*math.cos(y[3]-y[5])+Y[4][6].imag*math.sin(y[3]-y[5]))-\
    E[4]*E[7]*(Y[4][7].real*math.cos(y[3]-y[6])+Y[4][7].imag*math.sin(y[3]-y[6]))-\
    E[4]*E[8]*(Y[4][8].real*math.cos(y[3]-y[7])+Y[4][8].imag*math.sin(y[3]-y[7]))-\
    E[4]*E[9]*(Y[4][9].real*math.cos(y[3]-y[8])+Y[4][9].imag*math.sin(y[3]-y[8])))+y[12]-k[3] 

    y_p[13] = delta_t*(1/H[5][5])*(-D[5][5]*(y[13]+u[4])+P[5]-Y[5][5].real*E[5]**2-\
    E[5]*E[0]*(Y[5][0].real*math.cos(y[4])+Y[5][0].imag*math.sin(y[4]))-\
    E[5]*E[1]*(Y[5][1].real*math.cos(y[4]-y[0])+Y[5][1].imag*math.sin(y[4]-y[0]))-\
    E[5]*E[2]*(Y[5][2].real*math.cos(y[4]-y[1])+Y[5][2].imag*math.sin(y[4]-y[1]))-\
    E[5]*E[3]*(Y[5][3].real*math.cos(y[4]-y[2])+Y[5][3].imag*math.sin(y[4]-y[2]))-\
    E[5]*E[4]*(Y[5][4].real*math.cos(y[4]-y[3])+Y[5][4].imag*math.sin(y[4]-y[3]))-\
    E[5]*E[6]*(Y[5][6].real*math.cos(y[4]-y[5])+Y[5][6].imag*math.sin(y[4]-y[5]))-\
    E[5]*E[7]*(Y[5][7].real*math.cos(y[4]-y[6])+Y[5][7].imag*math.sin(y[4]-y[6]))-\
    E[5]*E[8]*(Y[5][8].real*math.cos(y[4]-y[7])+Y[5][8].imag*math.sin(y[4]-y[7]))-\
    E[5]*E[9]*(Y[5][9].real*math.cos(y[4]-y[8])+Y[5][9].imag*math.sin(y[4]-y[8])))+y[13]-k[4]

    y_p[14] = delta_t*(1/H[6][6])*(-D[6][6]*(y[14]+u[5])+P[6]-Y[6][6].real*E[6]**2-\
    E[6]*E[0]*(Y[6][0].real*math.cos(y[5])+Y[6][0].imag*math.sin(y[5]))-\
    E[6]*E[1]*(Y[6][1].real*math.cos(y[5]-y[0])+Y[6][1].imag*math.sin(y[5]-y[0]))-\
    E[6]*E[2]*(Y[6][2].real*math.cos(y[5]-y[1])+Y[6][2].imag*math.sin(y[5]-y[1]))-\
    E[6]*E[3]*(Y[6][3].real*math.cos(y[5]-y[2])+Y[6][3].imag*math.sin(y[5]-y[2]))-\
    E[6]*E[4]*(Y[6][4].real*math.cos(y[5]-y[3])+Y[6][4].imag*math.sin(y[5]-y[3]))-\
    E[6]*E[5]*(Y[6][5].real*math.cos(y[5]-y[4])+Y[6][5].imag*math.sin(y[5]-y[4]))-\
    E[6]*E[7]*(Y[6][7].real*math.cos(y[5]-y[6])+Y[6][7].imag*math.sin(y[5]-y[6]))-\
    E[6]*E[8]*(Y[6][8].real*math.cos(y[5]-y[7])+Y[6][8].imag*math.sin(y[5]-y[7]))-\
    E[6]*E[9]*(Y[6][9].real*math.cos(y[5]-y[8])+Y[6][9].imag*math.sin(y[5]-y[8])))+y[14]-k[5]

    y_p[15] = delta_t*(1/H[7][7])*(-D[7][7]*(y[15]+u[6])+P[7]-Y[7][7].real*E[7]**2-\
    E[7]*E[0]*(Y[7][0].real*math.cos(y[6])+Y[7][0].imag*math.sin(y[6]))-\
    E[7]*E[1]*(Y[7][1].real*math.cos(y[6]-y[0])+Y[7][1].imag*math.sin(y[6]-y[0]))-\
    E[7]*E[2]*(Y[7][2].real*math.cos(y[6]-y[1])+Y[7][2].imag*math.sin(y[6]-y[1]))-\
    E[7]*E[3]*(Y[7][3].real*math.cos(y[6]-y[2])+Y[7][3].imag*math.sin(y[6]-y[2]))-\
    E[7]*E[4]*(Y[7][4].real*math.cos(y[6]-y[3])+Y[7][4].imag*math.sin(y[6]-y[3]))-\
    E[7]*E[5]*(Y[7][5].real*math.cos(y[6]-y[4])+Y[7][5].imag*math.sin(y[6]-y[4]))-\
    E[7]*E[6]*(Y[7][6].real*math.cos(y[6]-y[5])+Y[7][6].imag*math.sin(y[6]-y[5]))-\
    E[7]*E[8]*(Y[7][8].real*math.cos(y[6]-y[7])+Y[7][8].imag*math.sin(y[6]-y[7]))-\
    E[7]*E[9]*(Y[7][9].real*math.cos(y[6]-y[8])+Y[7][9].imag*math.sin(y[6]-y[8])))+y[15]-k[6]

    y_p[16] = delta_t*(1/H[8][8])*(-D[8][8]*(y[16]+u[7])+P[8]-Y[8][8].real*E[8]**2-\
    E[8]*E[0]*(Y[8][0].real*math.cos(y[7])+Y[8][0].imag*math.sin(y[7]))-\
    E[8]*E[1]*(Y[8][1].real*math.cos(y[7]-y[0])+Y[8][1].imag*math.sin(y[7]-y[0]))-\
    E[8]*E[2]*(Y[8][2].real*math.cos(y[7]-y[1])+Y[8][2].imag*math.sin(y[7]-y[1]))-\
    E[8]*E[3]*(Y[8][3].real*math.cos(y[7]-y[2])+Y[8][3].imag*math.sin(y[7]-y[2]))-\
    E[8]*E[4]*(Y[8][4].real*math.cos(y[7]-y[3])+Y[8][4].imag*math.sin(y[7]-y[3]))-\
    E[8]*E[5]*(Y[8][5].real*math.cos(y[7]-y[4])+Y[8][5].imag*math.sin(y[7]-y[4]))-\
    E[8]*E[6]*(Y[8][6].real*math.cos(y[7]-y[5])+Y[8][6].imag*math.sin(y[7]-y[5]))-\
    E[8]*E[7]*(Y[8][7].real*math.cos(y[7]-y[6])+Y[8][7].imag*math.sin(y[7]-y[6]))-\
    E[8]*E[9]*(Y[8][9].real*math.cos(y[7]-y[8])+Y[8][9].imag*math.sin(y[7]-y[8])))+y[16]-k[7]

    y_p[17] = delta_t*(1/H[9][9])*(-D[9][9]*(y[17]+u[8])+P[9]-Y[9][9].real*E[9]**2-\
    E[9]*E[0]*(Y[9][0].real*math.cos(y[8])+Y[9][0].imag*math.sin(y[8]))-\
    E[9]*E[1]*(Y[9][1].real*math.cos(y[8]-y[0])+Y[9][1].imag*math.sin(y[8]-y[0]))-\
    E[9]*E[2]*(Y[9][2].real*math.cos(y[8]-y[1])+Y[9][2].imag*math.sin(y[8]-y[1]))-\
    E[9]*E[3]*(Y[9][3].real*math.cos(y[8]-y[2])+Y[9][3].imag*math.sin(y[8]-y[2]))-\
    E[9]*E[4]*(Y[9][4].real*math.cos(y[8]-y[3])+Y[9][4].imag*math.sin(y[8]-y[3]))-\
    E[9]*E[5]*(Y[9][5].real*math.cos(y[8]-y[4])+Y[9][5].imag*math.sin(y[8]-y[4]))-\
    E[9]*E[6]*(Y[9][6].real*math.cos(y[8]-y[5])+Y[9][6].imag*math.sin(y[8]-y[5]))-\
    E[9]*E[7]*(Y[9][7].real*math.cos(y[8]-y[6])+Y[9][7].imag*math.sin(y[8]-y[6]))-\
    E[9]*E[8]*(Y[9][8].real*math.cos(y[8]-y[7])+Y[9][8].imag*math.sin(y[8]-y[7])))+y[17]-k[8]

    return y_p