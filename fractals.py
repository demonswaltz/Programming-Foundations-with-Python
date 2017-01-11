import turtle    

counter = 0
num_sides = 0  

#class Fractal:
#	def __init__(self, length): 

window = turtle.Screen()
window.bgcolor("orange")
alice = turtle.Turtle()
length1= 100
def draw_triangle(side_len):
	for i in range (1, 4):
		alice.forward(side_len)
		alice.left(120)	

		
def draw_fractal(side_len):
	draw_triangle(side_len)
	alice.forward(side_len)
	draw_triangle(side_len)
	alice.left(120)
	alice.forward(side_len)
	alice.right(120)
	draw_triangle(side_len)
	side_len = side_len/2
	return side_len
	
	

length1 = draw_fractal(length1)
length1 = draw_fractal(length1)
length1 = draw_fractal(length1)


window.exitonclick()
	
