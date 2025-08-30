class BeaconPlugin(PythonPlugin):
    def onEnable(self):
        pass

    def onCommand(self, sender, command, label, args):
        player_position = sender.getLocation()                      # Get the player's current position
        dir_unit_vector = player_position.getDirection()            # Get the player's direction unit vector
        target_position = player_position.add(dir_unit_vector)      # Calculate the target position

        world = sender.getWorld()                                   # Get the world object
        for i in range(0, 10):                                      # Iterate 10 times
            block = world.getBlockAt(target_position)               # Get the block at the target position
            block.setType(bukkit.Material.GOLD_BLOCK)               # Set the block type to gold
            target_position.setY(target_position.getY() + 1)        # Increment the y-coordinate of the target position

        return True