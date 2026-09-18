import math
import sys
import scene


def dot_product(V, T):
    return V[0] * T[0] + V[1] * T[1] + V[2] * T[2]


def cross_product(V, T):
    return V[1] * T[2] - V[2] * T[1], V[2] * T[0] - V[0] * T[2], V[0] * T[1] - V[1] * T[0]


def scalar_V_product(s, V):
    return s * V[0], s * V[1], s * V[2]


def sum_vectors(V, T):
    return tuple(map(sum, zip(V, T)))


def sub_vectors(V, T):
    T = tuple(-x for x in T)
    return sum_vectors(V, T)


def magnitude_vector(V):
    return math.sqrt(V[0] ** 2 + V[1] ** 2 + V[2] ** 2)


def normalize_vector(V):
    magnitude = magnitude_vector(V)
    if magnitude == 0:
        return 0.0, 0.0, 0.0
    return V[0] / magnitude, V[1] / magnitude, V[2] / magnitude


def closest_collision(V, coords):
    normalized_V = normalize_vector(V)
    closest_point = sys.float_info.max
    found = False
    for obj in scene.objects:
        current_collision = obj.collision(normalized_V, coords)

        if current_collision == None: continue

        current_distance = magnitude_vector(sub_vectors(coords, current_collision))
        if closest_point > current_distance:
            closest_point = current_distance
            closest_collision = current_collision
            closest_obj = obj
            found = True
    if found:
        return closest_collision, closest_obj, closest_point
    else:
        return None, None, None
