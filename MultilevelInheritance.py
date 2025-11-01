class A:
    def describe(self):
        return "A"

class B(A):
    def describe(self):
        return f"B -> {super(B, self).describe()}"

class C(B):
    def describe(self):
        return f"C -> {super(C, self).describe()}"

obj = C()
print(obj.describe())