import turtle    

counter = 0
num_sides = 0  

#class Fractal:
#	def __init__(self, length): 

window = turtle.Screen()
window.bgcolor("orange")
alice = turtle.Turtle()
start_length=75

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
	alice.right(120)
	
	
def draw_inception(length1):	
	#draw_fractal(length1)
	#length1=length1/2
	draw_fractal(length1)
	alice.forward(length1)
	alice.right(120)
	draw_fractal(length1)
	alice.forward(length1)
	alice.left (60)
	alice.forward(length1*2)
	alice.left (60)
	draw_fractal(length1)

draw_inception(start_length)
start_length = start_length/2
draw_inception(start_length)
start_length = start_length/2
draw_inception(start_length)
start_length = start_length/2
draw_inception(start_length)
#start_length = start_length/2
#draw_inception(start_length)

#draw_fractal(start_length)

window.exitonclick()
	
