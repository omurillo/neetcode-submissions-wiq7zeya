class TimeMap:

    def __init__(self):
        self.keystore = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.keystore:
            self.keystore[key] = []
        val = [value, timestamp]
        self.keystore[key].append(val)

    def get(self, key: str, timestamp: int) -> str:
        res, values = "", self.keystore.get(key, [])
        left, right = 0, len(values) - 1
        while left <= right:
            middle = (left + right) // 2
            if values[middle][1] <= timestamp:
                res = values[middle][0]
                left = middle + 1
            else:
                right = middle - 1
        return res


