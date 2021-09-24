# Development Diary

by Jin Heock - S3491222

1. [[#Contributions]]
2. [[#Activities]]
3. [[#Credits]]

# Contributions
Working on 100% of `property` subpackage with minor contributions from Lachlan and Roy. See [[#Credits]]

Github commits under bp094p21 & fibretothepremises.

# Activities

## Week 1

Learning
 - Read chapter 1 & 2 on textbook
 - Setup VS Code, and Minecraft on my Macbook
 - Learnt about the Minecraft game mechanics
 - Learnt the Minecraft API
 - Learnt about the order in which blocks are enumerated with the `mc.getBlocks(...)` method call
 - Learnt about setting particular game rules such as `gamerule doDayLightCycle false`
 - Learnt about setting particular server properties to improve the development experience such as setting
	  `spwan-monsters` to `false`

Playing
 - Played some Minecraft and built some blocks manually

Installing
 - Installed correct version of Java
 - Installed spigot server
 - Installed Minecraft Java edition API

Collaborating
 - Got on a Minecraft server with Roy to build a house together manually

Implementing
 - Added class structures
 - Added basic program for the `build()` function for the `Property` class
 - Added printer utility to provide feedback to user on build status
 - Added orientation capabilities to component building

Testing
 - Tested functionality of Property build function
 - Tested functionality of Component build function

## Week 2

Learning
 - Went through each block from 0-255 and learnt about each one and their variation
 - Learnt about the `random.choice()` function to choose a random item from a list
 - Learnt a lot about OOP - class inheritance, how importing statements behave depending on what file you're running and who's importing what from where.

Designing
 - Added appropriate blocks to use for each component for 'medi' theme

Implementing
 - Added Basic layout for a property with start and end values in the x and z direction for each component
 - Drafted up suitable themes for the properties
 - Drafted up suitable house types for each theme
 - Drafted up possible themes for property
 - Drafted up sets of distinguishable blocks to use for each theme
 - Implemented and tested build functions for Entrance and Floor class
 - Modified classes so that classes that represent inanimate objects such as house components ('gate', 'wall') do not contain functions. They now only contain attributes
 - Added classes that represent objects that have the ability to "do". These classes use objects to query for design specs and appropriate blocks to use to build with
 - Finished main module `architect.py`
 - `property` subpackage working with basic functionality
 - Added functionality to `layout.py`, `builder.py`, and `designer.py`
 - Added easier to read print messages for a better dev experience
 - Added method to design stair components
 - Added method to build stairs
 - Added `orientate` function to set component positions based on property orientation
 - Add wall wrap designing function

Testing
 - Getting into the habit of writing "if name is main" tests at the bottom of every file to easily test main functionality of each file
 - Tested `architect.py`, `layout.py`, `builder.py` and `designer.py` and they are all working as intended together
 - Tested component designing for gate, fence, floor, pool and stairs and they are working as intended

## Week 3

Learning
 - Learnt about difference between `__str__` and `__repr__`
  - concensus:
   - `__repr__` is for developers and to be as comprehensive to provide info of object
   - `__str__` is for clients to provide simple readable feedback
 - It's very annoying to assign new objects inside a for loop because it gets overridden every time. TODO: learn more about this
 - Learnt about the difference between `__new__` and `__init__`
  - `__new__` is what creates an instance of the class and returns that object
  - `__init__` is the code that is run after the object is instantiated and that is why it doesn't return anything

Implementing
 - Added layout randomizer functions for pool gate, fencing, house door placements, and outdoor paths
 - Added component designing functions for pool gate, fencing, house door and outdoor paths
 - Added layout randomizer function for internal walls
 - Added component designer for internal walls
 - Tweak `roofer.py` to use given style of stair, slab and cube blocks to be used for roof building
 - Added dictionary for different roof blocks
 - Added window layout designing func
 - Added window component designing func
 - Added window component specs
 - Added window making func
 - Added door layout/design/specs/building code
 - Added steps layout/design/specs/building code
 - Added outdoor features layout code
 - Added veggie patch, flower bed and tree designing/component specs code
 - Added bed layout/design/specs/building code
 
Collaborate
 - Got assisstance from Roy to contribute code to build veggie patch, flower bed and tree components with mcpi

Fixes
 - Fixed poolside window positioning for house position middle.
 
Testing
 - Successfully tested automatic creation of entrance, paths, floors, walls, house doors (need further improvement with orientation), stairs, pool lining, pool filling, pool fence & gate
 - Successfully tested internal wall building for all orientations and possible house layouts
 - Amended house layout randomisation range to accomodate for internal room sizes
 - Successfully tested roof component designing and building
 - Successfully tested door layout,design,building for all orientations
 - Successfully tested step layout,design,building for all orientations
 - Successfully tested outdoor feature generation for all orientations
 - Successfully tested bed generation for all orientations and floor elevations
 
 Refactoring
  - Refactored `architect.py`
  - Refactored `layout.py`
  - Refactored `theme.py`
  - Refactored `property.py`
  - Refactored `block.py`
  - Renamed e and c references to z and x for easier understanding
  - moved `_orientate` function to `util` subpackage and renamed to `orientate`

Documenting
 - Added docstring to `architect.py`
 - Added docstring to `block.py`
 - Added docstring to `layout.py`
 - Added docstring to `theme.py`
 - Added docstring to `designer.py`

## Credits
Contributions from Lachlan.
 - particularly on `components/roof.py`, `components/wall.py`, `components/roofer.py` and `tradies/mason.py`

Contributions from Roy.
 - particularly on `tradies/gardner.py`