import random
from bokeh.plotting import figure, show

def toss():
  t = []
  num = 0
  count = 0 
  for i in range(500):
    num += random.randint(0,1)
    count += 1
    t.append(num/count)
  return t
  
f = figure(width = 600,height = 500, x_range=(0, 500), y_range=(0, 1), x_minor_ticks = 2, background_fill_color = "black")
f.background_fill_alpha = 0.75
f.xgrid.visible = False
f.ygrid.visible = False
for i in range(100):
  col = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
  f.line(range(500), toss(), color = col)

show(f)
  
