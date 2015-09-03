A custom network topology using mininet python APIs as given below. 
 
The program takes two command line arguments as input:
No. of hosts:  X 
No. of switches: Y

Used: Oracle Virtual Box
Downloaded Mininet.vmdk file from mininet github page.

And creates a custom network topology with Y Switches where each switch has X hosts.

The following functionality is also implemented:
1) Odd hosts can only talk to each other and even hosts can talk to each other Ex: h1 should only be able to ping h3, h5 and h2 should be able to ping h4, h6 

2)  All the communication should be throttled to 1 mbps for odd hosts and 2 mbps 
for even hosts


