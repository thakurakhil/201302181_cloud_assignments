#A custom network topology using mininet python APIs. 

To run ->

sudo python topology.py x y


###Here the code tests the topology by pingall , showing the communication between hosts and to check bandwidth (h1, h3) and (h2,h4) are chosen for simplicity purpose


##Youtube link  : https://www.youtube.com/watch?v=RcEm-BRr-MY&feature=youtu.be




##problem statement:


The program takes two command line arguments as input:
No. of hosts:  X 
No. of switches: Y

And creates a custom network topology with Y Switches where each switch has X hosts.

The following functionality is also implemented:
1) Odd hosts can only talk to each other and even hosts can talk to each other Ex: h1 should only be able to ping h3, h5 and h2 should be able to ping h4, h6 

2)  All the communication should be throttled to 1 mbps for odd hosts and 2 mbps 
for even hosts



201302181
Akhil
