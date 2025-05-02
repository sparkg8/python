
class transaction_content():
    rid = 0 #Requester id
    rdev = 0 #Requester device number
    rbus = 0 # Requester bus number
    rfun = 0 # Requester function number
    tag = 0
    fbe = 0 # first byte enable field
    lbe = 0 # last byte enabled
    addrh = 0
    addrl = 0
    tid = 0
    tdev = 0
    tfun = 0 # target function
    reg = 0
    vid = 0
    vmsg = 0
    cid = 0
    cdev = 0 # completion device number
    cbus = 0
    cfun = 0
    cplstatus = 0 # Completion status
    bytecount = 0
    routing = 0
    code = 0
    codedescription = 0
    lwradd = 0
    ph = 0
    msgsubtype = 0
    msgsubtypedecode = 0


class transaction():
    memory = transaction_content()
    cfg = transaction_content()
    cpl = transaction_content()
    msg = transaction_content()



    

class DecodeTLP:
    def __init__(self, HDR1):
        self.HDR1 = HDR1
    
        self.fmt = 0 # Format
        self.type = 0
        self.tc = 0
        self.tph = 0
        self.digest = ""
        self.poisoned = ""
        self.ordering = ""
        self.snoop = ""
        self.length = 0
        self.description = ""
        self.dw24 = transaction()
    # Memory request
    def base_header_nfm(self):
        self.fmt = (self.HDR1 >> 29) & 0x7
        self.type = (self.HDR1 >> 24) & 0x1F
        
        
        


def decode(arg1, arg2, arg3, arg4):

    HDR1 = arg1
    HDR2 = arg2
    HDR3 = arg3
    HDR4 = arg4

    legacy_mode = 0 
    isaread = 0
    isawrite = 0

    print(f"TLP Header DW: {hex(HDR1)} {hex(HDR2)} {hex(HDR3)} {hex(HDR4)}")

    x = DecodeTLP(HDR1)
    x.base_header_nfm()
    

#Test
decode(0x29000001, 0x99000000, 0x0000f5a7, 0x00000000)

    

