# class Char(Field[str]):
#     min_length: int
#     max_length: int
#
#     def __init__(
#         self, min_length: int | None = None, max_length: int | None = None
#     ):
#         self.min_length = min_length or 0
#         self.max_length = max_length or 1000
#         print(self.value)
#
#     def create(self) -> None:
#         self.value = "a" * self.min_length
