from complex.Complex import MyComplex
import math as m

# creating two complex number
a = MyComplex(re=2.0, im=1.0)
b = MyComplex(r=5.0, theta=m.pi / 4.0)
print("Informations for complex 'a':")
print(a)
print("\nInformations for complex 'b':")
print(b)

# we can determine their complex sum c = a+b via the overloaded operator '+'
c = a + b
# we print the result and verify that the resulting variable 'c' is indeed an instance of the class 'Complex'
print("\nInformation on their sum:")
print(c)
print("\nSaving visualisation for c ...")
c.visualization("single").savefig("sum.png")

# similarly, we can compute other basic complex operations between the complex number 'a' and 'b'
c = a - b
print("\nInformation on their difference:")
print(c)
print("\nSaving visualisation for c ...")
c.visualization("single").savefig("diff.png")

c = a * b
print("\nInformation on their product:")
print(c)
c.visualization("single").savefig("prod.png")

c = a / b
print("\nInformation on their ratio:")
print(c)
c.visualization("single").savefig("div.png")

print(f"\nTheir respective modules are: {a.mod():.2f}, {b.mod():.2f}")
