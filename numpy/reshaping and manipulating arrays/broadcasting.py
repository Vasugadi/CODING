"""broad casting example
1 matching dimensions
2 expanding elments [1,2,3,4,5] + [1,2,3] = [2,4,6,5,7,8]
3.incompatible dimensions [1,2,3] + [1,2] = error
to solve incompatible dimensions we use np.newaxis
[1,2,3] + [[1],[2]] = [[2,3,4],[3,4,5]]

"""

prices=[100,200,300]
discount=10
final_prices=[]
for price in prices:
    final_price=price-(price*discount/100)
    final_prices.append(final_price)

print(final_prices)

import numpy as np
prices=np.array([100,200,300])
discount=10
final_prices2=(prices)-(prices)*discount/100
print(final_prices2)