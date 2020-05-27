from turtle import * #imports turtle
bgcolor('yellow') #the background color
color('blue', 'black') # the two colors in the drawing
begin_fill() #fills the drawing
while True:
    forward(200) #this is the amount of pixels in that direction
    left(170) #this is the angle
    if abs(pos()) < 1:
       break 
end_fill()	# fills the drawing
done()# makes it able to exit the program and keeps the window from closing at the start