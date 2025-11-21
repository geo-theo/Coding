import stddraw

# Set canvas
stddraw.setCanvasSize(600, 600)
stddraw.setXscale(-1.5, 1.5)
stddraw.setYscale(-1.5, 1.5)

# Mouth coordinates
FROWN_CENTER_Y  = -0.50
FROWN_CORNER_Y  = -0.70
SMILE_CENTER_Y  = -0.70
SMILE_CORNER_Y  = -0.50
r = 1.0

# Frowning cat
stddraw.clear(stddraw.WHITE)
stddraw.setPenColor(stddraw.BLACK)
stddraw.filledCircle(0, 0, r)
stddraw.filledPolygon([-0.9, -0.5, -0.2], [0.4, 1.2, 0.4])
stddraw.filledPolygon([0.9, 0.5, 0.2],   [0.4, 1.2, 0.4])
stddraw.setPenColor(stddraw.YELLOW)
stddraw.filledCircle(-0.4, 0.3, 0.15)
stddraw.filledCircle(0.4,  0.3, 0.15)
stddraw.setPenColor(stddraw.BLACK)
stddraw.filledCircle(-0.4, 0.3, 0.07)
stddraw.filledCircle(0.4,  0.3, 0.07)
stddraw.setPenColor(stddraw.PINK)
stddraw.filledPolygon([-0.1, 0.1, 0], [-0.1, -0.1, -0.3])
stddraw.line(0.0, FROWN_CENTER_Y, -0.15, FROWN_CORNER_Y)
stddraw.line(0.0, FROWN_CENTER_Y,  0.15, FROWN_CORNER_Y)
stddraw.show(500)

# Flood goes up
total_steps = 60
for i in range(total_steps + 1):
    height = 3.0 * (i / total_steps)
    stddraw.setPenColor(stddraw.BLUE)
    stddraw.filledRectangle(-1.5, -1.5, 3.0, height)
    stddraw.show(30)

# Flood goes down
for i in range(total_steps + 1):
    height = 3.0 * (1 - i / total_steps)
    stddraw.clear(stddraw.WHITE)
    stddraw.setPenColor(stddraw.BLACK)
    stddraw.filledCircle(0, 0, r)
    stddraw.filledPolygon([-0.9, -0.5, -0.2], [0.4, 1.2, 0.4])
    stddraw.filledPolygon([0.9, 0.5, 0.2],   [0.4, 1.2, 0.4])
    stddraw.setPenColor(stddraw.YELLOW)
    stddraw.filledCircle(-0.4, 0.3, 0.15)
    stddraw.filledCircle(0.4,  0.3, 0.15)
    stddraw.setPenColor(stddraw.BLACK)
    stddraw.filledCircle(-0.4, 0.3, 0.07)
    stddraw.filledCircle(0.4,  0.3, 0.07)
    stddraw.setPenColor(stddraw.PINK)
    stddraw.filledPolygon([-0.1, 0.1, 0], [-0.1, -0.1, -0.3])
    stddraw.line(0.0, FROWN_CENTER_Y, -0.15, FROWN_CORNER_Y)
    stddraw.line(0.0, FROWN_CENTER_Y,  0.15, FROWN_CORNER_Y)
    stddraw.setPenColor(stddraw.BLUE)
    stddraw.filledRectangle(-1.5, -1.5, 3.0, height)
    stddraw.show(30)

# Smiling cat
stddraw.clear(stddraw.WHITE)
stddraw.setPenColor(stddraw.BLACK)
stddraw.filledCircle(0, 0, r)
stddraw.filledPolygon([-0.9, -0.5, -0.2], [0.4, 1.2, 0.4])
stddraw.filledPolygon([0.9, 0.5, 0.2],   [0.4, 1.2, 0.4])
stddraw.setPenColor(stddraw.YELLOW)
stddraw.filledCircle(-0.4, 0.3, 0.15)
stddraw.filledCircle(0.4,  0.3, 0.15)
stddraw.setPenColor(stddraw.BLACK)
stddraw.filledCircle(-0.4, 0.3, 0.07)
stddraw.filledCircle(0.4,  0.3, 0.07)
stddraw.setPenColor(stddraw.PINK)
stddraw.filledPolygon([-0.1, 0.1, 0], [-0.1, -0.1, -0.3])
stddraw.line(0.0, SMILE_CENTER_Y, -0.15, SMILE_CORNER_Y)
stddraw.line(0.0, SMILE_CENTER_Y,  0.15, SMILE_CORNER_Y)

# Animate
stddraw.show()


# Write-up
"""
One thing I noticed about how the film Flow communicates without dialogue, is through body language, sound intonation, and facial expressions used by the animals. Each of these components were very effective at conveying what was happening and how the characters were feeling about every situation and their interactions with each other. The body language and sound intonations were specific to each animal, but I noticed that some of the facial emotions were more human-like expressions than animal-like, in order to emphasize the communication clearer.
Therefore, I decided to connect my animation to the imagery of the film Flow, by animating a human facial expression of happiness (smiling) and sadness (frowning). My animation is connected not only with the imagery of facial expressions, but also ties slightly into the theme as well. A major theme of the film was about the (often sad) balance of nature of survival; so the animated cat is showing sadness for the devastating flood, and sadness for the whale dying at the flood receding. But in the film the whale does not appear to be sad, as it understands it is the cycle of life, and so the cat is able to look at their new friends and ultimately be happy in their survival and understanding the balance of nature.
In my animation, I have a cat that is frowning at the impending flood. The flood rises quickly, engulfing the screen. Then the flood recedes, and the cat’s frown turns to a smile. 
"""
