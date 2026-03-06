#DEVELOPER JOURNAL:

CONNECTION TO COURSE MATERIALS:

Workshop 7: I used the cowsay library to provide a welcoming user interface and matplotlib to plot a graph of the performance of the students. I also integrated json to handle complex data structures, ensuring student information could be saved and retrieved effectively. 

Workshop 8: I implemented a custom validation filter to ensure Student IDs followed a strict organisational format by using regex functions. I also used the unnitest framework to create individual tests in the test_app.p to review if my regex correctly blocked invalid inputs and if my getters functioned as expected. I also generated a permanent data.json log and a performance_graph.png image to show the performance of students.

Workshop 9: I established a meaningful relationship between a Person base class and a Student subclass, demonstrating Inheritance and how attributes and methods are passed down the hierarchy. I used @property decorator to implement getter and setter methods to protect the integrity of the data. 

DEVELOPMENT PROCESS AND CHALLENGES:

GIT History: I followed the brief and made sure I committed every technical feature individually with comments of what they do and why.

Problem Solving: I encountered a few problems within the coding. The first error I found was the cowsay package which was installed however I had to change interpretor in order for the code to get that the package was installed. I also had to install the matplotlib package so the graph could be generated. I encountered an Attribute Error when my Student Class could not find the add_grade method. I solved this by identifying the scope issue in Python rules and moved the position of the functions so that the code worked. I also had a problem with the graph not showing using the plt.show(), so instead I saved it as a file using plt.savefig('performance_graph.png') in order to save the graph as a file.