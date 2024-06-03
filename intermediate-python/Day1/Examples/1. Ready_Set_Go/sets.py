# Sets

color1 = {'Red','Blue','Green'}
color2 = {'Red','Yellow','Purple'}

#intersection
print(color1 & color2)

#union
print(color1 | color2)

#difference
print(color1 - color2)

#exclusive
print(color1 ^ color2)

#issubset
print({'Blue'} <= color1)

#issuperset
print(color1 >= {'Blue'})
