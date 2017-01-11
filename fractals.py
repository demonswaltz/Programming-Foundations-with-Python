import turtle    

counter = 0
num_sides = 0  

window = turtle.Screen()
window.bgcolor("orange")
alice = turtle.Turtle()
def draw_triangle(side_len):
	for i in range (1, 4):
		alice.forward(side_len)
		alice.left(120)	

		
def draw_fractal(side_len):
	alice.shape("turtle")
	alice.color("blue")
	alice.speed(5)
	draw_triangle(side_len)
	side_len = side_len/2
	alice.forward(side_len)
	alice.left(60)
	draw_triangle(side_len)
	side_len = side_len/2
	alice.forward(side_len)
	alice.right(120)
	draw_triangle(side_len)

#draw_square(100)
#draw_circle(100)

draw_fractal(200)



window.exitonclick()
	
