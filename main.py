import math
import sys


def dot_product(V, T):
    return V[0] * T[0] + V[1] * T[1] + V[2] * T[2]


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
    for obj in objects:
        current_collision = obj.collision(normalized_V, coords)

        if current_collision == (0, 0, 0): continue

        current_distance = magnitude_vector(sub_vectors(coords, current_collision))
        if closest_point > current_distance:
            closest_point = current_distance
            closest_collision = current_collision
            closest_obj = obj
            found = True
    if found:
        return closest_collision, closest_obj
    else:
        return (0, 0, 0), None


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
            return 0, 0, 0
        return min([sum_vectors(O, scalar_V_product(-dot_product(D, sub_vectors(O, C)) + math.sqrt(existence), D)),
                    sum_vectors(O, scalar_V_product(-dot_product(D, sub_vectors(O, C)) - math.sqrt(existence), D))],
                   key=lambda x: magnitude_vector(sub_vectors(x, O)))


class Screen:
    def __init__(self, x_res, y_res, y_size, distance):
        self.x_res = x_res
        self.y_res = y_res
        self.y_size = y_size
        self.x_size = int(y_size * (x_res / y_res))
        self.distance = distance
        self.pixel_size = y_size / y_res


class Camera:
    def __init__(self, screen):
        self.screen = screen

    def take_picture(self):
        with open("picture.ppm", "wb") as f:
            f.write(b"P6\n")
            f.write(f"{self.screen.x_res} {self.screen.y_res}\n".encode("ascii"))
            f.write(b"255\n")
            for row in range(self.screen.y_res):
                for col in range(self.screen.x_res):
                    f.write(bytes(self.get_pixel(row, col)))

    def get_pixel(self, row, col):
        camera_vector = self.get_camera_vector(row, col)
        returned_ray = closest_collision(camera_vector, (0, 0, 0))
        if returned_ray[1] != None:
            return returned_ray[1].color
        else:
            return 0, 0, 0

    def get_camera_vector(self, row, col):
        vector = ((self.screen.pixel_size * col + self.screen.pixel_size / 2 - self.screen.x_size / 2),
                  (-self.screen.pixel_size * row - self.screen.pixel_size / 2 + self.screen.y_size / 2),
                  -self.screen.distance)
        return vector


cool_screen = Screen(640, 480, 3, 3)
print(cool_screen.x_size, cool_screen.y_size)
objects = [Sphere((2, -1, -10), 2, (255, 100, 0), 0, 0), Sphere((0, 0, -15), 2, (255, 255, 255), 0, 0),
           Sphere((10, 5, -15), 3, (255, 10, 255), 0, 0)]
camera = Camera(cool_screen)
camera.take_picture()
