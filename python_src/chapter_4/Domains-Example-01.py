# Example-1.py
from __future__ import print_function
import sys
import libvirt

if __name__ == '__main__':
    conn = libvirt.open('qemu:///system')
    if conn is None:
        print('Failed to open connection to qemu:///system', file=sys.stderr)
        exit(1)

    domainID = 6
    try:
        dom = conn.lookupByID(domainID)
    except libvirt.libvirtError:
        print('Failed to get the domain object', file=sys.stderr)
    else:
        conn.close()
        exit(0)
