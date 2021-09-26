# API Additions

## By Matt

<br></br>
**Description**
<br></br>
Aside from re-structuring and slightly improving the API's overall codebase (particularly the ``RemoteSession.java``
file), I added some functionality to assist our group's needs.

NOTE #1: This is not a fully-fledged re-write, as I did not have the time for this. However, if time was not a constraint,
and interest prevailed, I would've re-written almost the entire codebase to make it very efficient, clean and practical.
I also would've added a lot more functionality, and better documentation.


NOTE #2: For this village generation to work properly, you need to make sure that you've set your ``LOCATION`` in the 
RaspberyJuice plugin's ``/plugins/config.yml`` to ``ABSOLUTE``, otherwise you will encounter problems.
<br></br>

**New Methods**
<br></br>
<b>getBiome()</b>
<br></br>
Usage: ``mc.player.getBiome()``
<br></br>
Args: None
<br></br>
Returns: A string representing the biome (i.e. ``DESERT``, ``BADLANDS`` ``BADLANDS_PLATEAU``, etc).
<br></br>
Description: <i>Get's the biome the player is currently in, and returns the biome in the form of an all-uppercase
string (invokes Enum Class' ``toString`` method on the constant).</i>
<br></br>

<b>removeBlocksInRegion()</b>
<br></br>
Usage: ``mc.removeBlocksInRegion(x1, y1, z1, x2, y2, z2, [types])``, where ``[types]`` is a list of block-ids to remove.
<br></br>
Args:
  - x1, y1, z1 (first corner of cuboid)
  - x2, y2, z2 (second corner of cuboid)
  - [types] (list of block-ids)
<br></br>

Returns: None
<br></br>
Description: <i>Removes all the blocks within a cuboid region, of the client's choice. The client can input as many
block-ids in the ``types`` list as they'd like. It performs this very fast, compared to doing it via the mcpi api with a
barrage of calls.</i>
<br></br>

<b>getHighestAndLowestYInRegion()</b>
<br></br>
Usage: ``getHighestAndLowestYInRegion(x1, z1, x2, z2)``
<br></br>
Args:
  - x1, z1 (first corner of region)
  - x2, z2 (second corner of region)
<br></br>
  - 
Returns: A tuple containing two ints: (highest_y_value, lowest_y_value).
<br></br>
Description: <i>Quickly finds and returns the highest and lowest y-values (as integers), respectively, within a client
selected region.</i>
<br></br>

<b>getLowestYInLine()</b>
<br></br>
**DEPRECATED AND MARKED FOR REMOVAL**
<br></br>
Usage: ``getLowestYInLine(x1, y1, z1, z2)``
<br></br>
Args:
  - x1, z1 (first corner of region)
  - x2, z2 (second corner of region)
<br></br>

Returns: An integer representing the lowest y-value in a line.
<br></br>
Description: <i>Finds the lowest y-value in a straight line going in the positive/negative z-direction only. Does not
support x-direction traversal. This method was created to assist in ensuring the roads were lined up straight, and was
used in tandemn with a simple flattening algorithm. However, it is not a very useful method, and can be avoided. In
fact, after changing the direction of the project, it was no longer used, but has not been removed from the API.</i>
<br></br>