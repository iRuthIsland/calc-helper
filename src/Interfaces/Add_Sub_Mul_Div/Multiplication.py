from .Add_Sub_Mul_Div import Add_Sub_Mul_Div
from .Types import Types



class Multiplication(Add_Sub_Mul_Div):
    def __init__(self, page, callback):
        super().__init__(page=page, callback=callback, selected=Types.mul)
        pass
    pass
