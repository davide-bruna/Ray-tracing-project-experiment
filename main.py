from geometry import Sphere, Rectangle
from camera_screen import Screen, Camera
import scene

cool_screen = Screen(1024, 768, 2.0, 3)
# light bulb
scene.objects.append(Sphere((-3, 0, -21), 1, (255, 255, 255), 0, 1, 0))
# red left wall
scene.objects.append(Rectangle((-6, -5, -25), (0, 0, 8), (0, 10, 0), (200, 10, 70), 0.5, 0, 0.2))
# green back wall
scene.objects.append(Rectangle((-6, -5, -25), (0, 10, 0), (14, 0, 0), (100, 200, 50), 0.6, 0, 0.2))
# blue floor
scene.objects.append(Rectangle((-6, -5, -25), (0, 0, 8), (14, 0, 0), (254, 200, 50), 0.6, 0, 0.2))

# highly reflective sphere
scene.objects.append(Sphere((5, 3, -15), 2, (255, 10, 255), 0.7, 0.5, 0))
# another light bulb
scene.objects.append(Sphere((3, -2, -13), 1, (80, 255, 255), 0.1, 1, 0))
camera = Camera(cool_screen)
camera.take_picture()