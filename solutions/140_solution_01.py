limit = 100

def clip(value):
    return min(max(0.0, value), limit)

value = -22.5

print(clip(value))