<h2 style="color:green"> This project has been created as part
of the 42 curriculum by <spam style= "color:#FFC0CB">khnoman </spam></h4>

<h1 style> 🛩️ 🕹️FLY_IN</h1>
</br>
<h3>📋 Table of Contents </h3>

<ul>
<li><a href="#overview"> Overview </a></li>
<li><a href="#Installation">Installation</a></li>
<li><a href="#Project_Description"> Project Description </a></li>
<li><a href="#Rules"> Rules </a></li>
<li><a href="#Project_Structure"> Project Structure </a></li>
<li><a href="#Resources"> Resources </a></li>
<li><a href="#AI_Usage"> AI Usage </a></li>
</ul>

<h4 id="overview"> 🎯OVERVIEW</h4>
<p style="font_size: 70px;">
FlyIn is a drone traffic simulator that models drones moving through a network of connected zones. It computes a path for each drone and simulates their movements while respecting zone capacities and connection constraints to avoid conflicts. The project also provides a graphical visualization of the simulation using Pygame.
</P>

<h4 id ="Installation" > 🛠️ INSTALLATION </h4>

<h6> clone the repository </h6>
<p> git clone <my_repo_link> fly_in </p>
<h6> install the packages </h6>
<p style="color:aqua"> make install</p>

<h6> run the program </h6>
<p style="color:aqua"> make run</p>
<h7> output</h7>
<code>
turn 0: D0-junction D1-junction
turn 1: D0-path_a D2-junction
turn 2: D0-goal D1-path_b D2-path_a D3-junction
turn 3: D1-goal D2-goal D3-path_b
turn 4: D3-goal
</code>

<h2 id="Project_Description"> 📖 Project Description</h2>

<p> FlyIn is a drone traffic simulation project that models the movement of multiple drones through a
    network of connected zones. Each drone must travel from a starting zone to a destination while 
    respecting operational constraints such as zone capacities and connection availability.
    The project computes collision-free paths using pathfinding algorithms and simulates the movement of all drones turn by turn.
    During each simulation step, drones compete for shared resources, and the scheduler ensures that capacity limits are respected while avoiding conflicts.
    The simulation includes a graphical visualization built with Pygame,
    allowing users to observe drone movements, occupied zones, and the progression of the simulation in real time.
</p>

<h2 id="Rules"> Rules</h2>
<p> The simulation follows these rules:

    - Each drone starts from the same start zone and must reach the destination zone.
    - A drone can only move to a neighboring zone through an existing connection.
    - Each zone has a maximum capacity that cannot be exceeded.
    - Connections between zones also have capacity limits.
    - If a drone cannot move because a zone or connection is full, it waits until the resource becomes available.
    - Drones move one step per simulation turn.
    - The simulation ends when all drones have reached the destination.
</p>

<h2 style="font-size: 27px;" id="Project_Structure">📁 Project Structure </h2>

<pre style="font-family: 'Courier New', monospace; background: #7c817875; padding: 20px; border-radius: 5px;">
fly_in/
├── images
|   ├──drone.png
|   └── enter_image.png
├── maps
├── src
|   ├── models
|   |   ├── __init__.py
|   |   ├── algo_class.py
|   |   ├── connection_class.py
|   |   ├── drone_class.py
|   |   ├── drones_class.py
|   |   ├── simulation.py
|   |   └── zone_class.py
|   ├── parser
|       ├── __init__.py
|       └── parsing.py
├── class_visualisation.py
├── main.py
├── Makefile
├── README.md
└── requirements.txt
</pre>
e.>

<div>
    <h2  style="font-size: 27px;" id="Resources"> 📚 Resources </h2>
    <h4 style="font-size: 20px;"> Useful Links:</h4>
    <ul>
    <li> <a href="https://www.pygame.org/docs/"> pygame </a> </li>
    <li> <a href="https://www.geeksforgeeks.org/dsa/dijkstras-shortest-path-algorithm-greedy-algo-7/"> Dijkstra's Algorithm</a></li>
    </ul>
    

</div>