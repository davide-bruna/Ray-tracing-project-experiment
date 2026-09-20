from math_utils import *


# collision functions return the point of collision and the direction of the bounce

class Sphere:
    def __init__(self, coordinates, ray, color, refl=0.3, light=0, roughness=0.1):
        self.coordinates = coordinates
        self.ray = ray
        self.color = scalar_V_product(1 / 255, color)
        self.refl = refl
        self.light = light
        self.roughness = roughness

    # C+ru= P
    def collision(self, D, O):
        C = self.coordinates  # a little bit more readable
        existence = dot_product(D, sub_vectors(O, C)) ** 2 - magnitude_vector(sub_vectors(O, C)) ** 2 + self.ray ** 2
        if existence < 0:
            return None, None
        t_plus = -dot_product(D, sub_vectors(O, C)) + math.sqrt(existence)
        t_minus = -dot_product(D, sub_vectors(O, C)) - math.sqrt(existence)

        # O+tD= P
        # it only accepts rays that go forwards (t_minus is always smaller than t plus, so if t_plus is negative they are both negative)
        if t_minus > 0 and t_plus > 0:
            collision_point = min([sum_vectors(O, scalar_V_product(t_plus, D)),
                                   sum_vectors(O, scalar_V_product(t_minus, D))],
                                  key=lambda x: magnitude_vector(sub_vectors(x, O)))
        elif t_plus > 0:
            collision_point = sum_vectors(O, scalar_V_product(t_plus, D))
        else:
            return None, None

        # now I found a point on the surface on the sphere that words, I need to find the direction of the bounce
        # Normal of surface of the sphere on that point
        sphere_normal = normalize_vector(sub_vectors(collision_point, C))
        reflected_vector = sub_vectors(D, scalar_V_product(2 * dot_product(D, sphere_normal), sphere_normal))
        return collision_point, reflected_vector


class Rectangle:
    def __init__(self, vertex, width_vector, height_vector, color, refl=0.3, light=0, roughness=0.1):
        self.vertex = vertex
        self.width_vector = width_vector
        self.height_vector = height_vector
        self.color = scalar_V_product(1 / 255, color)
        self.refl = refl
        self.light = light
        self.roughness = roughness

    def collision(self, D, O):
        # N is the normal vector
        N = normalize_vector(cross_product(self.height_vector, self.width_vector))
        if dot_product(D,
                       N) > 0:  # adjusting the normal in case the line comes from behind (makes sure reflection works correctly)
            N = sub_vectors((0, 0, 0),N)

        # the line is O+tD
        inside_plane = dot_product(N, sub_vectors(self.vertex, O))
        if inside_plane == 0: return None, None  # if the light hits parallel to a rectangle I assume it goes through it
        parallel_to_plane = dot_product(N, D)
        if parallel_to_plane == 0: return None,None
        t = inside_plane / parallel_to_plane
        if t <= 0: return None, None  # the light can only go forward
        intersection_with_plane = sum_vectors(scalar_V_product(t, D), O)
        # now I check if the intersection with plane is IN the rectangle
        # I create a vector from vertex to intersection
        relative_intersection = sub_vectors(intersection_with_plane, self.vertex)

        # projection of the collision point on width and height vectors
        dW = dot_product(relative_intersection, self.width_vector)
        dH = dot_product(relative_intersection, self.height_vector)
        if 0 <= dH <= dot_product(self.height_vector, self.height_vector) and 0 <= dW <= dot_product(self.width_vector,
                                                                                                     self.width_vector):
            reflected_vector = sub_vectors(D, scalar_V_product(2 * dot_product(D, N), N))
            return intersection_with_plane, reflected_vector
        else:
            return None,None
