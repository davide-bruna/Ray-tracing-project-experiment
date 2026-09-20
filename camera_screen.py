from math_utils import ray_tracer, scalar_V_product
from math import atan, degrees


class Screen:
    def __init__(self, x_res, y_res, y_size, distance):
        self.x_res = x_res
        self.y_res = y_res
        self.y_size = y_size
        self.x_size = y_size * (x_res / y_res)
        print("This camera has a screen size of ", self.x_size, "x", self.y_size)
        print("The FOV is: ", degrees(2 * atan(0.5 * y_size / distance)))
        self.distance = distance
        self.pixel_size = y_size / y_res


class Camera:
    def __init__(self, screen):
        self.screen = screen

    def take_picture(self):
        print("Taking the picture of your scene...")
        with open("picture.ppm", "wb") as f:
            f.write(b"P6\n")
            f.write(f"{self.screen.x_res} {self.screen.y_res}\n".encode("ascii"))
            f.write(b"255\n")
            for row in range(self.screen.y_res):
                for col in range(self.screen.x_res):
                    f.write(bytes(self.get_pixel(row, col)))
        print("Picture taken, check out the camera roll")

    def get_pixel(self, row, col):
        camera_vector = self.get_camera_vector(row, col)
        returned_ray = ray_tracer(camera_vector, (0, 0, 0))
        return (int(value) for value in scalar_V_product(255, returned_ray))

    def get_camera_vector(self, row, col):
        vector = ((self.screen.pixel_size * col + self.screen.pixel_size / 2 - self.screen.x_size / 2),
                  (-self.screen.pixel_size * row - self.screen.pixel_size / 2 + self.screen.y_size / 2),
                  -self.screen.distance)
        return vector
