import turtle    

counter = 0
num_sides = 0  

 

window = turtle.Screen()
window.bgcolor("orange")
alice = turtle.Turtle()
alice.up()
alice.setposition(100,-100)
alice.down()
alice.shape("turtle")

start_length= input ('Set starting side length:')
side= start_length

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
