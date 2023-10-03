# DATA_DRIVEN_FAULT_RECOVERY - compute optimal data-driven control input
# for fault recovery in the New England 10-unit 39-bus Test case
# Other m-files required: NE_test_parameters.m
# Author: Giacomo Baggio
# email: baggio [dot] giacomo [at] gmail [dot] com
# July 2020; Last revision: 26-July-2020
# Converted to Python by Haleh Soleimany, September 2023

# load grid parameters
import NE_test_parameters
import numpy as np
import swing
import custom_matlab_functions
import scipy
from numpy import *
import matplotlib.pyplot as plt
from progress import printProgressBar

H = NE_test_parameters.H
P = NE_test_parameters.P
D = NE_test_parameters.D
E = NE_test_parameters.E
Y_3 = NE_test_parameters.Y_3
Y_32 = NE_test_parameters.Y_32

# initial stable state
y_0 = np.array([0.1564, 0.1806, 0.1631, 0.3135, 0.1823, 0.1849, 0.1652, 0.2953, -0.06165, 0, 0, 0, 0, 0, 0, 0, 0, 0])
y_0 = np.zeros(18)

# sampling time
delta_t = 2e-4
# final simulation time
T_sim = 15
# vector of simulation times
tspan = np.arange(0, T_sim, delta_t)
# fault initial time
T_fault_in = 2
# fault final time
T_fault_end = 2.525
# number of inputs
m = 9
# number of states
n = 18
# control horizon
T = 0.1
# final stable state
xf = y_0
# control starting time
t_c = 3

Y = Y_3

P = np.array([1.2500, 2.4943, 3.2500, 3.1600, 2.5400, 3.2500, 2.8000, 2.7000, 4.1500, 5.0000])

k = 0
yy = []
for t in tspan:
    A_0 = swing.solving_swing(t,delta_t,y_0,np.zeros(m))
    yy.append(A_0)
    y_0 = A_0
    k += 1
yy = np.array(yy)

# initial state control
x_0 = yy[round(t_c/delta_t)]

# Plot the Initial State Control.
plt.style.use("seaborn")
fig, ax_0 = plt.subplots()
ax_0.plot(tspan, yy[:, 0], color='red', label = "gen 10")
ax_0.plot(tspan, yy[:, 1], color='blue', label = "gen 2")
ax_0.plot(tspan, yy[:, 2], color='green', label = "gen 3")
ax_0.plot(tspan, yy[:, 3], color='yellow', label = "gen 4")
ax_0.plot(tspan, yy[:, 4], color='cyan', label = "gen 5")
ax_0.plot(tspan, yy[:, 5], color='magenta', label = "gen 6")
ax_0.plot(tspan, yy[:, 6], color='black', label = "gen 7")
ax_0.plot(tspan, yy[:, 7], color='hotpink', label = "gen 8")
ax_0.plot(tspan, yy[:, 8], color='darkviolet', label = "gen 9")
ax_0.fill_between([T_fault_in, T_fault_in, T_fault_end, T_fault_end], [-20, 200, 200, -20], -20, facecolor='red', alpha=0.2)
plt.legend(loc="upper left")

# Format the Initial State Control. 
ax_0.set_title('Initial State Control', fontsize=20)
ax_0.set_xlabel('Time(sec)', fontsize=14)
ax_0.set_ylabel('Phase', fontsize=14)

# Plot the Initial State Control.
plt.style.use("seaborn")
fig, ax_1 = plt.subplots()
ax_1.plot(tspan, yy[:, 9], color='red', label = "gen 10")
ax_1.plot(tspan, yy[:, 10], color='blue', label = "gen 2")
ax_1.plot(tspan, yy[:, 11], color='green', label = "gen 3")
ax_1.plot(tspan, yy[:, 12], color='yellow', label = "gen 4")
ax_1.plot(tspan, yy[:, 13], color='cyan', label = "gen 5")
ax_1.plot(tspan, yy[:, 14], color='magenta', label = "gen 6")
ax_1.plot(tspan, yy[:, 15], color='black', label = "gen 7")
ax_1.plot(tspan, yy[:, 16], color='hotpink', label = "gen 8")
ax_1.plot(tspan, yy[:, 17], color='darkviolet', label = "gen 9")
ax_1.fill_between([T_fault_in, T_fault_in, T_fault_end, T_fault_end], [-20, 60, 60, -20], -20, facecolor='red', alpha=0.2)
plt.legend(loc="upper left")

# Format the Initial State Control.
ax_1.set_title('Initial State Control', fontsize=20)
ax_1.set_xlabel('Time(sec)', fontsize=14)
ax_1.set_ylabel('Frequency', fontsize=14)

# generate data for control

# number of samples
N = 5000
# variance of inital states
sigma = 0.01
# data matrices
U = []
X_0 = []
X_1T = []
X_T = []

printProgressBar(0, N, prefix = 'Progress:', suffix = 'Complete', length = 50)
for i in range(N):
    printProgressBar(i, N, prefix = 'Progress:', suffix = 'Complete', length = 50)
    k = 0
    # random input
    u = 1e-3 * np.random.randn(m,round(T/delta_t))
    # random initial state
    y_0 = np.array([0.1564 + sigma * np.random.randn(), 0.1806 + sigma * np.random.randn(), 0.1631 + sigma * np.random.randn(), 0.3135 + sigma * np.random.randn(), 0.1823 + sigma * np.random.randn(), 0.1849 + sigma * np.random.randn(), 0.1652 + sigma * np.random.randn(), 0.2953 + sigma * np.random.randn(), -0.06165 + sigma * np.random.randn(), 0 + sigma * np.random.randn(), 0 + sigma * np.random.randn(), 0 + sigma * np.random.randn(), 0 + sigma * np.random.randn(), 0 + sigma * np.random.randn(), 0 + sigma * np.random.randn(), 0 + sigma * np.random.randn(), 0 + sigma * np.random.randn(), 0 + sigma * np.random.randn()])
    y_0 = np.array([sigma * np.random.randn(), sigma * np.random.randn(), sigma * np.random.randn(), sigma * np.random.randn(), sigma * np.random.randn(), sigma * np.random.randn(), sigma * np.random.randn(), sigma * np.random.randn(), sigma * np.random.randn(), sigma * np.random.randn(), sigma * np.random.randn(), sigma * np.random.randn(), sigma * np.random.randn(), sigma * np.random.randn(), sigma * np.random.randn(), sigma * np.random.randn(), sigma * np.random.randn(), sigma*np.random.randn()])
    y0_data = y_0

    t_1 = np.arange(0, T-delta_t, delta_t)
    y_data = []
    for t in t_1:
        A_1 = swing.solving_swing(t,delta_t,y0_data,u[:, k])
        y0_data = A_1
        y_data.append(A_1)
        k += 1
    U.append(np.reshape(np.fliplr(u), [m*round(T/delta_t)]))
    X_0.append(y_0)
    X_1T.append(np.reshape(np.fliplr(y_data[0:round(T/delta_t-1)]), [n*round(T/delta_t-1)]))
    X_T.append(y_data[-1])

# Compute data-driven control.

U = np.array(U[0:7])
U = U.T

X_0 = np.array(X_0[0:7])
X_0 = X_0.T

X_1T = np.array(X_1T[0:7])
X_1T = X_1T.T

X_T = np.array(X_T[0:7])
X_T = X_T.T

K_X0 = custom_matlab_functions.null(X_0, 1e-10)
K_U = custom_matlab_functions.null(U, 1e-10)

xf_c = xf - np.dot(X_T, np.dot(K_U, np.dot(np.linalg.pinv(np.dot(X_0 , K_U), 1e-10), x_0)))

U = np.dot(U, K_X0)
X_1T = np.dot(X_1T, K_X0)
X_T = np.dot(X_T, K_X0)

K_U = custom_matlab_functions.null(U, 1e-10)
K_XT = custom_matlab_functions.null(X_T, 1e-10)

Q = 5e-3
R = 1
X_1T = np.array(X_1T)
L2 = Q * np.dot(X_1T.T , X_1T) + R * np.dot(U.T , U)
L = scipy.linalg.cholesky(L2)
[W,S,V] = custom_matlab_functions.svds(np.dot(L , K_XT) , m * round(T/delta_t) - n)
u_opt = np.dot(U , np.dot(np.linalg.pinv(X_T,1e-10) , xf_c)) - np.dot(U , np.dot(K_XT , np.dot(np.linalg.pinv(np.dot(W , np.dot(S , V)),1e-10) , np.dot(L , np.dot(np.linalg.pinv(X_T,1e-10) , xf_c)))))
u_opt = np.fliplr(np.reshape(u_opt,[m,round(T/delta_t)]))

# Apply control for fault recovery.
u_opt_seq = np.zeros((9,round(t_c/delta_t+1)))
A = np.shape(u_opt_seq)
u_opt_seq = np.insert(u_opt_seq, [A[1]], u_opt, axis = 1)
A = np.shape(u_opt_seq)
u_opt_seq = np.insert(u_opt_seq, [A[1]], np.zeros((9,round(500/delta_t))), axis = 1)

y_0 = np.zeros(18)
k = 0
tspan = np.arange(0, 500, delta_t)
yy = []
for t in tspan:
    A_1 = swing.solving_swing(t,delta_t,y_0,u_opt_seq[:, k])
    yy.append(A_1)
    y_0 = A_1
    k += 1
yy = np.array(yy)

# Plot results.
plt.style.use('seaborn')
fig, ax_2 = plt.subplots()
ax_2.plot(np.arange(0, T_sim, delta_t), yy[0:round(T_sim/delta_t), 0], color='red', label = "gen 10")
ax_2.plot(np.arange(0, T_sim, delta_t), yy[0:round(T_sim/delta_t), 1], color='blue', label = "gen 2")
ax_2.plot(np.arange(0, T_sim, delta_t), yy[0:round(T_sim/delta_t), 2], color='green', label = "gen 3")
ax_2.plot(np.arange(0, T_sim, delta_t), yy[0:round(T_sim/delta_t), 3], color='yellow', label = "gen 4")
ax_2.plot(np.arange(0, T_sim, delta_t), yy[0:round(T_sim/delta_t), 4], color='cyan', label = "gen 5")
ax_2.plot(np.arange(0, T_sim, delta_t), yy[0:round(T_sim/delta_t), 5], color='magenta', label = "gen 6")
ax_2.plot(np.arange(0, T_sim, delta_t), yy[0:round(T_sim/delta_t), 6], color='black', label = "gen 7")
ax_2.plot(np.arange(0, T_sim, delta_t), yy[0:round(T_sim/delta_t), 7], color='hotpink', label = "gen 8")
ax_2.plot(np.arange(0, T_sim, delta_t), yy[0:round(T_sim/delta_t), 8], color='darkviolet', label = "gen 9")
ax_2.fill_between([T_fault_in, T_fault_in, T_fault_end, T_fault_end], [-10, 15, 15, -10], -10, facecolor='red', alpha=0.2)
ax_2.fill_between([t_c, t_c, t_c+T, t_c+T], [-10, 15, 15, -10], -10, facecolor='green', alpha=0.2)
plt.legend(loc="upper left")

# Format Results' plot. 
ax_2.set_title('Results', fontsize=20)
ax_2.set_xlabel('Time(sec)', fontsize=14)
ax_2.set_ylabel('Phase', fontsize=14)

# Plot results.
plt.style.use('seaborn')
fig, ax_3 = plt.subplots()
ax_3.plot(np.arange(0, T_sim, delta_t), yy[0:round(T_sim/delta_t), 9], color='red', label = "gen 10")
ax_3.plot(np.arange(0, T_sim, delta_t), yy[0:round(T_sim/delta_t), 10], color='blue', label = "gen 2")
ax_3.plot(np.arange(0, T_sim, delta_t), yy[0:round(T_sim/delta_t), 11], color='green', label = "gen 3")
ax_3.plot(np.arange(0, T_sim, delta_t), yy[0:round(T_sim/delta_t), 12], color='yellow', label = "gen 4")
ax_3.plot(np.arange(0, T_sim, delta_t), yy[0:round(T_sim/delta_t), 13], color='cyan', label = "gen 5")
ax_3.plot(np.arange(0, T_sim, delta_t), yy[0:round(T_sim/delta_t), 14], color='magenta', label = "gen 6")
ax_3.plot(np.arange(0, T_sim, delta_t), yy[0:round(T_sim/delta_t), 15], color='black', label = "gen 7")
ax_3.plot(np.arange(0, T_sim, delta_t), yy[0:round(T_sim/delta_t), 16], color='hotpink', label = "gen 8")
ax_3.plot(np.arange(0, T_sim, delta_t), yy[0:round(T_sim/delta_t), 17], color='darkviolet', label = "gen 9")
ax_3.fill_between([T_fault_in, T_fault_in, T_fault_end, T_fault_end], [-10, 15, 15, -10], -10, facecolor='red', alpha=0.2)
ax_3.fill_between([t_c, t_c, t_c+T, t_c+T], [-10, 15, 15, -10], -10, facecolor='green', alpha=0.2)
plt.legend(loc="upper left")

# Format Results' plot. 
ax_3.set_title('Results', fontsize=20)
ax_3.set_xlabel('Time(sec)', fontsize=14)
ax_3.set_ylabel('Frequency', fontsize=14)

# Asymptotic behavior.
plt.style.use('seaborn')
fig, ax_4 = plt.subplots()
ax_4.plot(tspan, yy[:, 0], color='red', label = "gen 10")
ax_4.plot(tspan, yy[:, 1], color='blue', label = "gen 2")
ax_4.plot(tspan, yy[:, 2], color='green', label = "gen 3")
ax_4.plot(tspan, yy[:, 3], color='yellow', label = "gen 4")
ax_4.plot(tspan, yy[:, 4], color='cyan', label = "gen 5")
ax_4.plot(tspan, yy[:, 5], color='magenta', label = "gen 6")
ax_4.plot(tspan, yy[:, 6], color='black', label = "gen 7")
ax_4.plot(tspan, yy[:, 7], color='hotpink', label = "gen 8")
ax_4.plot(tspan, yy[:, 8], color='darkviolet', label = "gen 9")
ax_4.fill_between([2, 2, 2.4, 2.4], [-10, 15, 15, -10], -10, facecolor='red', alpha=0.2)
ax_4.fill_between([t_c, t_c, t_c+T, t_c+T], [-10, 15, 15, -10], -10, facecolor='green', alpha=0.2)
plt.legend(loc="upper left")

# Format Asymptotic behavior's plot. 
ax_4.set_title('Asymptotic behavior', fontsize=20)
ax_4.set_xlabel('Time(sec)', fontsize=14)
ax_4.set_ylabel('Phase', fontsize=14)

# Asymptotic behavior.
plt.style.use('seaborn')
fig, ax_5 = plt.subplots()
ax_5.plot(tspan, yy[:, 9], color='red', label = "gen 10")
ax_5.plot(tspan, yy[:, 10], color='blue', label = "gen 2")
ax_5.plot(tspan, yy[:, 11], color='green', label = "gen 3")
ax_5.plot(tspan, yy[:, 12], color='yellow', label = "gen 4")
ax_5.plot(tspan, yy[:, 13], color='cyan', label = "gen 5")
ax_5.plot(tspan, yy[:, 14], color='magenta', label = "gen 6")
ax_5.plot(tspan, yy[:, 15], color='black', label = "gen 7")
ax_5.plot(tspan, yy[:, 16], color='hotpink', label = "gen 8")
ax_5.plot(tspan, yy[:, 17], color='darkviolet', label = "gen 9")
ax_5.fill_between([2, 2, 2.4, 2.4], [-10, 15, 15, -10], -10, facecolor='red', alpha=0.2)
ax_5.fill_between([t_c, t_c, t_c+T, t_c+T], [-10, 15, 15, -10], -10, facecolor='green', alpha=0.2)
plt.legend(loc="upper left")

# Format Asymptotic behavior's plot. 
ax_5.set_title('Asymptotic behavior', fontsize=20)
ax_5.set_xlabel('Time(sec)', fontsize=14)
ax_5.set_ylabel('Frequency', fontsize=14)

plt.show()
