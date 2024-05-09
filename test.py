from common import matrix_expression as me
from common import initialization
import pandas as pd 


A = initialization.A()['matrix']
Y = initialization.Y()['matrix']
I = initialization.I()['matrix']
E = initialization.E()['matrix']

LEFT = me.matrix_multiplication(A, Y)
LEFT = me.matrix_multiplication(LEFT, me.transposition(A))
df_LEFT = pd.DataFrame(data=LEFT)

RIGHT = me.matrix_multiplication(Y, E)
RIGHT = me.addition(I, RIGHT)
RIGHT = me.matrix_multiplication(A, RIGHT)
RIGHT = me.scalar_multiplication(-1, RIGHT)
df_RIGHT = pd.DataFrame(data=RIGHT)


SOLVE = me.gauss(LEFT, RIGHT)
df_SOLVE = pd.DataFrame(data=SOLVE)
print(df_SOLVE)