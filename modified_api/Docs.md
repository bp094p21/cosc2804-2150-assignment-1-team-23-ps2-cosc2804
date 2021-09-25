# API Additions
## By Matt

**Description**
Aside from re-structuring and slightly improving the API's overall codebase (particularly the ``RemoteSession.java`` file), I added some functionality to assist our group's needs.

NOTE: This is not a fully-fledged re-write, as I did not have the time for this. However, if time was not a constraint, and interest prevailed, I would've re-written almost the entire codebase to make it very efficient, clean and practical. I also would've added a lot more functionality, and better documentation.

**New Methods**
* <b>getBiome()</b>
Usage: ``mc.player.getBiome()``
Args: None
Returns: A string representing the biome (i.e. ``DESERT``, ``BADLANDS`` ``BADLANDS_PLATEAU``, etc).

Description: <i>Get's the biome the player is currently in, and returns the biome in the form of an all-uppercase string (invokes Enum Class' ``toString`` method on the constant).</i>

* <b>removeBlocksInRegion()</b>
Usage: ``mc.removeBlocksInRegion(x1, y1, z1, x2, y2, z2, [types])``, where ``[types]`` is a list of block-ids to remove.
Args:
- x1, y1, z1 (first corner of cuboid)
- x2, y2, z2 (second corner of cuboid)
- [types] (list of block-ids)
Returns: None

Description: <i>Removes all the blocks within a cuboid region, of the client's choice. The client can input as many block-ids in the ``types`` list as they'd like. It performs this very fast, compared to doing it via the mcpi api with a barrage of calls.</i>

* <b>getHighestAndLowestYInRegion()</b>
Usage: ``getHighestAndLowestYInRegion(x1, z1, x2, z2)``
Args: 
- x1, z1 (first corner of region)
- x2, z2 (second corner of region)
Returns: A tuple containing two ints: (highest_y_value, lowest_y_value).

Description: <i>Quickly finds and returns the highest and lowest y-values (as integers), respectively, within a client selected region.</i>

* <b>** DEPRECATED AND MARKED FOR REMOVAL** getLowestYInLine()</b>
Usage: ``getLowestYInLine(x1, y1, z1, z2)``
Args:
- x1, z1 (first corner of region)
- x2, z2 (second corner of region)
Returns: An integer representing the lowest y-value in a line.

Description: <i>Finds the lowest y-value in a straight line going in the positive/negative z-direction only. Does not support x-direction traversal. This method was created to assist in ensuring the roads were lined up straight, and was used in tandemn with a simple flattening algorithm. However, it is not a very useful method, and can be avoided. In fact, after changing the direction of the project, it was no longer used, but has not been removed from the API.</i>