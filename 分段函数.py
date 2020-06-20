import matplotlib.pyplot as plt

x = range(-20, 20, 1)
interval0 = [4 for i in x if (i<=3.5)]
interval1 = [25 for i in x if (3.5<=i<=6)]
interval2 = [49 for i in x if (i>6)]
interval = interval0+ interval1 + interval2

i0 = [(70-29*i)/(7-2*i) for i in x if (i<=2)]
i1 = [7*i-10 for i in x if (2<i<=4.5)]
i2 = [(210-37*i)/(6-i) for i in x if (4.5<i<=5)]
i3 = [12*i-35 for i in x if (5<i<=7)]
i4 = [(37*i-210)/(i-6) for i in x if (i>7)]
i = i0+i1+i2+i3+i4

j0 = [int((78*(i**2)-616*i+980)/(3*(i**2)-28*i+59)) for i in x if (i<=2)]
j1 = [((-70)*(i**2)+520*i-700)/((-(i**2)+4*i+11)) for i in x if (2<i<=5)]
j2 = [(20*(i**2)-70*i)/((-(i**2)+14*i-39)) for i in x if (5<i<=7)]
j3 = [(78*(i**2)-616*i+980)/(3*(i**2)-28*i+59) for i in x if (i>7)]
j=j0+j1+j2+j3

y1 = [y**2 for y in x]
plt.plot(x, y1, label='Original function')
plt.plot(x, interval, label='k=1')
plt.plot(x, i, label='k=2')
plt.plot(x,j,label='k=3' )
plt.xlabel('x')
plt.ylabel('y')
plt.axis([-20, 20, 0, 50])
plt.title('Function curve comparison')
plt.legend()
plt.show()