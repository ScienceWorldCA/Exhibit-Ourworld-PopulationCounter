#LED_font_constants.py

# text colours (all have been verified by testing)
RED             = 0xB0
BRIGHTRED       = 0xB1
ORANGE          = 0xB2
BRIGHTORANGE    = 0xB3
YELLOW          = 0xB4
BRIGHTYELLOW    = 0xB5
GREEN           = 0xB6
BRIGHTGREEN     = 0xB7
LAYERMIX        = 0xB8
BRIGHTLAYERMIX  = 0xB9
VERTICALMIX     = 0xBA
SAWTOOTHMIX     = 0xBB
GREENONRED      = 0xBC
REDONGREEN      = 0xBD
ORANGEONRED     = 0xBE
YELLOWONGREEN   = 0XBF

# text sizes
FONT5X6         = 0xA0
FONT5X11        = 0xA1
FONT7X6         = 0xA2
FONT7X11        = 0xA3
FONT7X9         = 0xA4
FONT7X17        = 0xA5
FONTSMALL       = 0xA6

# transitions (unverified unless marked otherwise)
CYCLIC          = 0x01
IMMEDIATE       = 0x02
#               = 0x03  # Open from Right
#               = 0x04  # Open from Left
#               = 0x05  # Open from Centre
#               = 0x06  # Open to Centre
#               = 0x07  # Cover from Centre
#               = 0x08  # Cover from Right
#               = 0x09  # Cover from Left
#               = 0x0A  # Cover to Centre
#               = 0x0B  # Scroll Up
#               = 0x0C  # Scroll Down
#               = 0x0D  # Interlace to Centre
#               = 0x0E  # Interlace Cover
COVERUP         = 0x0F
COVERDOWN       = 0x10
#               = 0x11  # Scan Line
#               = 0x12  # Explode
#               = 0x13  # Pac Man
#               = 0x14  # Fall & Stack
#               = 0x15  # Shoot
#               = 0x16  # Flash
#               = 0x17  # Random
#               = 0x18  # Slide In
#               = 0x19  # Compress Text (does not work!)

# approximate pause between transitions (must be placed at the end of the header)
TWOSECONDS      = 0xC8  # default
THREESECONDS    = 0xC9
FOURSECONDS     = 0xCA
SIXSECONDS      = 0xCB
TENSECONDS      = 0xCC
TWENTYSECONDS   = 0xCD
THIRTYSECONDS   = 0xCE
SIXTYSECONDS    = 0xCF

# transition speed
#               = 0xC0  # fastest
#               = 0xC1
#               = 0xC2  # default
#               = 0xC3
#               = 0xC4
#               = 0xC5
#               = 0xC6
#               = 0xC7  # slowest

# Use the settings below to modify the text formatting to the LED
textSize        = FONT7X6
textColour      = BRIGHTGREEN
transition      = IMMEDIATE
transitionSpeed = 0xC0
pause           = TWOSECONDS
thousandsseparator      = ','   # which character to use (comma is common use; space for SI style,
                                #or leave blank for no delimiter

								