Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import numpy as np
>>> x=np.array([1,2,3,5])
>>> x
array([1, 2, 3, 5])
>>> np.arange(0,-10,-1)
array([ 0, -1, -2, -3, -4, -5, -6, -7, -8, -9])
>>> x.shape
(4,)
>>> np.full((2,2),8)
array([[8, 8],
       [8, 8]])
>>> np.full((2,3),8)
array([[8, 8, 8],
       [8, 8, 8]])
>>> np.linspace(1,4,6)
array([1. , 1.6, 2.2, 2.8, 3.4, 4. ])
>>> x=np.eye(3)
>>> x
array([[1., 0., 0.],
       [0., 1., 0.],
       [0., 0., 1.]])
>>> np.eye(3,4)
array([[1., 0., 0., 0.],
       [0., 1., 0., 0.],
       [0., 0., 1., 0.]])
>>> x=np.random.random((3,4))
>>> x
array([[0.56892526, 0.16012393, 0.5438949 , 0.30897769],
       [0.89852791, 0.83672616, 0.21396998, 0.66245049],
       [0.40249042, 0.18330502, 0.28303189, 0.94384205]])
>>> x=x*1
>>> x
array([[0.56892526, 0.16012393, 0.5438949 , 0.30897769],
       [0.89852791, 0.83672616, 0.21396998, 0.66245049],
       [0.40249042, 0.18330502, 0.28303189, 0.94384205]])
>>> x=x*100
>>> x
array([[56.89252639, 16.01239334, 54.38949013, 30.89776874],
       [89.85279111, 83.67261629, 21.39699809, 66.24504927],
       [40.24904221, 18.33050235, 28.30318916, 94.38420517]])
>>> x=x%10
>>> x
array([[6.89252639, 6.01239334, 4.38949013, 0.89776874],
       [9.85279111, 3.67261629, 1.39699809, 6.24504927],
       [0.24904221, 8.33050235, 8.30318916, 4.38420517]])
>>> x=x*10
>>> x
array([[68.92526386, 60.12393344, 43.89490132,  8.97768742],
       [98.52791107, 36.7261629 , 13.96998089, 62.45049266],
       [ 2.49042211, 83.30502351, 83.03189156, 43.84205165]])
>>> x=x+1
>>> x
array([[69.92526386, 61.12393344, 44.89490132,  9.97768742],
       [99.52791107, 37.7261629 , 14.96998089, 63.45049266],
       [ 3.49042211, 84.30502351, 84.03189156, 44.84205165]])
>>> 
>>> x
array([[69.92526386, 61.12393344, 44.89490132,  9.97768742],
       [99.52791107, 37.7261629 , 14.96998089, 63.45049266],
       [ 3.49042211, 84.30502351, 84.03189156, 44.84205165]])
>>> 
>>>
>>> 