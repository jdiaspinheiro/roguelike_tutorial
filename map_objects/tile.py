class Tile:
    """
    Map tiles | May or may not be blocked (sight or otherwise)
    """
    def __init__(self, blocked, block_sight=None):
        self.blocked = blocked
        
        # Default behaviour - If tile is blocked, sight is blocked
        if block_sight is None:
            block_sight = blocked

        self.block_sight = block_sight