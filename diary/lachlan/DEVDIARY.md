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
* Lachlan
    * Setup VSCode, and Minecraft on Windows 10
    * Successfully implemented Minecraft Tools by allowing a server connection between localhost and minecraft java edition, as well as ensuring the MC_Py_API works correctly.
    * Assisted other students in ensuring that they have all the tools required for commencing the project, as well as providing shortcuts for optimisation within the API.
    * Completed the participation activity for building a brick staircase, as well as tested various other functionalities with the MC_Py_API, resulting in creation of ideas such as teleportation, house making, path making, terrain scanning, and a clock (done to test numpy and time module support, as well as learning the MC_Py_API commands).
    * Read chapter 1, 2, & 3 on Computer Architecture textbook.
    * Completed the decimal, binary, and hexadecimal practice questions.
    * Created a discord channel alongside my team in order to note down rough strategies and milestones that are not major enough to be published on teams, as well as communicate ideas more informally.
    * Collaborated with my team in order to devise strategies for tackling the first assessment (how would the village be generated? who is going to do what? what are the requirements? etc)
    * Created an outline of how the project will be undertaken, giving key milestones to each group member as to what needs to be completed by each week in order to stay on track and move on with steps in an order that makes sense.
    * Completed my first major task for the week of making templates for all the roads present in the village (accounting for all possible oreintations, curves, and intersections)
    * Successfully created straight, curved, and intersected roads for the village using the MC_Py_API
    * Successully created a terrain scanning program that gets the block height of the highest block in specific x,z coordinates within a given matrix (will be used within the village generation to test for whether the target spawn area is acceptable or not for a village)
    * Tested the efficiency of numpy arrays against python lists using the terrain scanning program I built. The conclusion through testing was that numpy arrays have a much more efficient runtime than python lists do, as well as take up less memory.
    * Currently working on producing different randomised structures depending on the results of the terrain scanning program. I.E if terrain is suitable for building, place a random road template in a certain position within the scan. This will be important for later implementation of our matrix.
**Week 2**
* Lachlan
    * Fully completed the terrain scanning program which can be implemented into the program to account for placement in awkward positions (on the ocean, in the sky, over a mountain, etc)
    * Collaborated with Matt to create and optimise the matrix generation method we have decided on.
    * Created a biome-to-theme program that picks up the biome the player is, and then assigns a theme to it, which can be used to decide the blocks in the structures generated within the village.
    * Assigned tasks and deadlines to group members in order to stay on track with what needs to be finished by when (I.E being able to test generation with houses, misc, and roads, by Week 2 Friday, and be completely finished ideally by Week 3 Monday, latest Week 3 Wednesday, ready for recording and submission by Week 3 Friday.)
    * Watched all required videos on linkedin learning for cybersecurity.
    * Completed participation activities for cybersecurity.
    * Assisted Jin in the creation of houses using the MC_Py_API, allowing for randomisation of structure, pools, and interior design.
    * Implemented the terrain scanning program and the biome-to-theme program into the main repository, constructing them in a way that will allow module access by any other file.
    * Added T-intersections to the roads file to allow for more flexibility in road generation.
    * Downloaded and tested Kali Linux using VirtualBox.
    * Completed roof and wall structure for house generation, blocks can be substituted in and out per theme, and designs are randomised and account for each others dimensions (roof builds according to dimensions of walls) to fit criteria.
    * Used Kali Linux through VirtualBox to capture TCP packets being communicated between Kali Linux and Windows on the same machine (this was done using wireshark).
    * Re-read chapter 3, as well as chapter 4, on Computer Architecture textbook.

**Week 3**
* Lachlan
    * Reconsidered path design in order to fufill criteria better (perhaps doing a 9 block wide path with blockages on the side is not worth it when compared to doing a 5 block wide path with no blockages that can scale terrain)
    * Thought about and tested solutions to the environment conservation problem (how will we get houses to generate in natural ways when their positions are predetermined by the matrix?)
    * Created East/West and North/South paths that can scale any terrain (more mark efficient than previous design), this was done using the same algorithm I implemented in the terrain scanner last week, which is what allowed the efficient scalability
    * Tried out using the math import to do vector calculus in minecraft (if we were able to find the base of the mountain on top and bottom, we could build the path going upwards in a way where it doesnt excavate terrain), in the process this would allow us to build houses in practically any position and connect them to paths accordingly. This is something Matt and I will work on throughout the week most likely
    
.....
.....
.....
