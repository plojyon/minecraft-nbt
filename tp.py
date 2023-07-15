"""Change player's position in level.dat"""
import amulet_nbt

level = amulet_nbt.load(
   "mcworld/level.dat",
   compressed=True,  # These inputs must be specified as keyword inputs like this.
   little_endian=False,  # If you do not define them they will default to these values
)
player = level["Data"]["Player"]

new_pos = amulet_nbt.TAG_List([
    amulet_nbt.TAG_Double(1462.5),
    amulet_nbt.TAG_Double(74.0),
    amulet_nbt.TAG_Double(-949.5),
])

print("old_pos", player["Pos"])
player["Pos"] = new_pos
print("new_pos", level["Data"]["Player"]["Pos"])

level.save_to(
    "level.dat",
    compressed=True,
    little_endian=False,
)
