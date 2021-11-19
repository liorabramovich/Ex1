The Problem: 
In the problem there is an elevator system with an abound of elevators in the begining the system gets an array of requests, 
the task is to compute which elevator is best for which task

the solution: 
In the solution we take each elevator and give it its own work plan, an array where we save the floors that the elevator needs to go to.
each elevator also has an array of ETAs, an array of the time that the elevator will arrive at the target floor.
by calculating the time that each elevator needs to get to a floor we choose the best elevator for each task

how to operate:
-first the user needs to type the building he wants to use(data\B1.json, data\B2.json, data\B3.json, data\B4.json, data\B5.json)
-second the user needs to type the call case he wants to use(data\Calls_a.csv, data\Calls_b.csv, data\Calls_c.csv, data\Calls_d.csv)
-now wait for the algorythm to do its magic
---------------
RESULTS

B1 , calls_a , 0 uncpompleted , 112 avg time
B2 , calls_a , 0 uncompleted , 50.07 avg time 
B3 , calls_a , 0 uncompleted , 45.67 avg time 
B3 , calls_b, 161 uncompleted , 578.8 avg time 
B3 , calls_c , 117 uncompleted, 601.35 avg time 
B3 , calls_d , 248 uncompleted, 632.08 avg time
B4 , calls_a , 0 uncompleted, 37.4 avg time 
B4 , calls_b , 145 uncompleted, 349.26 avg time 
B4 , calls_c , 137 uncompleted, 429.67 avg time 
B4 , calls_d , unCompleted calls,358 846.987129190017
B5 , calls_a , 0 uncompleted, 17.18 avg time 
B5 , calls_b , 2 uncompleted, 122.11 avg time 
B5 , calls_c , 14 uncompleted, 111. 72 avg time 
B5 , calls_d , 14 uncompleted, 126.07 avg time

