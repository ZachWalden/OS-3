# Zach Walden
# Programming Assignment 3

import random

PAGE_SIZE = 1024  
FRAME_SIZE = 1024  
NUM_PAGES = 16  
NUM_FRAMES = 8  

#Function returns a logical address within the given parameters of the system memory
def generate_logical_address():
    return random.randint(0, NUM_PAGES * PAGE_SIZE - 1) 


random.seed()  # Seed random number generator

# Initialize empty page frame table
page_frame_table = [-1] * NUM_PAGES  # Page/frame table initialized with -1 indicating no mapping initially

# Initialize empty physical memory 
physical_memory = [-1] * NUM_FRAMES  

# Fill page/frame table and physical memory
for i in range(NUM_PAGES):
    if random.random() < 0.5:
        page_frame_table[i] = i % NUM_FRAMES 
    else:
        page_frame_table[i] = 1

# Run 10 random addrsses through table
for _ in range(10):
    #Get random address, calculate page # and offset
    logical_address = generate_logical_address()  
    page_number = logical_address // PAGE_SIZE  
    offset = logical_address % PAGE_SIZE  

    # Verify page is within given range:
    if page_number < NUM_PAGES:  

        # Get corresponding frame number from page frame table
        frame_number = page_frame_table[page_number]  

        # Calculates the physical address by adding offset to the base address of the frame
        physical_address = frame_number * FRAME_SIZE + offset  

        if logical_address != physical_address:

            # Parse address to print page number and offset 
            hexed_addr = hex(physical_address)[2:]
            offset_num = hexed_addr[-2:]
            page_num = hexed_addr.replace(offset_num, "")

            if len(page_num) == 1:
                page_num = "0" + page_num
            elif len(page_num) == 0:
                page_num = "00"

        if logical_address != physical_address:
            print(f"Logical Address: 0x{logical_address:04X} => Physical Address: 0x{physical_address:04X}, Page Number: 0x{page_num} , Offset Number: 0x{offset_num}")  # Prints the logical and physical addresses in hexadecimal format
    else:
        print(f"Invalid Page Number: {page_number}")  # Prints an error message for invalid page number
        page_frame_table[page_number] = page_number   # Update page table with page number


