# template for "Stopwatch: The Game"
import simplegui

# define global variables
interval = 100
count = 0
t = 0
total = 0
mili = 0 

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    global mili
    minu = 0
    mili = int(t)%10          #gives us millisecs
    
    remainder1 = int(t)//10
    sec = remainder1%100     #gives us second
    
    if(sec>=60):
        minu = int(t)//1000 + sec//60 #minutes
        sec = sec%60
    
    else:
        minu = int(t)//1000
     
    if(sec<10):
        sec = "0"+str(sec)
    
    return str(minu)+":"+str(sec)+"."+str(mili)
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def Start():    
    timer.start()

def Stop():
    global count
    global total 
    global mili
    timer.stop()
    total = total +1
    if (mili == 0):
        count = count +1
    
def Reset():
    global t
    global count
    global total
    timer.stop()
    t = 0
    count = 0
    total = 0
    
      
# define event handler for timer with 0.1 sec interval
def tick():
    global t
    t = t + 1
    return

# define draw handler
def draw_handler(canvas):
    canvas.draw_text(format(t), (133, 160), 70, 'Green')
    canvas.draw_text(str(total)+"/"+str(count), (20,20), 30, "Red")
    canvas.draw_circle((210, 190), 150, 5, 'Blue')
    canvas.draw_text("Stop Watch", (100, 250), 50, 'White')
    
# create frame
frame = simplegui.create_frame("Time converter", 400, 400)
frame.set_draw_handler(draw_handler)

# register event handlers
frame.add_button("Stop", Stop, 100)
frame.add_button("Start", Start, 100)
frame.add_button("Reset", Reset, 100)
timer = simplegui.create_timer(interval, tick)


# start frame
frame.start()


# Please remember to review the grading rubric

