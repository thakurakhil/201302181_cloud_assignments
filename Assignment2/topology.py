#!/usr/bin/python

import sys
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import OVSController
from mininet.link import TCLink


switches_array = []
hosts_array = []
x = 0
y = 0

class SwitchHostTopo(Topo):
	"Y Switchs connected to X hosts."
        def __init__(self, **opts):
            Topo.__init__(self, **opts)
            args=(sys.argv)
            x =int(args[1])    # X
            y =int(args[2]) # Y 
            print x
            print y
            print " creating " + str(y) + " switches and " +  str(x) + " hosts "
            even_domain = '10.0.0.'
            odd_domain = '11.0.0.'
            for i in range(y):
            	switches_array.append(self.addSwitch('s' + str(i+1)))
            for j in range(x):
                if (j+1)%2 == 0:
                	hosts_array.append(self.addHost('h' + str(j+1), ip = even_domain + str(j+1)))
                else:
                	hosts_array.append(self.addHost('h' + str(j+1), ip = odd_domain + str(j+1)))
            for i in range(y):
                for j in range(x):
                    if (j+1)%2 == 0:
                        self.addLink(hosts_array[j], switches_array[i], bw = 2)
                    else:
                        self.addLink(hosts_array[j], switches_array[i], bw = 1)
            
            for i in range(y-1):
				self.addLink(switches_array[i], switches_array[i+1])

def createTopo():
    "Creating network"
    
    topo = SwitchHostTopo()
    net = Mininet(topo=topo, 
                  controller=OVSController, link=TCLink)
    net.start()
    print "Testing network connectivity"
    net.pingAll()

    print "Testing bandwidth between odd hosts"
    net.iperf((net.getNodeByName(hosts_array[0]), net.getNodeByName(hosts_array[2])))
    print "Testing bandwidth between even hosts"
    net.iperf((net.getNodeByName(hosts_array[1]), net.getNodeByName(hosts_array[3])))
    net.stop()


if __name__ == '__main__':
    createTopo()
