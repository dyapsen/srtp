import math
class PointInt:
	x: int
	y: int
	def __init__(self, x, y) -> None:
		x = round(x) if isinstance(x, float) else x
		y = round(y) if isinstance(y, float) else y
		self.x, self.y = int(x), int(y)
	
	def equal(self, p: 'PointInt') -> bool :
		return p.x == self.x and p.y == self.y 

	def slope(self, other: 'PointInt') -> float:
		if self.x == other.x:
			raise ValueError("分母为0，斜率为无穷大，请检查")
		else:
			return (self.y - other.y) / (self.x - other.x)

	def slope_y(self, other: 'PointInt') -> float:
		if self.y == other.y:
			raise ValueError("分母为0，斜率为无穷大，请检查")
		else:
			return (self.x - other.x) / (self.y - other.y)
	
	def copy(self) -> 'PointInt':
		return PointInt(self.x, self.y)

	def distance(self, other: 'PointInt') -> float:
		return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)

class PointFloat:
	x: float
	y: float
	def __init__(self, x, y) -> None:
		self.x, self.y = float(x), float(y)
	
	def slope(self, other: 'PointFloat') -> float:
		if self.x == other.x:
			raise ValueError("分母为0，斜率为无穷大，请检查")
		else:
			return (self.y - other.y) / (self.x - other.x)

	def slope_y(self, other: 'PointFloat') -> float:
		if self.y == other.y:
			raise ValueError("分母为0，斜率为无穷大，请检查")
		else:
			return (self.x - other.x) / (self.y - other.y)
	
	def copy(self) -> 'PointFloat':
		return PointFloat(self.x, self.y)
