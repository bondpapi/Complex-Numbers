import math


class ComplexNumber:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        """addition of two complex number's real and imaginary parts to return ComplexNumber"""
        return ComplexNumber(self.real + other.real, self.imag + other.imag)

    def __sub__(self, other):
        """subtracts real and imaginary parts of two complex numbers returns ComplexNumber"""
        return ComplexNumber(self.real - other.real, self.imag - other.imag)

    def __mul__(self, other):
        """multiplication of two complex numbers using (a+bi)×(c+di)=(ac−bd)+(ad+bc)i formula"""
        real_part = (self.real * other.real) - (self.imag * other.imag)
        imag_part = (self.real * other.imag) + (self.imag * other.real)
        return ComplexNumber(real_part, imag_part)

    def __truediv__(self, other):
        """division of two complex numbers"""
        denom = other.real**2 + other.imag**2
        real_part = (self.real * other.real + self.imag * other.imag) / denom
        imag_part = (self.imag * other.real - self.real * other.imag) / denom
        return ComplexNumber(real_part, imag_part)

    def mod(self):
        return ComplexNumber(math.sqrt(self.real**2 + self.imag**2), 0)

    def __str__(self):
        # Format the string based on the value of real and imaginary parts
        if self.imag == 0:
            return f"{self.real:.2f}+0.00i"
        elif self.real == 0:
            return f"0.00{'+' if self.imag >= 0 else '-'}{abs(self.imag):.2f}i"
        else:
            return (
                f"{self.real:.2f}{'+' if self.imag >= 0 else '-'}{abs(self.imag):.2f}i"
            )


if __name__ == "__main__":

    """Input Handling"""
    real1, imag1 = map(float, input().split())
    real2, imag2 = map(float, input().split())

    """Complex Numbers"""
    C = ComplexNumber(real1, imag1)
    D = ComplexNumber(real2, imag2)

    """Operations"""
    print(C + D)  # Addition
    print(C - D)  # Subtraction
    print(C * D)  # Multiplication
    print(C / D)  # Division
    print(f"{C.mod():.2f}")  # Modulus of C
    print(f"{D.mod():.2f}")  # Modulus of D
