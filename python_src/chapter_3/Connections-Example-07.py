# Example-7.py
from __future__ import print_function
import sys
import libvirt

if __name__ == '__main__':
    conn = libvirt.open('qemu+tls://host2/system')
    if conn is None:
        print('Failed to open connection to qemu+tls://host2/system', file=sys.stderr)
        exit(1)
    conn.close()
    exit(0)