# Example-8.py
from __future__ import print_function
import sys
import libvirt

if __name__ == '__main__':
    conn = libvirt.open('qemu:///system')
    if conn is None:
        print('Failed to open connection to qemu:///system', file=sys.stderr)
        exit(1)

    caps = conn.getCapabilities()  # caps will be a string of XML
    print('Capabilities:\n'+caps)

    conn.close()
    exit(0)
