from sympy import *
from sympy import Rational as RR
vz=symbols('U_\text{з}')
vg=symbols('U_\text{г}')
R0=symbols('R_0')
R=symbols('R')
rho=symbols('\rho')
C=symbols('C')
E=symbols('\mathcal{E}')
tau2=symbols('\tau_2')
v0=symbols('U_0')

tau2=rho*C*ln(((vz-v0)*R+(vz-E)*R0)/((vg-v0)*R+(vg-E)*R0))
