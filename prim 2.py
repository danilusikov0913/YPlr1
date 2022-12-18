def mul(a):
    def helper(b):
        return a * b

    return helper


new_mul5 = mul(5)
print(new_mul5(2))
print(new_mul5(7))
