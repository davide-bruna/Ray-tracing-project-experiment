from math_utils import closest_collision


class Screen:
    def __init__(self, x_res, y_res, y_size, distance):
        self.x_res = x_res
        self.y_res = y_res
        self.y_size = y_size
        self.x_size = y_size * (x_res / y_res)
        print(self.x_size, self.y_size)
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
