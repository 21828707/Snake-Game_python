from turtle import * # 터틀 그래픽 사용
from time import sleep # 타임 모듈의 sleep()함수 사용
from random import randint # 랜덤 모듈의 randint()함수 사용

# 스크린 생성
win = Screen()
win.title("Snake Game")
win.setup(width=600,height=600)
win.tracer(0) # 코드들이 실행되는 과정을 스크린창에 출력하지 않는다.
dela=0.1
speed = 10	# 스피드
select = 0
time = 0

#head
head = Turtle()
head.color("#696969")
head.shape("square")
head.penup() # 펜을 들어 올린다. - 이동 시 선이 그어지지 않는다.
head.speed(0) 
head.direction = "stop" # 방향 - 시작 전은 정지상태

#food
food = Turtle()
food.color('orange')
food.penup() # 펜을 들어 올린다. - 이동 시 선이 그어지지 않는다.
food.shape("circle")
food.speed(0)

# item
item = Turtle()
item.color('blue')
item.penup() # 펜을 들어 올린다. - 이동 시 선이 그어지지 않는다.
item.shape("circle")
item.speed(0)

#scoreing
scr=Turtle()
scr.color("black")
scr.shape("triangle")
scr.penup()
scr.speed(0)
scr.hideturtle() # 삼각형 모형을 숨긴다.
scr.goto(0,240)
scr.write("Score: 0 Highscore: 0",align="center",font=("arial",10,"bold")) # 숨긴 문자열이 있는 위치에 출력
score=-1
highscore=-1

own=Turtle()
own.color("black")
own.shape("triangle")
own.penup()
own.speed(0)
own.hideturtle() # 삼각형 모형을 숨긴다.
own.goto(-250,-280)
own.write("Created By OMar ",font=("arial",5,"bold")) # 숨긴 문자열이 있는 위치에 출력

#key press function
# 함수 정의(def 함수명(매개변수))
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
# 본래의 위치에서 속도 만큼의 위치 이동
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
	win.update() # 화면을 계속 업데이트
	if head.xcor() < -290 or head.xcor() > 290 or head.ycor() < -290 or head.ycor() > 290: # 화면 밖으로 이동할 경우 초기화
		head.goto(0,0)
		head.direction = "stop"
		for segments in segment:
			segments.goto(5000,5000)
		score=0
		dela=0.1
		scr.clear()
		scr.write(f"Score: {score} Highscore: {highscore}",align="center",font=("arial",10,"bold"))
		segment=[] 
	if head.distance(food) < 20: # 점수 획득 및 몸체, 점수 추가
		food.goto(randint(-290,290),randint(-290,290))
		
		#new body segment
		new_segment = Turtle()
		new_segment.speed(0)
		new_segment.color("#A9A9A9")
		new_segment.shape("square")
		new_segment.penup()
		segment.append(new_segment) # segment 증가
		
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
		if select == 1:
			if speed == 10:
				speed += 10
		elif select == 2:
			if len(segment) > 1:
				segment.pop()
		elif select == 3:
			score += 5

		select = randint(1,3)
		if select == 1:
			item.shape("circle") # 부스트 아이템 구현 완성
		elif select == 2:
			item.shape("triangle")
		elif select == 3:
			item.shape("square")

		
	#add body with head
	for i in range(len(segment)-1,0,-1): # 몸체의 길이가 2이상일 경우 for문 몸체가 이동하게 된다. 
		x,y=segment[i-1].xcor(),segment[i-1].ycor()
		segment[i].goto(x,y)
	if len(segment) > 0: # 몸체의 길이가 1개일 경우 위의 for문을 위해서 따로 코드
		segment[0].goto(head.xcor(),head.ycor())
	move()
	#cut body
	for segments in segment: # 자신의 몸과 부딧쳤을 경우
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

	# 아이템 1 효과 제어
	if speed != 10:
		time += 1
	if time >= 30:
		time = 0
		speed = 10
	sleep(dela) # 뱀의 움직임을 식별 가능하게 조금씩 정지
win.mainloop()