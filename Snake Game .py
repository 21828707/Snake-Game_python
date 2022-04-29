from turtle import * # ��Ʋ �׷��� ���
from time import sleep # Ÿ�� ����� sleep()�Լ� ���
from random import randint # ���� ����� randint()�Լ� ���

# ��ũ�� ����
win = Screen()
win.title("Snake Game")
win.setup(width=600,height=600)
win.tracer(0) # �ڵ���� ����Ǵ� ������ ��ũ��â�� ������� �ʴ´�.
dela=0.1
speed = 10	# ���ǵ�
select = 0
time - 0

#head
head = Turtle()
head.color("#696969")
head.shape("square")
head.penup() # ���� ��� �ø���. - �̵� �� ���� �׾����� �ʴ´�.
head.speed(0) 
head.direction = "stop" # ���� - ���� ���� ��������

#food
food = Turtle()
food.color('orange')
food.penup() # ���� ��� �ø���. - �̵� �� ���� �׾����� �ʴ´�.
food.shape("circle")
food.speed(0)

# item
item = Turtle()
item.color('blue')
item.penup() # ���� ��� �ø���. - �̵� �� ���� �׾����� �ʴ´�.
item.shape("circle")
item.hideturtle()
item.speed(0)
select = randint(1,3)
if select == 1:
	item.write("fast",align="center",font=("arial",10,"bold"))
elif select == 2:
	item.write("short",align="center",font=("arial",10,"bold"))
elif select == 3:
	item.write("bonus",align="center",font=("arial",10,"bold"))

#scoreing
scr=Turtle()
scr.color("black")
scr.shape("triangle")
scr.penup()
scr.speed(0)
scr.hideturtle() # �ﰢ�� ������ �����.
scr.goto(0,240)
scr.write("Score: 0 Highscore: 0",align="center",font=("arial",10,"bold")) # ���� ���ڿ��� �ִ� ��ġ�� ���
score=-1
highscore=-1

own=Turtle()
own.color("black")
own.shape("triangle")
own.penup()
own.speed(0)
own.hideturtle() # �ﰢ�� ������ �����.
own.goto(-250,-280)
own.write("Created By OMar ",font=("arial",5,"bold")) # ���� ���ڿ��� �ִ� ��ġ�� ���

#key press function
# �Լ� ����(def �Լ���(�Ű�����))
def go_up():
	dec = head.direction
	if dec != "down":
		head.direction = "up"
def go_down():
	if head.direction != "up":
		head.direction = "down"
def go_left():
	if head.direction != "right":
		head.direction = "left"
def go_right():
	if head.direction != "left":
		head.direction = "right"
win.listen()
win.onkeypress(go_up, "w")
win.onkeypress(go_down, "s")
win.onkeypress(go_left, "a")
win.onkeypress(go_right, "d")

# head move function 
# ������ ��ġ���� �ӵ� ��ŭ�� ��ġ �̵�
def move():
	dec = head.direction
	if dec == "up":
		head.sety(head.ycor()+ speed)
	elif dec == "down":
		head.sety(head.ycor()- speed)
	elif dec == "left":
		head.setx(head.xcor()- speed)
	elif dec == "right":
		head.setx(head.xcor()+ speed)

#body segment
segment=[]
while True:
	win.update() # ȭ���� ��� ������Ʈ
	if head.xcor() < -290 or head.xcor() > 290 or head.ycor() < -290 or head.ycor() > 290: # ȭ�� ������ �̵��� ��� �ʱ�ȭ
		head.goto(0,0)
		head.direction = "stop"
		for segments in segment:
			segments.goto(5000,5000)
		score=0
		dela=0.1
		scr.clear()
		scr.write(f"Score: {score} Highscore: {highscore}",align="center",font=("arial",10,"bold"))
		segment=[] 
	if head.distance(food) < 20: # ���� ȹ�� �� ��ü, ���� �߰�
		food.goto(randint(-290,290),randint(-290,290))
		
		#new body segment
		new_segment = Turtle()
		new_segment.speed(0)
		new_segment.color("#A9A9A9")
		new_segment.shape("square")
		new_segment.penup()
		segment.append(new_segment) # segment ����
		
		#scoring
		score+=1
		if score > highscore:
			highscore = score
		scr.clear()
		scr.write(f"Score: {score} Highscore: {highscore}",align="center",font=("arial",10,"bold"))
		dela+=0.001
	

	if head.distance(item) < 20:
		item.goto(randint(-290,290),randint(-290,290))
		while food.xcor == item.xcor and food.ycor == item.ycor:
			item.goto(randint(-290,290),randint(-290,290))
		if select == 1 or time > 0:
			if time < 30:
				speed += 0.5
				time += 1
			elif time >= 30:
				time = 0
		elif select == 2:
			segment.pop()
		elif select == 3:
			score += 5

		select = randint(1,3)
		if select == 1:
			item.write("fast",align="center",font=("arial",10,"bold"))
		elif select == 2:
			item.write("short",align="center",font=("arial",10,"bold"))
		elif select == 3:
			item.write("bonus",align="center",font=("arial",10,"bold"))

		
	#add body with head
	for i in range(len(segment)-1,0,-1): # ��ü�� ���̰� 2�̻��� ��� for�� ��ü�� �̵��ϰ� �ȴ�. 
		x,y=segment[i-1].xcor(),segment[i-1].ycor()
		segment[i].goto(x,y)
	if len(segment) > 0: # ��ü�� ���̰� 1���� ��� ���� for���� ���ؼ� ���� �ڵ�
		segment[0].goto(head.xcor(),head.ycor())
	move()
	#cut body
	for segments in segment: # �ڽ��� ���� �ε����� ���
		if head.distance(segments) < 10:
			head.goto(0,0)
			head.direction = "stop"
			for i in segment:
				i.goto(500,500)
			score=0
			scr.clear()
			scr.write(f"Score: {score} Highscore: {highscore}",align="center",font=("arial",10,"bold"))
			segment=[]
		dela=0.1
	sleep(dela) # ���� �������� �ĺ� �����ϰ� ���ݾ� ����
win.mainloop()