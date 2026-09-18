from geometry import Sphere, Rectangle
from camera_screen import Screen, Camera
import scene

cool_screen = Screen(640, 480, 1.0, 1)

scene.objects.append(Sphere((2, -1, -10), 2, (255, 100, 0), 0, 0))
scene.objects.append(Sphere((0, 0, -15), 2, (255, 255, 255), 0, 0))
scene.objects.append(Sphere((10, 5, -15), 3, (255, 10, 255), 0, 0))
scene.objects.append(Rectangle((-5, 4, -8), (0, 0, -3), (0, -5, 0), (50, 255, 50), 0, 0))
scene.objects.append(Rectangle((-5, -2, -8), (0, 0, -8), (8, 0, 0), (50, 10, 50), 0, 0))

camera = Camera(cool_screen)
camera.take_picture()