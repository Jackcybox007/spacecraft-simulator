import math
import planet as pl

# constant
G = 6.6743e-11
R = 8.314       # universal gas constant in J/(mol K)
M = 0.0289644   # molar mass of dry air in kg/mol
g = 9.81        # acceleration due to gravity in m/s^2
T0 = 288.15     # temperature at sea level in K
p0 = 101325     # pressure at sea level in Pa
L = 0.0065      # temperature lapse rate in K/m


def gravity(alt, planet):
    g = G * pl.planet_mass[planet] / alt + pl.planet_radius[planet]
    return g


def distance(pos1, pos2):
    dist = math.sqrt((pos2["x"] + pos1["x"]) ** 2 + (pos2["y"] + pos1["y"]) ** 2)
    return dist


def calc_drag(altitude, v, Cd, A, planet):

    g = gravity(altitude, planet)

    T = T0 - L * altitude
    p = p0 * (1 - L * altitude / T0) ** (g * M / (R * L))
    rho = p / (R * T)

    return 0.5 * rho * v**2 * Cd * A


def calc_lift(altitude, V, Cl, A, planet):
    g = gravity(altitude, planet)

    T = T0 - L * altitude
    p = p0 * (1 - L * altitude / T0) ** (g * M / (R * L))
    rho = p / (R * T)

    return 0.5 * rho * V ^ 2 * A * Cl


def Thrust(Isp, m_dot, altitude, planet):
    g = gravity(altitude, planet)
    return Isp * m_dot * g


def angle(pos1, pos2):
    Angle = math.atan2(pos2["y"] - pos1["y"], pos2["x"] - pos1["x"])
    deg = math.degrees(Angle)
    return deg


def angleF(x,y):
    Angle = math.atan2(y,x)
    deg = math.degrees(Angle)
    return deg


def filp_angle(Angel):
    if Angel >= 180:
        Angel -= 180
    else:
        Angel += 180
    return Angel

