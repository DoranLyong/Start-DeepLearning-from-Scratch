# coding: utf-8


class MulLayer:
    def __init__(self):
        self.x = None
        self.y = None

    def forward(self, x_in, y_in):
        self.x = x_in
        self.y = y_in                
        out = x_in * y_in

        return out

    def backward(self, dout):
        dx = dout * self.y  # x와 y를 바꾼다.
        dy = dout * self.x

        return dx, dy


class AddLayer:
    def __init__(self):
        pass

    def forward(self, x_in, y_in):
        out = x_in + y_in

        return out

    def backward(self, dout):
        dx = dout * 1
        dy = dout * 1

        return dx, dy
