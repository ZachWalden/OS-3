# Logical Address objects
class LogicalAddress():
    # Page number 
    def __init__(self, pagenum, offset):
        self.pagenum = pagenum
        self.offset = offset
        pass
    
    def __str__(self):
        return f"Page Number: {self.pagenum} ; Offset: {self.offset}"

# Memory Management
class MemManagement():

    def __init__(self, page, ):
        page_frame_table = []

        pass

    def convert(self, logical_addr):
        if logical_addr.pagenum not in self.page_frame_table:
            pass
        pass
