# Example-17.py
from __future__ import print_function
import sys
import libvirt

if __name__ == '__main__':

    conn = libvirt.open('qemu:///system')
    if conn == None:
        print('Failed to open connection to qemu:///system', \
              file=sys.stderr)
        exit(1)

    uri = conn.getURI()
    print('Canonical URI: '+uri)

    conn.close()
    exit(0)
