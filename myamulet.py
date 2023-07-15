"""Parse NBT world files with Amulet API."""
import amulet
from amulet.api.errors import ChunkLoadError, ChunkDoesNotExist

level = amulet.load_level("mcworld")

try:
    chunk = level.get_chunk(0, 0, "minecraft:overworld")
except ChunkDoesNotExist:
    print("Chunk does not exist")
except ChunkLoadError:
    print("Chunk load error")
else:
    print(chunk)
    # Chunk(
    #   0,
    #   0,
    #   UnboundedPartial3DArray(dtype=<class 'numpy.uint32'>, shape=(16, inf, 16)),
    #   EntityList([]),
    #   BlockEntityDict()
    # )


# level.save()
level.close()