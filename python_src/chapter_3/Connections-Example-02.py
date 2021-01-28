# Example-2.py
from __future__ import print_function
import sys
import libvirt

if __name__ == '__main__':
    conn = libvirt.openReadOnly('qemu:///system')
    if conn is None:
        print('Failed to open connection to qemu:///system', file=sys.stderr)
        exit(1)
    conn.close()
    exit(0)
