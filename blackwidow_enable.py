#!/usr/bin/python

""" blackwidow_enable.py
A further updated version of blackwidow_enable. This script has an extensive history,
and many people have contributed slight modifications to it.

Sources:
    https://github.com/tuxmark5/EnableRazer
    https://finch.am/projects/blackwidow/
    https://github.com/jelly/Utils/blob/master/blackwidow_enable.py
    https://superuser.com/questions/342107/getting-macro-keys-from-a-razer-blackwidow-to-work-on-linux
"""
import usb
import sys

VENDOR_ID = 0x1532  # Razer Vendor ID
PRODUCT_ID = 0x0000  # To be set programmatically

USB_REQUEST_TYPE = 0x21  # Host To Device | Class | Interface
USB_REQUEST = 0x09       # SET_REPORT

USB_VALUE = 0x0300
USB_INDEX = 0x2
USB_INTERFACE = 2

LOG = sys.stderr.write


def getProductID():
    razer_devices = usb.core.find(find_all=True, idVendor=VENDOR_ID)

    razer_devices_list = list(razer_devices)

    if(len(razer_devices_list) > 1):
        print("Multiple razer devices are attached, please unplug\
              any razer devices that are not the BlackWidow.")
    elif(razer_devices_list == 0):
        print(
            "Cannot detect any razer products, please ensure your\
            BlackWidow is plugged in.")
    else:
        global PRODUCT_ID
        PRODUCT_ID = razer_devices_list[0].idProduct


class blackwidow(object):
    kernel_driver_detached = False

    def __init__(self):
        self.device = usb.core.find(idVendor=VENDOR_ID, idProduct=PRODUCT_ID)

        if self.device is None:
            raise ValueError(
                "Device {}:{} not found\n".format(VENDOR_ID, PRODUCT_ID))
        else:
            LOG("Found device {}:{}\n".format(VENDOR_ID, PRODUCT_ID))

        if self.device.is_kernel_driver_active(USB_INTERFACE):
            LOG("Kernel driver active. Detaching it.\n")
            self.device.detach_kernel_driver(USB_INTERFACE)
            self.kernel_driver_detached = True

        LOG("Claiming interface\n")
        usb.util.claim_interface(self.device, USB_INTERFACE)

    def __del__(self):
        LOG("Releasing claimed interface\n")
        usb.util.release_interface(self.device, USB_INTERFACE)

        if self.kernel_driver_detached:
            LOG("Reattaching the kernel driver\n")
            self.device.attach_kernel_driver(USB_INTERFACE)

        LOG("Done.\n")

    def bwcmd(self, c):
        from functools import reduce

        c1 = bytes.fromhex(c)
        c2 = [reduce(int.__xor__, c1)]
        b = [0] * 90
        b[5: 5 + len(c1)] = c1
        b[-2: -1] = c2
        return bytes(b)

    def send(self, c):
        def _send(msg):
            USB_BUFFER = self.bwcmd(msg)
            result = 0

            try:
                result = self.device.ctrl_transfer(
                    USB_REQUEST_TYPE, USB_REQUEST, wValue=USB_VALUE,
                    wIndex=USB_INDEX, data_or_wLength=USB_BUFFER)
            except:
                sys.stderr.write("Could not send data.\n")

            if result == len(USB_BUFFER):
                LOG("Data sent successfully.\n")

            return result

        if isinstance(c, list):
            for i in c:
                print(' >> {}\n'.format(i))
                _send(i)
        elif isinstance(c, str):
            _send(c)


def main():
    getProductID()

    init_new = '0200 0403'  # Enables use of macro keys (newer firmwares)
    init_old = '0200 0402'  # Enables use of macro keys (older firmwares)
    pulsate = '0303 0201 0402'  # Make LEDs pulsate
    bright = '0303 0301 04ff'  # Make LEDs bright
    normal = '0303 0301 04a8'  # Make LEDs normal
    dim = '0303 0301 0454'  # Make LEDs dim
    off = '0303 0301 0400'  # Turn LEDs off

    bw = blackwidow()
    bw.send(init_new)


if __name__ == '__main__':
    main()
