import cmath
import math

a = 1  # 1,1,1
# float(input("Enter value for a: "))   #we can use entries from user
b = 6  # 6,4,6
c = 5  # 45,4,5

# Calculate the discriminant: The discriminant, \(D=b^{2}-4ac\), determines the nature of the roots.

discriminant = (b**2) - (4 * a * c)

# Calculate the roots: Apply the quadratic formula, \(x=\frac{-b\pm \sqrt{D}}{2a}\), considering the three cases for the discriminant:
print(f" the discriminant D value->{discriminant}")
if discriminant > 0 or discriminant < 0:
    # Two distinct real roots when D > 0
    # Two complex conjugate roots when D < 0

    root1 = (-b - cmath.sqrt(discriminant)) / (2 * a)
    root2 = (-b + cmath.sqrt(discriminant)) / (2 * a)

    print(f"The roots are  {int(root1.real)} and {int(root2.real)}")
else:
    # when D=0 One real root, repeated
    root = -b / (2 * a)
    print(f"The real root, repeated is-> {int(root.real)}")
