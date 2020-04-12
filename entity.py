class Entity:
    """
    Generic object to represent everything on the map (players, enemies, items, etc.)
    """
    def __init__(self, x, y, char, color):
        self.x = x
        self.y = y
        self.char = char
        self.color = color

    def move(self, dx, dy):
        # Move by given amount
        self.x += dx
        self.y += dy