class FavoritesList:
    class Item:
        def __init__(self, val):
            self.val = val
            self.count = 0

    def __init__(self):
        self.items = []

    def _find(self, e):
        for i in range(len(self.items)):
            if self.items[i].val == e:
                return i
        return -1

    def access(self, e):
        idx = self._find(e)
        if idx == -1:
            self.items.append(self.Item(e))
            idx = len(self.items) - 1
        self.items[idx].count += 1
        # move forward to keep sorted by count
        while idx > 0 and self.items[idx].count > self.items[idx - 1].count:
            self.items[idx], self.items[idx - 1] = self.items[idx - 1], self.items[idx]
            idx -= 1

    def remove(self, e):
        idx = self._find(e)
        if idx != -1:
            self.items.pop(idx)

    def top(self, k):
        res = []
        for i in range(min(k, len(self.items))):
            res.append((self.items[i].val, self.items[i].count))
        return res

fav = FavoritesList()
for song in ["a", "b", "a", "c", "b", "a"]:
    fav.access(song)
print("top 2:", fav.top(2))
fav.remove("b")
print("after removing b:", fav.top(3))
