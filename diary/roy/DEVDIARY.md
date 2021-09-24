# Development Diary
This is a *template* for your dev diary in PS2.
Feel free to edit as you see fit e.g., based on your progress updates, hurdles encountered and circumnvented.
Make sure to log one comprehensive update per student, per each week of our teaching term.
Please, get in touch with teaching staff for any questions around this or otherwise post on Microsoft Teams.

# Mandatory Student's contributions
Please, specify your individual contributions to the project **as a percentage**. 
Default is a *25% contribution for each student*. However, please modify as necessary, if that is not the case.

# Development Diary Activities
Please, report your key activities in each week this assignment is running.  

**Week 1**
***project work:***
tested with designs of various buildings that will be used in the village, was later assigned with the role of creating various park like areas for the village
-group then decided that areas of land should be 15x15 blocks for convinence, so i designed my parks with that in mind
-made code for a basic fountain that is currently based on players position, with the plan to make it modular and accept x,y,z values and biome from main program to dictate where it will be built. then made pond park.
-tested creating modules with a 'park' class, after the reorganisation of files from Mathew.
decided that i would like a tree in one of the four corners of the park, so i created a function that would randomly select the coordinates of a corner, and randomly generate a tree there.
-thought that the park did not have enough nature, so functions, place_grass and place_flower were created, and they would randomly choose a x,z value in the park and place grass and a flower in that random coordinate

*** Studio class reading/work**
-set up working environment(spigot and mcpi that was given out) needed to work on the project
-tried out the tools by placing blocks in Minecraft via python files



**Week 2**
project work:
The team decided to call the objects that i was working on 'Misc" for clarity, and later i created the basic misc object, with the aim to make it compatible with the main function.
the team also decided that instead of making a village type for every biome, we would only have three types of 'themes', that being 'modern' for plains, 'medi' for desserts and 'magic' for the rest.
-with jins help, created block list for each theme for the 'misc' objects using Jins block list file, later changed my block list to use only the block id's as it was easier.
-realised that the code for the grass and flower placement was pretty much the same, so i took the code out that decided the random placement of the items and made a new function called random_placement.
-created three more misc objects throughout the week: a large tree that will have a random height, a chess board and modern art
-errors occured when modularising the code, meaning i had to spend quite of time changing things, luckily i mannaged to make all of the 'misc' objects inherit from the min class.
- started makeing the builder function, that imports all of the child misc classes, and randomly build one of them at a given x,y,z coordinate.
    encontered problem with the way the Misc parent class as coded, and how i decided to pass the buildig functions to the main program
        - originally aimed to have main program pass the x,y,z and biome to build functions, however the parent class contained functions that build the foundations of the Misc object, and could not see a way to pass the theme from main program to the parent class at the current time.
            -later decided to just use import the theme checking function that lachie made into the parent class file, and use the theme as a variable all child classes would inherit.
- tested various ways that i could use to make the builder function
    -this included placing the build function into the parent class, which ended in failure due to circular import
        - did not see this working anyway
    -tried importing the theme though the basic build file, and did not work, and then thought it would take too much time to actually implement that way
    -thought about just getting the main program that mathew was working on to import all of the Misc classes, but then decided against that as it seemed like more work
    
    after testing those options, finally decided to just import the theme checker into the parent class for convinience 
-completed the builder function, now known as builder.py,  has not been tested with main function, but it should work

**Week 3**
project work
-started on decorations for the property objects, with template code given by jin
- created flowerbeds, vegetable gardens and a tree in the simplest form, unsure whether to make them more complex

.....
.....
.....
