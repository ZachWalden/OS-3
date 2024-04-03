# Zach Walden
# Programming Assignment 3

#Set Page & frame size to 256 bytes
page_size = 256  
frame_size = 256  

class PageFrame:

    # Initialize empty table
    def __init__(self, page_size, frame_size):
        self.page_size = page_size
        self.frame_size = frame_size
        self.table = {}  

    # Add the frame number into page frame table
    def map(self, page_number, frame_number):
        self.table[page_number] = frame_number

    # Translate the logical address given the frame number is in the table
    def translate(self, logical_address):
        page_number = logical_address // self.page_size
        offset = logical_address % self.page_size
        if page_number in self.table:
            frame_number = self.table[page_number]
            return frame_number, offset
        else:
            return None, None  # Handle page fault here

# Sample input
logical_addresses = [0x3A7F, 0xABCD, 0x5678]

table1 = PageFrame(page_size, frame_size)

# Fill page frame table with a few random addresses
table1.map(0x0D, 0x01)
table1.map(0x2B, 0x02)
table1.map(0x15, 0x03)

# Page frames for given addresses, preventing page faults
table1.map(0xAB, 0x05)
table1.map(0x56, 0x06)


# Translate logical addresses
for logical_address in logical_addresses:
    frame_number, offset = table1.translate(logical_address)

    #If a frame number is returned, print page number & offset
    if frame_number is not None:
        print(f"Logical Address: {hex(logical_address)} => Page Number: 0x{frame_number:02x}, Offset: 0x{offset:02x}")
    else:
        print(f"Page fault occurred for logical address: {hex(logical_address)}")
