class cookie:
    def __init__(self, color):
        self.color = color
    
    def p_color(self):
        print(self.color)



my = cookie('amarillo')
my.p_color()
