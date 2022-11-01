import math

#################
# Målte Størrelser
M1 = 1502.5E-3 # Masse blykule 1
M2 = 1507.8E-3 # Masse blykule 2
glass_stor_blykule_1 = 3E-3 # Avstand fra glass - stor blykule1
glass_stor_blykule_2 = 1E-3 # Avstand fra glass - stor blykule1
kammer_bredde = 3E-2 # Bredde på kammer
glass_liten_blykule = kammer_bredde / 2 # Avstand fra glass - liten blykule
d_kammer_meterstav = 210.5E-2 # Avstand fra speil - meterstav
Diameter_blykule = 6E-2  # Diameter til stor blykule

# Svinginger 1
S1=		3.828001e-1 # mm
S2 =	3.411847e-1 # mm
T1=		5.831662e+02 # s
T2=		6.092171e+02 # s

dS1=	3.998454e-04 # mm
dS2=	3.995166e-04  # mm

# Avledede størrelser
S = abs(S1-S2)
M = (M1+M2) / 2
L = d_kammer_meterstav + glass_liten_blykule
T = (T1 + T2) / 2
b = glass_liten_blykule + Diameter_blykule / 2 + (glass_stor_blykule_1 + glass_stor_blykule_2) / 2
r = 100.0E-3 / 2
ds = math.sqrt(dS1**2+dS2**2)
dM = abs(M1-M2) / 2
dT = abs(T1-T2) / 2
db = math.sqrt((0.25E-2)**2 + (0.05E-2)**2 + (abs(glass_stor_blykule_1 - glass_stor_blykule_2) / 2)**2)
db = math.sqrt((0.25E-2)**2 + (0.05E-2)**2 + (0.1E-3 / 2 + 0.1E-3 / 2)**2)
dr = 0.05E-3
dL = math.sqrt(0.5E-2**2 + 0.05E-2**2)

beta = b**3/(b**2+4*r**2)**(3/2)





def G(S, b, r, T, L, M):
    return math.pi**2 / (1-beta) * S * b**2 * r / (T**2 * L * M)

usikkerhet = math.sqrt((ds/S)**2 + (2*db/b)**2 + (dr/r)**2 + (2*dT/T)**2 + (dM/M)**2 + (dL/L)**2)

print(G(S, b, r, T, L, M))
print(usikkerhet)