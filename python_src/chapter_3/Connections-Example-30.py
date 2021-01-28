# Example-30.py
from __future__ import print_function
import sys
import libvirt

if __name__ == '__main__':

    conn = libvirt.open('qemu:///system')
    if conn == None:
        print('Failed to open connection to qemu:///system', \
              file=sys.stderr)
        exit(1)

    # stats = conn.getCPUStats(0)
    stats = conn.getCPUStats(libvirt.VIR_NODE_CPU_STATS_ALL_CPUS)

    print("kernel: " + str(stats['kernel']))
    print("idle:   " + str(stats['idle']))
    print("user:   " + str(stats['user']))
    print("iowait: " + str(stats['iowait']))

    conn.close()
    exit(0)
