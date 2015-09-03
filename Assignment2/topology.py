#!/usr/bin/python

import sys
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import OVSController
from mininet.link import TCLink
from mininet.log import setLogLevel, info

TCLink = []
switches_array = []
x = 0
y = 0

class SwitchHostTopo(Topo):
	"Y Switchs connected to X hosts."
        def build(self):
            args=(sys.argv)
            x =int(args[1])    # X
            y =int(args[2]) # Y
            even_domain = '10.2.0.'
            odd_domain = '10.1.0.'
            for i in range(y):
            	switches_array.append(self.addSwitch('s' + str(i+1)))
            for j in range(x):
                if (j+1)%2 == 0:
                	hosts_array.append(self.addHost('h' + str(j+1)), ip = even_domain + str(j+1))
                else:
                	hosts_array.append(self.addHost('h' + str(j+1)), ip = odd_domain + str(j+1))
            j = 0
            while j < x :
            	for i in range(y):
            		if (j+1)%2 == 0:
	            		self.addLink(hosts_array[j], switches_array[i], bw = 2)
	            	else:
	            		self.addLink(hosts_array[j], switches_array[i], bw = 1)
	            	j = j + 1

            for i in range(y):
				self.addLink(switches[i], switches[i+1])

def createTopo():
    "Creating network"
    
    topo = SwitchHostTopo()
    net = Mininet(topo=topo, 
                  controller=OVSController, link=TCLink)
    net.start()
    print "Dumping host connections"
    dumpNodeConnections(net.hosts)
    print "Testing network connectivity"
    net.pingAll()
    print "Testing bandwidth between even hosts and odd hosts"
    for i in x:
    	if (i+2) <= x:
    		 net.iperf( ( net.getNodeByName(('h' + str(i)), ('h' + str(i+2))) ) )
    
    net.stop()


if __name__ == '__main__':
    setLogLevel( 'info' )
    createTopo()
