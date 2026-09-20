import math
import sys
import scene


def dot_product(V, T):
    return V[0] * T[0] + V[1] * T[1] + V[2] * T[2]


def cross_product(V, T):
    return V[1] * T[2] - V[2] * T[1], V[2] * T[0] - V[0] * T[2], V[0] * T[1] - V[1] * T[0]


def scalar_V_product(s, V):
    return float(s) * V[0], float(s) * V[1], float(s) * V[2]


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


def ray_tracer(V, coords, depth=0, last_obj=None):
    if depth > 5 or (depth > 0 and last_obj.light > 0.7):
        return scalar_V_product(1.0 - last_obj.refl, scalar_V_product(min(1, last_obj.light + 0.15), last_obj.color))
    normalized_V = normalize_vector(V)
    closest_point = sys.float_info.max
    found = False
    for obj in scene.objects:
        # skip the object we are reflecting from
        if depth != 0 and last_obj == obj:
            continue

        current_collision = obj.collision(normalized_V, coords)
        if current_collision[0] is None:
            continue  # this one means that the object is not in the way of the ray, so skip

        current_distance = magnitude_vector(sub_vectors(coords, current_collision[0]))
        if closest_point > current_distance:
            closest_point = current_distance
            closest_collision = current_collision
            closest_obj = obj
            found = True
    if found:
        final_color = sum_vectors(
            scalar_V_product(1.0 - closest_obj.refl,
                             scalar_V_product(min(1, closest_obj.light + 0.15), closest_obj.color)),
            scalar_V_product(closest_obj.refl,
                             ray_tracer(closest_collision[1], closest_collision[0], depth + 1, closest_obj))
        )
        return final_color
    else:
        return 0, 0, 0
