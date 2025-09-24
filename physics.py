import numpy as np
import pyglet.math

GRAVITY_CONST = 9.807

FRICTION = 0.02 #ice

class physicsObject():
	def __init__(self, x, y, top_speed):
		self.position = pyglet.math.Vec2(x, y)
		self._velocity = pyglet.math.Vec2(0, 0)
		self.top_speed = top_speed

	# already implemented in pyglet.math	
	# def rotate(coord, target_angle):
	# 	theta = np.radians(target_angle)
	# 	rotation = np.array((
	# 				(np.cos(theta), -np.sin(theta)), 
	# 				(np.sin(theta), np.cos(theta))
	# 				))
	# 	# x' = x * cos(theta) + y * -sin(theta)
	# 	coord[0] = coord[0] * rotation[0][0] + coord[1] * rotation[0][1]
	# 	# y' = x * sin(theta) + y * cos(theta)
	# 	coord[1] = coord[0] * rotation[1][0] + coord[1] * rotation[1][1]
		
	# 	return(coord[0], coord[1])

	# magnitude (length) & direction
	def accel(self, accelRate):
		if self._velocity.x < self.top_speed : self._velocity += accelRate

def update_objects(phys_list):
	for obj in phys_list:
		#obj._velocity -= pyglet.math.Vec2(0, GRAVITY_CONST)
		obj.position += obj._velocity
		obj.sprite.center_x = obj.position.x
		obj.sprite.center_y = obj.position.y