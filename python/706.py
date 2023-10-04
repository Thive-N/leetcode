class MyHashMap:

    def __init__(self):
        self.l = {}

    def put(self, key: int, value: int) -> None:
        self.l[key] = value

    def get(self, key: int) -> int:
        return self.l.get(key, -1)

    def remove(self, key: int) -> None:
        self.l.pop(key, 0)
