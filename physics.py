import pyglet.math as math

GRAVITY_CONST = 1

FRICTION = 0.02

class physicsObject():
	def __init__(self, position: math.Vec2, top_speed):
		self.position = position
		self._velocity = math.Vec2(0, 0)
		self.top_speed = top_speed
		self.colliding = False

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

	def set_velocity(self, vel: math.Vec2):
		self._velocity = vel
	
	def get_velocity(self):
		return self._velocity.x

def update_objects(phys_list):
	for obj in phys_list:
		#obj._velocity -= math.Vec2(0, GRAVITY_CONST)
		obj.position += obj._velocity
		obj.sprite.center_x = obj.position.x
		obj.sprite.center_y = obj.position.y
		# friction
		if obj._velocity.x > 0.0:
			obj._velocity -= math.Vec2(FRICTION, 0)
		elif obj._velocity.x < 0.0:
			obj._velocity += math.Vec2(FRICTION, 0)

def collision_object(sprite1, sprite2):
