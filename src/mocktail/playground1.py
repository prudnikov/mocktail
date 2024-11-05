class A:
    number: int


aa = getattr(A, "__mocktail_fields__", None)
print(aa)


setattr(A, "__mocktail_fields__", dict(number=1))
aa = getattr(A, "__mocktail_fields__", None)
print(aa)
