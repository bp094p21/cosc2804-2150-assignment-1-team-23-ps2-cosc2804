# Development Diary

by Jin Heock - S3491222

1. [[#Contributions]]
2. [[#Activities]]

# Contributions
Working on 100% of `property` subpackage.

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
 - Install correct version of Java
 - Install spigot server
 - Install Minecraft Java edition API

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
 - Add easier to read print messages for a better dev experience

Testing
 - Getting into the habit of writing "if name is main" tests at the bottom of every file to easily test main functionality of each file
 - Tested `architect.py`, `layout.py`, `builder.py` and `designer.py` and they are all working as intended together
 
# TODO: Make sets of suitable blocks for each component for each house_type for each theme

## Week 3

Learning
