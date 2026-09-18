from math_utils import *


class Sphere:
    def __init__(self, coordinates, ray, color, refl, light):
        self.coordinates = coordinates
        self.ray = ray
        self.color = color
        self.refl = refl
        self.light = light

    # O+cD= P
    # C+ru= P
    def collision(self, D, O):
        C = self.coordinates  # a little bit more readable
        existence = dot_product(D, sub_vectors(O, C)) ** 2 - magnitude_vector(sub_vectors(O, C)) ** 2 + self.ray ** 2
        if existence < 0:
            return None
        return min([sum_vectors(O, scalar_V_product(-dot_product(D, sub_vectors(O, C)) + math.sqrt(existence), D)),
                    sum_vectors(O, scalar_V_product(-dot_product(D, sub_vectors(O, C)) - math.sqrt(existence), D))],
                   key=lambda x: magnitude_vector(sub_vectors(x, O)))


class Rectangle:
    def __init__(self, vertex, width_vector, height_vector, color, refl, light):
        self.vertex = vertex
        self.width_vector = width_vector
        self.height_vector = height_vector
        self.color = color
        self.refl = refl
        self.light = light
        # N is the normal vector
        self.N = normalize_vector(cross_product(self.height_vector, self.width_vector))

    def collision(self, D, O):
        # the line is O+tD

        inside_plane = dot_product(self.N, sub_vectors(self.vertex, O))
        if inside_plane == 0: return None  # if the light hits parallel to a rectangle I assume it goes through it
        parallel_to_plane = dot_product(self.N, D)
        if parallel_to_plane == 0: return None
        t = inside_plane / parallel_to_plane
        intesection_with_plane = sum_vectors(scalar_V_product(t, D), O)
        # now I check if the intersection with plane is IN the rectangle
        # I create a vector from vertex to intersection
        V1 = sub_vectors(intesection_with_plane, self.vertex)

        # projection of V1 on width and height vectors
        dW = dot_product(V1, self.width_vector)
        dH = dot_product(V1, self.height_vector)
        if 0 <= dH <= dot_product(self.height_vector, self.height_vector) and 0 <= dW <= dot_product(self.width_vector,
                                                                                                     self.width_vector):
            return V1
        else:
            return None
