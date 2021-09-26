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
    * Fully completed the terrain scanning program which can be implemented into the program to account for placement in awkward positions (on the ocean, in the sky, over a mountain, etc)
    * Collaborated with Matt to create and optimise the matrix generation method we have decided on.
    * Created a biome-to-theme program that picks up the biome the player is, and then assigns a theme to it, which can be used to decide the blocks in the structures generated within the village.
    * Assigned tasks and deadlines to group members in order to stay on track with what needs to be finished by when (I.E being able to test generation with houses, misc, and roads, by Week 2 Friday, and be completely finished ideally by Week 3 Monday, latest Week 3 Wednesday, ready for recording and submission by Week 3 Friday.)
    * Watched all required videos on linkedin learning for cybersecurity as well as completed participation activities for cybersecurity. While the communicator for the content in the linkedin videos was dry and was using jargon that I'm sure not many of the students were familiar with, I personally found all the content interesting and found myself spending the rest of the day looking at different threat management strategies and potential sources for these threats. 
    * Assisted Jin in the creation of houses using the MC_Py_API, allowing for randomisation of structure, pools, and interior design.
    * Implemented the terrain scanning program and the biome-to-theme program into the main repository, constructing them in a way that will allow module access by any other file.
    * Added T-intersections to the roads file to allow for more flexibility in road generation.
    * Downloaded and tested Kali Linux using VirtualBox.
    * Completed roof and wall structure for house generation, blocks can be substituted in and out per theme, and designs are randomised and account for each others dimensions (roof builds according to dimensions of walls) to fit criteria.
    * Used Kali Linux through VirtualBox to capture TCP packets being communicated between Kali Linux and Windows on the same machine (this was done using wireshark).
    * Re-read chapter 3, as well as chapter 4, on Computer Architecture textbook. While a lot of the concepts here are abstract for the time being and a lot of jargon I am not familar with is being used, I comprehended enough of the basics in order to build a solid foundation, alongside my previous knowledge of cpu's and memory, in order to sufficienctly participate in next weeks activities. 

    ||This is an edit from the end of Week 3:||
    In retrospect, this was the week that Matt and I had come to the conclusion that our village generation was insufficient for some of the criteria requirements, more specifically, allowing village generation have multiple y levels, and in the process, not destroy terrain in order to place the builds. We spent hours brainstorming together on possible solutions to this problem, such as calling in different y levels of roads and using the ending y levels for that road as the starting y levels for another build, however this proved to be an inefficient solution as we could not figure out how to get roads to move downhill when they're seperated into 15x15 plots. While the matrix idea was a good idea for efficient and easy randomised generation, it was impossible to work with when it came to moving in the y direction. Realising this, we decided to journey down the path of pathfinding using astar, and while hopeful at first, as it did not take very long to get the pathfinding algorithm to work in 2 dimensions (x and z), we again ran into a roadblock when we attempted to move it in the 3rd dimension, as blocks would be skipped, terrain that was ok to path on was deemed as insufficient by the algorithm. Had we worked on this in Week 1 and gotten Roy and Jin involved, I believe we would have been able to use this alternative and likely scored better as this would have been used in conjuction with a modified version of my terrain scanner in order to find areas of land that are suitable for a house, however changing our entire system when houses had already begun being created using this system would be a nightmare, and is just not possible to do within 1 week. After a few days of stressing and testing with Matt, the 2 of us and Jin, who had been vigorously working on houses while we were testing different possibilities for proper generation, all came to the agreement that we should just stick with our original idea, as such we were able to complete our village generation like orginally intended. This is something we should remember for the rest of our course, as this is the result of not truly thinking ahead of big ideas before doing them, and I'm sure we will be spending much more time devising an outline of how everything will work right from the get go.

**Week 3**
* Lachlan
    * Reconsidered path design in order to fufill criteria better (perhaps doing a 9 block wide path with blockages on the side is not worth it when compared to doing a 5 block wide path with no blockages that can scale terrain)
    * Thought about and tested solutions to the environment conservation problem (how will we get houses to generate in natural ways when their positions are predetermined by the matrix?)
    * Created East/West and North/South paths that can scale any terrain (more mark efficient than previous design), this was done using the same algorithm I implemented in the terrain scanner last week, which is what allowed the efficient scalability
    * Completed participation activity for Studio Class 1. In doing so I become more knowledgable on the function of memory within a computer system, as well as the difference between DRAM and SRAM. I consulted the Computer Architecture textbook once more after this class in order to further read upon concepts I was not familar with, or jargon I was not familiar with, within the memory chapter I had previously read last week. Furthermore I downloaded CPUID, a software that accesses details of your pc on an advanced level, such as returning to me what DDR my RAM sticks were (they are DDR4). With this knowledge I can further look into compatability between different components within my machine in order to make future upgrades.
    * Tried out using the math import to do vector calculus in minecraft (if we were able to find the base of the mountain on top and bottom, we could build the path going upwards in a way where it doesnt excavate terrain), in the process this would allow us to build houses in practically any position and connect them to paths accordingly. This is something Matt and I will work on throughout the week most likely
    * Tested the A* (AStar) path finding algorithm to use in place of our regular road designs in order to accomondate for extreme mountain terrain taking the best path, proved to be a waste of time as it appears to be impossible to force natural generation in extreme mountain terrain within such a short time frame, had we known that this was a preferable alternative to our currently used road generation and instead done this in Week 1, this would have been likely to have worked.
    * Created a seperate version of the terrain scanner that will search plots (15x15) in the matrix for suitable places to build houses, and if the village cannot generate 3+ houses, then the village will not be spawned
    * In the end we collaboratively decided to not go with most of these new ideas and instead have gone back to our old design that suited better with the matrix, which is unfortunate given the amount of hours and code put into them, however it should be treated as learning experience to think more in depth on the consequences of big decisions before making them
    * Created a border around the village that is determined by the dimensions of the village. This is done in order to prevent liquid from seeping in from the surroundings into the village upon generation.
    * Completed participation activity for Studio Class 2. In this activity we practiced budget management against CPU's, deciding what was the best decision based on the performance vs cost metrics. By doing this activity, as well as using my knowledge from the previous activity on memory, I played around with pcpartpicker in order to try and grab the most cost vs performance efficient parts that are compatable with each other. While this will take more time to completely master, this week has been really useful in pushing me along with computer engineering knowledge.
    * Collaborated with team to create slides that would provide as a sufficient guide during recording to present our village to the marking criteria.
    * Worked with Jin in order to fix some last minute bugs with generation in order to have consistently well spawned villages on a random basis.
    * Collaboratively recorded and submitted our village.
    * Read up on the concept of levels of abstraction in preperation for next week, as well as viewed and attempted to comprehend the memory map presented in the first class of Week 4. With this minecraft village assignment out of the way, a lot of stress has been taken off my shoulders, and I can spend a majority of my focus on reading the Computer Architecture book more in depth in order to understand the more abstract concepts beyond the basic knowledge that has been learnt, at least for the time being.
    
.....
.....
.....
