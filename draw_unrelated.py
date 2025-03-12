# completely unrelated, just ignore it
# drawing test

import turtle as t
import random

# step collections / patterns
# angle must be 90 & round should be 4
patterns = {
    "manji" : 120010023 # 卍
}

rand = random.randint(1, 10**30)
print(rand)

#setting

step = 111211166 # a serie of numbers or put a patten here: ex) step = patterns["manji"]
scale = 10
round = 4
speed = 0 # high = fast; low = slow; 0 = fastest
angle = 90

# Code
step = str(step)
t.speed(speed)

for i in  range(len(step)*round):
    t.forward(int(step[i%len(step)])*scale)
    t.right(angle)

t.mainloop()