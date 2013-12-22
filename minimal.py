# matplotlib is too helpful for its own good

# IF I run this with 'python'
# because the plot must be hooked to run when python exits but then immediately exits
# IF I run it with 'python -i' then it does show up
# 
# IF i run this code with plt.ion()
# paste this code into a terminal:

# If I paste this into a terminal...

import matplotlib.pyplot as plt
#plt.ion() #key? does this show up???
          # arrrrgh. 
fig, ax = plt.subplots()

#plt.show() #doing this explicitly means it blocks here
# "in noninteractive mode", ie without calling .ion(),
# matplotlib has two paths here:
#  -if you run with python -i, it displays the plot
#  -if you do not run with -i, it simply exits and you never see your result

# What I ~really~ want is a simple way to display
