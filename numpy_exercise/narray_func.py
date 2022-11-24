import numpy as np

#zeros()
print(np.zeros((2,2)))
#ones()
print(np.ones((1,2)))
print(np.ones((2,1)))
#full()
print(np.full((2,2), 7))

#identity() (단위행렬)
print(np.identity(3))
#eye()
print(np.eye(3))
print(np.eye(3, k=1))
print(np.eye(3, k=-2))

#random.random()
print(np.random.random((2,2)))
#random.normal()
print(np.random.normal((2,2))) #??????  **결과가 이해가 안된다
#random.randint()
print(np.random.randint(0,3,(3,3)))

#linspace()
print(np.linspace(0,1,num=5,endpoint=True))
print(np.linspace(0,1,num=5,endpoint=True,retstep=True))
print(np.linspace(0,1,num=5,endpoint=False))
print(np.linspace(0,1,num=5,endpoint=False,retstep=True))
print(type(np.linspace(0,1,num=5,endpoint=False,retstep=True)))
print(np.linspace(0,1,num=5,endpoint=False,retstep=True)[0])
print(type(np.linspace(0,1,num=5,endpoint=False,retstep=True)[0]))

#arange()
print(np.arange(0.4, 1.1, 0.1, dtype=float))
