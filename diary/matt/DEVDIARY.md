# Matt's Development Diary
## Student Code: s3902219

### NOTE: The order of entries is not chronological.
<br></br>
**Week 1**

* Read chapters 1, 2 and 3 of the Computer Architecture with Raspberry Pi's book.


* Completed number system conversion questions.


* Wrote numerous guides to assist those having trouble with getting set up.
    - How does the Spigot API, Minecraft, RaspberryJuice and MC Python API work and interact.
    - What Java versions do you need, where to download them (plus personal recommendations) and which version of
      Minecraft & Spigot maps to which Java version.
    - How to alter the java command-line startup flags for the ``start`` executable, so that the 20-second cool down can
      be omitted and the second white Mojang server gui is not displayed. As well as how to close the server properly to
      avoid "this port is already in use" issue.


* Setup Pycharm on my MacBook, and VSCode on my Windows laptop to allow familiarity when presenting code snippets to
  other team members. The programming is done on my MacBook, whilst running Minecraft and the Spigot Server is handled
  on the Windows machine. Files are shared via a dropbox server.


* Forked RaspberryJuice and the Python Minecraft API to add in a setBiome() method, as well as clean up, restructure,
  update and improve the codebase. Wrote detailed documentation for the team on how to install this new forked version,
  to ensure a smooth transition.


* Spent countless hours envisioning a design for a central framework, so that all components can work together smoothly.
  Drew a class diagram on paper, and various other forms of diagrams. See the Excel document embedded within this
  directory for a high-level overview with lots of visuals.


* Hosted a meeting discussing the framework design, and running through the idea to teammates, whilst being open to
  constructive criticism and alterations.


* Discussed code conventions with team to ensure consistency, and organised project structure.


* Collaborated with team to allocate duties, discuss central questions and design concerns, as well as to get a plan
  going.


* Set up the discord server to be conducive to a team environment, with multiple channels dedicated to this project.
  Created a webhook to integrate into a particular channel "commit-log", so that all pushes and their commit messages
  are logged there. This way, the team can be notified when someone pushes some changes, so that they can pull them
  before they begin their coding session, thereby, avoiding merge conflicts.


* Implemented the bare bones of the framework; file structure, modules and some code, design patterns and decisions, and
  general layout.

<br></br>
**Week 2**

* Completed the Kali-linux studio class, and used wireshark to inspect incoming and outgoing packets.


* Did research on DIMM vs SIMM memory, and the different models to further consolidate chapter 3 of the textbook. Also
  watched the LinkedIn videos and read Chapter 4 of the textbook.


* Spent time integrating all the sub-programs that were ready. In the midst of this, I also cleaned the code as much as
  possible, and optimised it if applicable. The sub-programs that were subject to this treatment were, but not limited
  to: terrain_scanner, road code, etc.


* Modified the RaspberryJuice plugin and the McPi Python API to make it slightly more efficient. I also attempted to
  swap out the updateBlocks() method (responsible for updating blocks on the backend) with a nms-altering (**N**
  et.**M**inecraft.**S**erver) variant, which would alter the internals of the traditional Mojang Minecraft Server
  release. To be specific, it modified the chunk's data palette (allowed for around 14 million blocks to be placed per
  second, real-time). This caused some problems however, as it did not perform lighting update and required the server
  to be restarted, since it did not receive a proper dynamic update. Hence, I another variation, which was much slower,
  but did not have the disadvantages of the rest:

  ``` 
    public static void setBlock(World world, int x, int y, int z, int blockId, byte data, boolean applyPhysics) {
       net.minecraft.server.v1_12_R1.World nmsWorld = ((CraftWorld) world).getHandle();
       BlockPosition bp = new BlockPosition(x, y, z);
       IBlockData ibd = net.minecraft.server.v1_12_R1.Block.getByCombinedId(blockId + (data << 12));
       nmsWorld.setTypeAndData(bp, ibd, applyPhysics ? 3 : 2);
  }
  ```

    Feel free to use this if you'd like.
    
    <br></br>There are better, faster solutions out there that I am also aware of, however, they require too much work to integrate
    and become increasingly more complicated as Mojang releases new Minecraft versions due to heavier obfuscation of the
    source code and the sub-systems changing significantly, and frequently. Hence, in the interest of time, I decided to
    just settle for the above.

    <br></br>However, to my mistake, I accidentally installed the wrong version of build-tools, due to not being focused at the time.
    And by the time I realised, I was far into this, and was a little demotivated to continue. More importantly, time was
    running thing, so I just scrapped this whole idea after some thought and looked elsewhere for optimisations.
    
    <br></br>FYI: BuildTools takes a logon time to build, and it's a mission to install it for different versions. Note for future -
    make sure you install BuildTools for 1.16.3 and NOT 1.12.2, since the spigot server ultimately is ported for 1.16.3.
    
    <br></br>After some thinking, I discovered a better form of optimisation, which was to move all the expensive calls to the
    back-end, to avoid the bottleneck of requests being transferred through the sockets (there is a 9000 request limit I
    believe, and it becomes quite slow). Repeated calls were not the way to go, and Java is a fast language to perform the
    computation quickly. Doing so also allowed me not to resort to batch processing or any forms of multithreading or
    micro-optimisations, which saved time. In doing so, I also added additional methods to the API (for a full list, check
    the <b>API Additions</b> heading).


* Designed all the small, medium and large layouts and altered the Excel document so that these would be detailed. To
  see this Excel document, please view ``Village Layouts.xlxs``.


* The majority of this week was spent brainstorming ideas, and designing systems that would later be tested/implemented
  in week 3. A few of these ideas were:
    - The roads could take one of two approaches:
      <br></br>**Easy Way**<br></br>
      Pros:
        - Its easy and will only take about a day to implement properly.
        - This is kinda the same style that minecraft has with their villages.

      Cons:
        - Does not look very clean, and does not account for heights greater than 1 (this goes against the criteria
          cause it says, players can walk along the roads without having to build or destroy blocks).
        - The code is somewhat ugly.

      <br></br>**Hard Way**<br></br>
      Pros:
        - Very elegant and looks super nice.
        - Can account for heights greater than 1 and will carve out a path if need be. All steps are uniform and flush
          with each other. The player won't have to build or destroy blocks to get around.

      Cons:
        - Difficult to implement and will take time if I'm doing it alone.
        - Will probably not have time to do the pathfinding thing.
        - Not 100% if I will be able to finish this and all the other stuff I still need to handle.
      <br></br>
    - Started looking into pathfinding and derived a solid plan to get full marks:
      <br></br><i>NOTE #1: A fair portion of this is discussed in <b>retrospect</b>, as the timeline of these events are far too
      messy to be 100% accurate.</i>
      <br></br>I would've used Dijkstra's Algorithm because it allows for weighting, such that I would make it prefer to go
      around mountains instead of over, and to avoid water/lava if possible. In addition, it is better tailored for
      multiple destinations unlike a*. Breadth First Search was also applicable, however, it lacked the niceties of the
      weighting system.
      <br></br>Lachlan's terrain scanner would scan each plot (15 x 15) and check if the land is suitable to place a house. If it
      is suitable then it will identify that plot in the matrix with a number (or enum). If it was not suitable, it
      would identify that. That way, all houses would be randomly placed. Then, with a pathfinding algorithm, would
      iterate through the matrix of plots, and then the first one it finds would be the source, while the others would
      be destinations. The destinations would be added to a list for later use. Then the pathfinding algorithm would
      find the cheapest (depending on allocated weights as mentioned above) route to all houses, so that they are all
      linked in some manner. Once the path is found, it would then simply draw the roads by replacing the blocks and
      enforcing the gradient of less than or equal to 0.5 system to ensure 1-block increments in the elevation.
      <br></br>Another alternative, presented by Lachie (occurred in week 3, but detailed here to keep topics consistent), was to
      heavily weight against mountains where the y-level increments are inconsistent (i.e. greater than 1), so that the
      pathfinder would very rarely go over mountains, and it would prefer to go around them. However, the downfall to
      this was that houses would then not be built on top of mountains. While practical and doable, it was not ideal.
      This would've been the fall-back option if the former option failed.
      <br></br><i>NOTE #2: None of these ideas were implemented or tested yet. This was just planning to solve many issues I
      personally encountered before reaching out to fellow teammates to get assistance. I had many solutions, but as you
      will read, none of them turned out to be feasible within the timeframe.</i>
    <br></br>
    - Tried to conceive a way to ensure houses are nicely placed in the terrain. Two approaches were discovered:
        1. They can be placed at the smallest y-block within a 15x15 plot (cutting into mountains - works well for
           non-mountainous biomes though).
        2. Alternatively, they can be placed on the highest y-block and the floating bits would be filled with the
           material under the house so that it blends in naturally with the terrain. To prevent a very abnormal
           look, complexity would be added, such that it bulges slightly, and it is not just a straight square of
           blocks (it blends with the mountain). However, this is only for mountains, and would not be a problem for
           houses that are not spawned on the edge or side of mountains.


* Altered the sizes of the plots because they were far too large to begin with, and the terrain_scanner would not allow
  placement in approx. 80% of test cases. Hence, I installed the WorldEdit plugin and played around with different
  sizes. This allowed for a more informed, and realistic perspective of the actual magnitude of each dimension, unlike
  the former attempts where mere guesses were deemed adequate. After some extensive testing, I discovered some
  reasonable dimensions and altered the Excel document's contents accordingly. Once that was complete, I then
  implemented it within the core sub-package's codebase.


* Made further progress on the village generation system, optimised and cleaned up the code.

<br></br>
**Week 3**

* Early this week, I felt overwhelmed with the amount of problems encountered along the way. It was too much to handle
  by myself, otherwise, I would not have finished. Hence, I consulted with Lachie, and he generously aided me in
  brainstorming new ideas, testing them and coming up with various plans throughout the week (as detailed below).


* In attempt to rectify the dilemmas associated with variable y-levels, multiple solutions were conceived: pathfinding,
  linear algebra, simple algorithms, navigation meshes, etc. A brief description of each idea will be detailed below.
  However, the full extent of these ideas, and the exhaustive testing that was carried out will not be explored in-depth
  to reduce the amount of lines in this document, and as well as due to being on a strict time constraint.
  <br></br>
    - Implemented, and thoroughly tested an a* pathfinding algorithm. However, the idea was scrapped due unreasonable
      levels of difficulty in relation to accomplishing the task within a very limiting time frame. In addition, it
      required me to alter the entirety of the system and start over, which is obviously not a feasible task in the
      third week.
    <br></br>
    - Implemented a ramp system using gradients and basic linear algebra (and vector calculus) to combat the 1-block max
      height increment issue. To no surprise, the idea was ditched because the plot-based matrix system did not align
      with this level of thinking. To implement such a system using the existing system, the roads would have to be
      connected via an ugly recursive node system.

  <br></br>Nonetheless, the gist of the idea is a ramping system. The ramps would be filled with bricks all the way down, until
  it the bricks touched the ground (think a bridge with pillars to keep it up-right). This prevented floating stairs.
  First, the idea was to calculate the gradient of two 3D points (using the x, and z mapped to the y-axis respectively),
  and if it was over 0.5 (too steep), then push out the z OR x coordinate (depending on player orientation) by 1 block,
  until that gradient is either 0.5 or below. This would continue until the gradient satisfied the condition of being
  equal to or less than 0.5. This number is unique because it allows the roads to then be built with a maximum of
  1-block height increment (like a normal staircase).
  <br></br>However, this idea later transitioned into a plot-based system, so that it could be interoperable with the current
  design. Instead of pushing out the z/x coordinate by 1 block, it would,rather, select the next road plot. So, if one
  road plot's road could not scale the mountain, while enforcing a 1-block-max height increment, then the next road plot
  would be chosen, and the gradient re-calculated. The next road would most likely (in most cases) be able to scale the
  mountain while enforcing this requirement. However, as mentioned above, this required a recursive node system, where
  roads were connected to other roads (on the logical level), and it was just not a feasible task to get this working in
  5 days. Moreover, it was rather messy, and there is definitely a more practical solution that awaits, given sufficient
  time. Therefore, the idea was, yet again, abandoned.
<br></br>
    - An alternative approach to the aforementioned road problem was also tackled from a more algorithmic, imperative
      approach. An algorithm that flattens the land based on the smallest block in a strip (hence the
      getSmallestYInLine() method - now obsolete) and enforces a 1-block height maximum via retaining the previous
      y-value and checking, consecutively, if the y-values for 2 increments (in the z/x direction) were less than or
      equal to 1 block. Once again, the idea was deserted. This was due to it digging into the terrain, and causing
      alignment problems with houses and roads not being on the same y-levels, even though their corresponding x/z
      values were aligned correctly.
  <br></br>In addition, Lachie also had an attempt at this, which was more successful than its former (developed by myself), and
  made use of his modular, and re-usable terrain_scanner. However, it dug into the terrain more than the former, and
  also dissatisfied the same criteria its predecessor did, thus, also being ditched.
  <br></br>This was a painstaking process because along the journey, I had to recode the roads at least 3 times in different
  ways. Hence, a lot of time was wasted in this pursuit.
    <br></br>
* The continuation of modifying the API once again to add 3 new methods took off here. The most notable was the removal
  function to assist the powerful terraform, ensuring a better time and auxiliary space complexity. As already
  mentioned, but for further clarity, the sockets proved to be a bottleneck, hence implementation of removing blocks and
  finding the highest and lowest y-blocks was moved to the backend to ensure only one call was made over thousands.


* I further looked into pathfinding and obtained an in-depth understanding of breadth first search, dijkstra's algorithm
  and a*. I then transitioned into learning about navigation meshes, and attempted to re-do the entire framework and
  system, however, soon realised that it was an impossible task with only 5-6 days left. Thus, I undid all of my work
  and consulted with Lachie to come up with another plan. Unfortunately, much of my work never made it past a <b>GitHub
  stage</b>, hence a lot of it was lost to time. In retrospect, this was a terrible idea, because I later needed to
  revisit some ideas and code that I had written, but I could not retrieve it since it was only stored locally, but then
  deleted. The lesson learned was to always take advantage of version control - even if you change your mind.


* Altered the structure of all the components outside the core sub-package (except for property) so that they worked in
  unison with the framework. Further, I optimised and cleaned up the code, while altering the imports. Python's package
  system sucks :(. So unnecessarily complicated at times, and very platform dependent. Anyway, that's a discussion for
  another time.


* Implemented the large and medium village schematics fully.


* Implemented all the building of components to replace blocks and cater for different y-levels (similar to how
  minecraft villages do it). Ah, yes - another unforeseen caveat! I discovered that it was far too slow because the road
  code is not as efficient as it could be, in conjunction with the fact that ``mc.getHeight()`` is an expensive call and
  was being invoked excessively. A re-write of all the roads with time complexity in mind could solve this issue,
  however, this is unwise with only 5 days left, as it is a weighty task. AS per usual, a different course of action was
  taken. We decided to just decimate the land, flattening everything, and not accounting for different y-levels. This
  was very disheartening, because a lot of work had been poured into getting this working, and the only factor
  preventing them from flourishing was a poor start and disorganisation, which eventuated into a stressful last week of
  trying to cram potential ideas into the code (obviously did not work because you need more time). All in all, it is
  definitely a lesson learned for the next project.


* Fixed a small hiccup with intersection code, preventing it from digging into the ground level layer. It was not the
  nicest solution and could easily be avoided with better design decisions, although there is not enough time for Lachie
  to re-write the roads and that would be too stressful.


* Reformatted and refactored the entire project's codebase so that it was up to the python formatting conventions, and a
  lot easier to digest for you guys (the markers!). Removed unnecessary modules and old, obsolete code. Added comments
  and doc strings where necessary.


* Spent time altering all the imports so that the project could work properly, because some major sub-packages did not
  have their imports relative to the overall project structure. This was unfortunately, a very lengthy, excruciating
  process.


* Cleaned up the code, and altered parts to get it functioning with the village generation system.