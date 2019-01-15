import turtle as t

class MagicBrush:
    def draw_square(self):
        for i in range(4):
            t.forward(100)
            t.right

m = MagicBrush()
m.draw_square()

brad = t.Turtle()
brad.shape('turtle')
brad.speed(2)
brad.forward(100)

t.mainloop()