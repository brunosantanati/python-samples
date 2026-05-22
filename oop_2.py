class Numbers:
    def __getitem__(self, index):
        return index * 2

n = Numbers()

print(n[3])
print(n[50])