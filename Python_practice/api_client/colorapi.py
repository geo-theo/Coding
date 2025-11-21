"""
colorapi.py
------------
Functions for computing luminance, grayscale, contrast ratio,
and color compatibility between RGB colors.

Created a new function make_color() so that all other functions are able to take CSS color string names as well as color objects.
Error, edge, and corner case handling will also happen in the make_color function

Formulas:
----------
1. Luminance:
   L = 0.299 * R + 0.587 * G + 0.114 * B

2. Contrast Ratio (WCAG):
   ratio = (L1 + 0.05) / (L2 + 0.05)
   where:
       L1 = higher luminance / 255
       L2 = lower luminance / 255
"""
from color import Color
THRESHOLD = 128  # Minimum luminance difference for compatibility

def make_color(value):
    """Return a Color object from a Color or color name string."""
    if isinstance(value, Color):
        return value
    if value == "":
        raise ValueError("Input cannot be an empty string.")
    if not isinstance(value, str):
        raise ValueError("Input must be a Color object (for example, Color(255, 0, 255)) or a color name string (for example, 'yellow').")
    name = value.lower().strip()

    COLORS = {
        "black": (0, 0, 0),
        "white": (255, 255, 255),
        "red": (255, 0, 0),
        "green": (0, 255, 0),
        "blue": (0, 0, 255),
        "yellow": (255, 255, 0),
        "cyan": (0, 255, 255),
        "magenta": (255, 0, 255),
        "gray": (128, 128, 128),
        "grey": (128, 128, 128),
        "orange": (255, 165, 0),
        "pink": (255, 192, 203),
        "purple": (128, 0, 128),
        "brown": (165, 42, 42),
        "gold": (255, 215, 0),
        "beige": (245, 245, 220),
        "navy": (0, 0, 128),
        "teal": (0, 128, 128),
        "olive": (128, 128, 0),
        "lime": (0, 255, 0),
        "skyblue": (135, 206, 235),
        "royalblue": (65, 105, 225),
        "turquoise": (64, 224, 208),
        "indigo": (75, 0, 130),
        "violet": (238, 130, 238),
        "salmon": (250, 128, 114),
        "chocolate": (210, 105, 30),
        "coral": (255, 127, 80),
        "crimson": (220, 20, 60),
        "darkblue": (0, 0, 139),
        "darkgreen": (0, 100, 0),
        "darkred": (139, 0, 0),
        "lightblue": (173, 216, 230),
        "lightgreen": (144, 238, 144),
        "lightgray": (211, 211, 211),
    }

    if name not in COLORS:
        raise ValueError(f"Unknown color name: {value}")

    r, g, b = COLORS[name]
    return Color(r, g, b)




def luminance(myColor):
    """Return the luminance of a color based on its RGB values."""
    myColor = make_color(myColor)
    R = myColor.getRed()
    G = myColor.getGreen()
    B = myColor.getBlue()

    luminance = 0.299 * R + 0.587 * G + 0.114 * B
    return luminance
# luminance("") # raise error for empty string
# luminance("Hello") # raise error for non-color
# luminance(1) # raise error for non-color
# luminance("black")
# luminance("white")
# luminance("yellow")
# luminance("crimson")
# luminance(Color(57, 138, 231))

def isCompatible(myColor, myOtherColor):
    """Return True if two colors have a luminance difference >= THRESHOLD."""
    myColor = make_color(myColor)
    myColor = make_color(myColor)
    myOtherColor = make_color(myOtherColor)

    lum1 = luminance(myColor)
    lum2 = luminance(myOtherColor)

    difference = abs(lum1 - lum2) #make sure difference is positive value
    if difference >= THRESHOLD:
        return True
    else:
        return False
# isCompatible("red", "") # raise error for empty string
# isCompatible("red", "Hello") # raise error for non-color
# isCompatible("red", 1) # raise error for non-color
# isCompatible("black", "white") # True
# isCompatible("blue", "purple") # False
# isCompatible("cyan", "darkred") # True
# isCompatible((Color(57, 138, 231)), (Color(254, 11, 120))) # False

def grayscale(myColor):
    """Return a grayscale version of the given color."""
    myColor = make_color(myColor)
    brightness = luminance(myColor)
    gray = Color(int(brightness), int(brightness), int(brightness)) # creates grayscale where R, G, and B are all equal to the luminance
    return gray
# print(grayscale("")) # raise error for empty string
# print(grayscale("Hello")) # raise error for non-color
# print(grayscale(1)) # raise error for non-color
# print(grayscale("yellow"))
# print(grayscale("violet"))
# print(grayscale(Color(57, 138, 231)))

def contrastRatio(myColor, myOtherColor):
    """Return the contrast ratio between two colors using the WCAG formula."""
    myColor = make_color(myColor)
    myOtherColor = make_color(myOtherColor)

    lum1 = luminance(myColor) / 255
    lum2 = luminance(myOtherColor) / 255
    if lum1 < lum2: #puts higher luminance in numerator and smaller luminance in denomenator
        lum1, lum2 = lum2, lum1  #swap so lum1 is always lighter

    contrast_ratio = (lum1 + 0.05) / (lum2 + 0.05) #WCAG formula
    return contrast_ratio
# contrastRatio("red", "") # raise error for empty string
# contrastRatio("red", "Hello") # raise error for non-color
# contrastRatio("red", 1) # raise error for non-color
# contrastRatio("black", "white")
# contrastRatio("yellow", "navy")
# contrastRatio("salmon", "beige")
# contrastRatio((Color(57, 138, 231)), (Color(254, 11, 120)))

def complementary(myColor):
    """Return the complementary (inverse) color."""
    myColor = make_color(myColor)
    R = int(myColor.getRed())
    G = int(myColor.getGreen())
    B = int(myColor.getBlue())

    invR = 255 - R #invert red
    invG = 255 - G #invert green
    invB = 255 - B #invert blue
    complementaryColor = Color(invR, invG, invB)

    return complementaryColor
# print(complementary("")) # raise error for empty string
# print(complementary("Hello")) # raise error for non-color
# print(complementary(1)) # raise error for non-color
# print(complementary("yellow"))
# print(complementary("coral"))
# print(complementary(Color(57, 138, 231)))