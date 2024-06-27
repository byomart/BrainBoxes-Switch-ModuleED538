#!/usr/bin/env python

# Example of using brainboxes.AsciiIo class for communication with Brainboxes ED-range products
# Tested with Python 2.7.9 and 3.4.3 on Windows, and 2.7.6 and 3.4.0 on Linux

import brainboxes

with brainboxes.AsciiIo(ipaddr='192.168.127.254', port=9500, timeout=1.0) as io:

    for txmessage in (b'$01M', b'~**', b'@01', b'@02', b'$016'):
        print("Sending command %s" % txmessage)
        if txmessage[1:3] == b'**':
            data = io.command_noresponse(txmessage)
            print("  No response expected")
        else:
            rxdata = io.command_response(txmessage)
            if rxdata is None:
                print("  No response received!")
            else:
                print("  Response was %s" % rxdata) 