# Example-26.py
from __future__ import print_function
import sys
import libvirt

if __name__ == '__main__':

    conn = libvirt.open('qemu:///system')
    if conn == None:
        print('Failed to open connection to qemu:///system', \
              file=sys.stderr)
        exit(1)

    buf = conn.getMemoryStats(libvirt.VIR_NODE_MEMORY_STATS_ALL_CELLS)

    for key, val in buf.items():
        print(f"{key}: {val}")

    conn.close()
    exit(0)
