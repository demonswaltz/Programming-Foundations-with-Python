import turtle    

counter = 0
num_sides = 0  

 

window = turtle.Screen()
window.bgcolor("orange")
alice = turtle.Turtle()
alice.up()
alice.setposition(-100,-100)
alice.down()
alice.shape("turtle")
alice.right(180)
start_length= 30
side= start_length

def draw_triangle_down(side_len):
	for i in range (1, 4):
		alice.forward(side_len)
		alice.left(120)	
def draw_triangle_up(side_len):
	for i in range (1, 4):
		alice.forward(side_len)
		alice.right(120)	
		
def draw_fractal(side_len):
	draw_triangle_up(side_len*2)
	alice.forward(side_len)
	alice.right(120)
	draw_triangle_down(side_len)	
	
def draw_inception(length1):	
	draw_fractal(length1)
	alice.forward(length1)
	alice.right(120)
	alice.forward(length1)
	alice.left(120)
	draw_fractal(length1)
	alice.left(120)
	alice.forward(length1)
	alice.left(120)
	draw_fractal(length1)
	
	
	


draw_inception(side)
alice.right(60)
alice.forward(side)
alice.right(60)
alice.forward(side*2)
alice.left(60)
alice.forward(side*2)
alice.left(180)
draw_inception(side)
alice.left(60)
alice.forward(side)
alice.right(60)
alice.forward(side)
alice.left(120)
alice.forward(side*2)
draw_inception(side)


window.exitonclick()
	
