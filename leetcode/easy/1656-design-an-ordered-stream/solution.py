class OrderedStream:

    def __init__(self, n: int):
        self.stream = [None] * (n + 1)
        self.ptr = 1

    def insert(self, idKey: int, value: str) -> list[str]:
        self.stream[idKey] = value
        res = []
        while self.ptr < len(self.stream) and self.stream[self.ptr] is not None:
            res.append(self.stream[self.ptr])
            self.ptr += 1
        return res