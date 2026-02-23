# threedfigures.py
import math

# ---------------- CUBE ----------------
def cube_surface_area(a):
    return 6 * a * a

def cube_volume(a):
    return a ** 3


# ---------------- CUBOID ----------------
def cuboid_surface_area(l, b, h):
    return 2 * (l*b + b*h + l*h)

def cuboid_volume(l, b, h):
    return l * b * h


# ---------------- CYLINDER ----------------
def cylinder_curved_surface_area(r, h):
    return 2 * math.pi * r * h

def cylinder_total_surface_area(r, h):
    return 2 * math.pi * r * (r + h)

def cylinder_volume(r, h):
    return math.pi * r * r * h


# ---------------- CONE ----------------
def cone_curved_surface_area(r, l):
    return math.pi * r * l

def cone_total_surface_area(r, l):
    return math.pi * r * (r + l)

def cone_volume(r, h):
    return (1/3) * math.pi * r * r * h


# ---------------- SPHERE ----------------
def sphere_surface_area(r):
    return 4 * math.pi * r * r

def sphere_volume(r):
    return (4/3) * math.pi * r ** 3


# ---------------- HEMISPHERE ----------------
def hemisphere_curved_surface_area(r):
    return 2 * math.pi * r * r

def hemisphere_total_surface_area(r):
    return 3 * math.pi * r * r

def hemisphere_volume(r):
    return (2/3) * math.pi * r ** 3