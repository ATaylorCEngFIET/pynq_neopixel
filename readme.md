This is a pynq overlay for the PYNZ Z2 which drives upto 1023 neo pixels. 

Accessed over MMIO, each neo pixel is stored from address 0x4 as a 24 bit value RGB
Address off set 0x0 defines the number of pixels in the array 