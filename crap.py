import turtle    

counter = 0
num_sides = 0  

window = turtle.Screen()
window.bgcolor("orange")
	
def draw_square(side_len):	
	counter = 0
	num_sides = 4
	
	gary = turtle.Turtle()
	gary.shape("turtle")
	gary.color("green")
	gary.speed(2)
	
	while counter < num_sides:
		gary.forward(side_len)
		gary.right(90)
		counter += 1
		
def draw_circle(circ):
	alex = turtle.Turtle()
	alex.shape("turtle")
	alex.color("purple")
	alex.speed(8)
	
	alex.circle(circ)	
		
def draw_traingle(side_len):
	counter = 0
	num_sides = 3
	
	alice = turtle.Turtle()
	alice.shape("arrow")
	alice.color("blue")
	alice.speed(5)
	
	while counter < num_sides:
		alice.forward(side_len)
		alice.left (-120)
		counter += 1
			

#draw_square(100)
#draw_circle(100)
draw_traingle(200)

window.exitonclick()
	
