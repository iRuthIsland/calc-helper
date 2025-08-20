from .Add_Sub_Mul_Div import Add_Sub_Mul_Div
from .Types import Types



class Division(Add_Sub_Mul_Div):
    def __init__(self, page, callback):
        super().__init__(page=page, callback=callback, selected=Types.div)
        pass
    pass
