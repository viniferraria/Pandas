import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df=pd.DataFrame({'x': range(1,11),
'y1': [1,2,3,4,6,7,8,4,65,7],
'y2': np.random.randn(10),
'y3': np.random.randn(10)*20 })

plt.plot('x','y1', data=df, marker='', color='skyblue', markersize=12, linewidth=2) 
plt.plot('x','y2', data=df, marker='', color='olive', linewidth=2)
plt.plot( 'x', 'y3', data=df, marker='', color='red', linewidth=2, linestyle='dashed')
plt.legend()