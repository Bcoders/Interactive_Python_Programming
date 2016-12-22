 
###################################################
# Time formatting function
import simplegui
import random

seconds = 361


def format_time(seconds):
    minu = str(int(seconds)// 60)
    sec = str(int(seconds)- (int(minu)*60))
    
    sec_units = convert_units(sec," second")
    minu_units = convert_units(minu," minute")
    
    if(int(minu) == 0):
        sec = str(sec)
        return sec + sec_units
        
    elif(int(sec) == 0):
        minu = str(minu)
        return minu + minu_units 
        
    else:
        sec = str(sec)
        minu = str(minu)
        return str(minu)+ minu_units + ' and '+ str(sec)+ sec_units
    
    
def convert_units(time, unit):
    if (int(time) > 0):
        return unit+"s"
    else:
        return unit
        
    
# Student should enter function on the next lines.


#define globals
#define classes
#define event handler.
def input_handler(text):
    global seconds
    seconds = text
    
    
    
    
    
    

#define draw handler.
def draw_handler(canvas):
    canvas.draw_text(format_time(seconds), [60, 110], 20, "White")
    
#create frame
frame = simplegui.create_frame("Minute converter", 300,300)

#register event handler.
frame.set_draw_handler(draw_handler)
frame.add_input("Convert seconds to minute", input_handler, 100)

#start frame
frame.start()

###################################################
# Tests
print format_time(23)
print format_time(1237)
print format_time(0)
print format_time(1860)



###################################################
# Output to console
#0 minutes and 23 seconds
#20 minutes and 37 seconds
#0 minutes and 0 seconds
#31 minutes and 0 seconds
