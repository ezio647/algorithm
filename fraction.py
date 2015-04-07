class fraction:
	def __init__(self, top, bottom):
		self.num = top
		self.den = bottom


		"""
		try:
			if isinstance(top, int) and isinstance(bottom, int):
				self.num = top
				self.den = bottom
			#else:
			#	raise RuntimeError("You can't use floats")

		except:
			RuntimeError("You can't use floats")
"""
	def show(self):
		print self.num, '/' , self.den

	def __str__(self):
		return str(self.num) + '/' + str(self.den)

	def __add__(self, other):
		sum_num = self.num * other.den + self.den * other.num
		sum_den = self.den * other.den
		common = gcd(sum_num, sum_den)
		return fraction(sum_num // common, sum_den //common)

	def __eq__(self, other):
		f = self.num * other.den
		s = other.num * self.den
		return f == s

	def get_num(self):
		return int(self.num)


def gcd(m, n):
	while m % n != 0:
		old_m  = m
		old_n = n
		m = old_n
		n = old_m % old_n
	return n

my_f = fraction(3, 5)
print my_f
my_f.show()

f1 = fraction(1.0, 4)
f2 = fraction(1, 2)
f3 = f1 + f2
print f3
print (f1 == f2)
print "num = ",f1.get_num()