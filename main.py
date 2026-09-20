from geometry import Sphere, Rectangle
from camera_screen import Screen, Camera
import scene

cool_screen = Screen(640, 480, 1.0, 1)

# scene.objects.append(Sphere((2, -1, -10), 2, (255, 100, 0), 0, 0 , 0))
scene.objects.append(Sphere((0, 0, -25), 2, (255, 255, 255), 0, 1, 0))
scene.objects.append(Sphere((5, 5, -10), 3, (255, 10, 255), 0.4, 0.5, 0))
scene.objects.append(Rectangle((-5, 4, -8), (0, 0, -3), (0, -5, 0), (50, 255, 50), 0.7, 0, 0))
scene.objects.append(Rectangle((-4, -5, -1), (0, 0, -100), (50, 0, 0), (254, 200, 50), 0.5, 0.3, 0))

camera = Camera(cool_screen)
camera.take_picture()