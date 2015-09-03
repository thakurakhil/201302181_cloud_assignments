#!/usr/bin/python

import sys
from mininet.net import Mininet
from mininet.node import Controller
from mininet.cli import CLI
from mininet.log import setLogLevel, info

class SwitchHostTopo(Topo):
	"Y Switchs connected to X hosts."
        def build(self, x, y):
            hosts_array = []
            switches_array = []
            for i in range(y):
            	switches_array.append(self.addSwitch('s' + str(i+1)))
            for j in range(x):
                # Each host gets 50%/n of system CPU
                hosts_array.append(self.addHost('h' + str(j+1)), cpu=0.5/n)
            for i in range(y):
            	for j in range(i+1, y):
            		self.addLink


                # 10 Mbps, 5ms delay, 10% loss, 1000 packet queue
                self.addLink(host, switch,
                   bw=10, delay='5ms', loss=10, max_queue_size=1000, use_htb=True)


def createTopo():
	"Creating network"
	args=(sys.argv)
    no_of_hosts =int(args[1])    # X
    no_of_switches =int(args[2]) # Y

    topo = SwitchHostTopo(x=no_of_hosts, y=no_of_switches)
    net = Mininet(topo=topo, 
                  host=CPULimitedHost, link=TCLink)
    net.start()
    print "Dumping host connections"
    dumpNodeConnections(net.hosts)
    print "Testing network connectivity"
    net.pingAll()
    print "Testing bandwidth between h1 and h4"
    h1, h4 = net.get('h1', 'h4')
    net.iperf((h1, h4))
    net.stop()


if __name__ == '__main__':
    setLogLevel( 'info' )
    createTopo()