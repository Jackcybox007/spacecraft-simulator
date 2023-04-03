import numpy as np
import matplotlib.pyplot as plt

import equation as eq
import planet as pl

aerodynamic = {
    "drag_coeffition":  0.42,
    "lift_coeffition":  0.42,
    "frontal_area":     31.6,
    "angle_of_attack":  15,
}

engine = {
    "ISP":      0,
    "m_dot":    0
}


def derivetive(state):
    pos_x = state["pos_x"]
    pos_y = state["pos_y"]
    velocity = state["velocity"]
    theta = state["theta"]
    mass = state["mass"]

    cd = aerodynamic["drag_coeffition"]
    cl = aerodynamic["lift_coeffition"]
    A = aerodynamic["frontal_area"]
    alpha = aerodynamic["angle_of_attack"]

    ISP = engine["ISP"]
    m_dot = engine["m_dot"]

    distance = {}
    gravityF = 0

    # compute distance between all planet
    pos = {"x": pos_x, "y": pos_y}

    for planet_name in pl.planet:
        distance[planet_name] = eq.distance(pos, pl.planet_pos[planet_name]) - pl.planet_radius[planet_name]

    # sorting nearest planet
    Distance = dict(sorted(distance.items(), key=lambda x: x[1]))

    # compute all Force
    # gravity (force)
    for planet_name, alt in Distance.items():
        gravityF += - eq.gravity(alt, planet_name)

    nearest = next(iter(Distance))
    alt = Distance[nearest] - pl.planet_radius[nearest]

    # gravity (angle)
    angle = eq.angle(pos, pl.planet_pos[nearest])

    # aerodynamics (Force)
    aero = eq.calc_drag(alt, velocity, cd, A, nearest)
    if aerodynamic["wing"]:
        aero += eq.calc_lift(alt, velocity, cl, A, nearest)

    # aerodynamics (angle)
    angle += eq.filp_angle(theta)
    angle += theta - (alpha + 90)

    # thrust
    Thrust = eq.Thrust(ISP, m_dot, alt, nearest)

    Force = gravityF + aero + Thrust

    accel = Force / mass


