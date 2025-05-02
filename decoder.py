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


class header_base():
    fmt = 0 # Format
    type = 0
    tc = 0
    tph = 0
    digest = ""
    poisoned = ""
    ordering = ""
    snoop = ""
    length = 0
    description = ""
    dw24 = transaction()



txn = header_base()

# Format types in a list
fmt = ["3 DW header, no data", "4 DW header, no data", "3 DW header, with data", "4 DW header, wit data"]

msg_routing = ["Routed to root complex", "Routed by Address", "Routed by ID", "Broadcast from RC", "Local-Terminated at the receiver", "Gathered to RC"]
msg_codes = {
    0x0: "Unlock", 
    0x10: "LTR",
    0x12: "OBFF",
    0x14: "PM_Active_state",
    0x18: "PME",
    0x19: "PME_Off",
    0x20: "Asser INT",
    0x24: "Deassert INT",
    0x52: "PTM",
    0x7E: "Vendor defined",

}
# Define the PCIe TLP header format
def decode(arg1, arg2, arg3, arg4):
   
    HDR1 = arg1
    HDR2 = arg2
    HDR3 = arg3
    HDR4 = arg4

    legacy_mode = 0 
    isaread = 0
    isawrite = 0

    print(f"TLP Header DW: {hex(HDR1)} {hex(HDR2)} {hex(HDR3)} {hex(HDR4)}")

    # Read the value of the bits in header base. shift right from bit 29 
    # and then bitwise with AND 0x7 to get the value of the thre bits that represent the format
    txn.fmt = (HDR1 >> 29) & 0x7
    txn.type = (HDR1 >> 24) & 0x1F
    txn.tc = (HDR1  >> 20) & 0x7 # This changes when legacy_mode=1 the bit to read would be: txn.tc = (HDR1  >> 21) & 0x7
    txn.tph = (HDR1 >> 16) & 0x1 

    if ((HDR1 >> 15) & 0x1) == 1: # This changes when legacy_mode=1 the bit to read would be (traler size): txn.ts = (HDR1  >> 13) & 0x7 
        txn.digest = "TLP With Digest"
    else:
        txn.digest = "TLP Without Digest"
    if ((HDR1 >> 14) & 0x1) == 1:
        txn.poisoned = "Corrupted"
    else:
        txn.poisoned = "Non-corrupted"
    if ((HDR1 >> 13) & 0x1) == 1:# This changes when legacy_mode=1 the bit to read would be (traler size): txn.ts = (HDR1  >> 11) & 0x1 = 1:
        txn.ordering = "Relaxed ordering"
    else:
        txn.ordering = "Default ordering"# This changes when legacy_mode=1 the bit to read would be (traler size): txn.ts = (HDR1  >> 10) & 0x1 = 1:
    if ((HDR1 >> 12) & 0x1) == 1:
        txn.snoop = "Snoop"
    else:
        txn.snoop = "Default snoop"
    if (HDR1 & 0x3FF) == 0:
        txn.length = 1024
    else:
        txn.length = HDR1 & 0x3FF


    print(f"\nFormat: \t\t {txn.fmt} = {fmt[txn.fmt]}")
    print(f"Traffic Class: \t\t {txn.tc}")
    print(f"TPH: \t\t\t {txn.tph}")
    print(f"\t\t\t {txn.digest}")
    print(f"\t\t\t {txn.poisoned}")
    print(f"\t\t\t {txn.ordering}")
    print(f"\t\t\t {txn.snoop}")
    print(f"Length: \t\t {txn.length} Double Words")

    # Print the name of the transaction that corresponds to the Type code field (5 bits value)
    if txn.type in [0x0, 0x1, 0x2, 0xC, 0xD, 0xE]:
        fmt_type = (txn.fmt << 5) | (txn.type & 0xFE) # to asign a differentiator type including both format and type fields
        if fmt_type in [0x0,0x20]:
            if txn.type == 1: #Refer table of the transactions type codes
                txn.description = "MemRd - Locked"
            else:
                txn.description = "MemRd"
                isaread = 1
        elif fmt_type in [0x2]:
            txn.description = "I/O Read"
        elif fmt_type in [0x40, 0x60]:
            txn.description = "MemWr"
            isawrite = 1
        elif fmt_type in [0x42]:
            txn.description = "I/O Write"
        elif fmt_type in [0x4C, 0x6C]:
            txn.description = "Fetch and add AtomicOP Request"
        elif fmt_type in [0x4E, 0x6E]:
            txn.description = "Compare and Swapp AtomicOp Request"
        else:
            if txn.type in [0x0, 0x1, 0x2]:
                print(f"Invalid TLP encoding (Mem, I/O), fmt = {hex(txn.fmt)}, type = {hex(txn.type)}")
            else:
                print(f"Invalid TLP encoding (AtomicOp), fmt = {hex(txn.fmt)}, type = {hex(txn.type)}")
            return 1
        
        txn.dw24.memory.rid = (HDR2 >> 16) & 0xFFFF # Requester ID is the whole value that includes the bus/device/function nombers below
        txn.dw24.memory.rbus = (txn.dw24.memory.rid >> 8) & 0xFF
        txn.dw24.memory.rdev = (txn.dw24.memory.rid >> 3) & 0x1F
        txn.dw24.memory.rfun = txn.dw24.memory.rid & 0x7
        txn.dw24.memory.tag = (HDR2 >> 8) & 0xFFFF | ((HDR1 >> 19) & 0x1) << 8 | ((HDR1 >> 23) & 0x1) << 9 # in legacy_mode=1 this is only found in HDR2: (HDR2 & 0xFFF)
        txn.dw24.memory.lbe = (HDR2 >> 4) & 0xF # first byte enabled field
        txn.dw24.memory.fdb = HDR2 & 0xF # Last byte enabled field

        if txn.fmt & 1: # f format = 1 then is a 64-bit memory(high and low address) and read the PH(Process hint value)
            txn.dw24.memory.addrl = HDR4 & 0xFFFFFFFC
            txn.dw24.memory.addrh = HDR3
            txn.dw24.memory.ph = HDR4 & 0x3
        else:# else format is not 1 then use the transacton is 32-bit adress only HDR3
            txn.dw24.memory.addrl = HDR3 & 0xFFFFFFFC
            txn.dw24.memory.ph = HDR4 & 0x3
        
        print(f"TLP Type: \t\t\t {hex(txn.type)} = {txn.description}")
        print(f"Requester ID: \t\t\t {hex(txn.dw24.memory.rid)}")
        print(f"Requester BUS: \t\t\t {txn.dw24.memory.rbus}")
        print(f"Requester Device: \t\t\t {txn.dw24.memory.rdev}")
        print(f"Requester Function: \t\t\t {txn.dw24.memory.rfun}")

        if (isawrite & txn.tph) == 1:
            print(f"ST: \t\t\t {hex(txn.dw24.memory.tag)}")
        else:
            print(f"TAG: \t\t\t {hex(txn.dw24.memory.tag)}")

        if (isaread & txn.tph) == 1:
            isawrite = (txn.dw24.memory.lbe << 4) | txn.dw24.memory.fdb
            print(f"ST: \t\t\t {hex(isawrite)}")
        else:
            print(f"Last DWord byte enabled: \t {hex(txn.dw24.memory.lbe)}")
            print(f"Last DWord byte enabled: \t {hex(txn.dw24.memory.fdb)}")

        print(f"Address Low: \t\t\t {hex(txn.dw24.memory.addrl)}")
        print(f"Address High: \t\t\t {hex(txn.dw24.memory.addrh)}")
        
        if txn.tph == 1:
            print(f"PH: \t\t\t {hex(txn.dw24.memory.ph)}")
    
    #Other type of request Configuration request types
    elif txn.type in [0x4, 0x5]:
        if txn.fmt in [0x0]:
            if txn.type == 0x4: # refer table of transaction types
                txn.description = "Configuration Read type 0"
            else:
                txn.description = "Configuration Read type 1"
        elif txn.fmt in [0x2]:
            if txn.type == 0x4:
                txn.description = "Configuration Write type 0"
            else:
                txn.description = "Configuration Write type 1"
        else:
            print(f"Invalid TLP encoding (CFG), fmt = {hex(txn.fmt)}, type = {hex(txn.type)}")
            return 1
    
        txn.dw24.cfg.rid = (HDR2 >> 16) & 0xFFFF # Requester ID is the whole value that includes the bus/device/function nombers below
        txn.dw24.cfg.rbus = (txn.dw24.memory.rid >> 8) & 0xFF
        txn.dw24.cfg.rdev = (txn.dw24.memory.rid >> 3) & 0x1F
        txn.dw24.cfg.rfun = txn.dw24.memory.rid & 0x7
        txn.dw24.cfg.tag = (HDR2 >> 8) & 0xFFFF | (HDR1 >> 19) & 0x1 | (HDR1 >> 23) & 0x1  
        txn.dw24.cfg.lbe = (HDR2 >> 4) & 0xF # first byte enabled field
        txn.dw24.cfg.fdb = HDR2 & 0xF # Last byte enabled field
        # Target information
        txn.dw24.cfg.tid = (HDR2 >> 16) & 0xFFFF # Requester ID is the whole value that includes the bus/device/function nombers below
        txn.dw24.cfg.tbus = (txn.dw24.memory.tid >> 8) & 0xFF
        txn.dw24.cfg.tdev = (txn.dw24.memory.tid >> 3) & 0x1F
        txn.dw24.cfg.tfun = txn.dw24.memory.tid & 0x7
        txn.dw24.cfg.reg = HDR3 & 0xFFF

        
        print(f"TLP Type: \t\t {hex(txn.type)} = {txn.description}")
        print(f"Requester ID: \t\t {hex(txn.dw24.cfg.rid)}")
        print(f"Requester BUS: \t\t {txn.dw24.cfg.rbus}")
        print(f"Requester Device: \t {txn.dw24.cfg.rdev}")
        print(f"Requester Function: \t {txn.dw24.cfg.rfun}")
        print(f"TAG: \t\t\t {hex(txn.dw24.cfg.tag)}")
        print(f"Last DWord byte enabled: {hex(txn.dw24.cfg.lbe)}")
        print(f"Last DWord byte enabled: {hex(txn.dw24.cfg.fdb)}")
        print(f"Target ID: \t\t {hex(txn.dw24.cfg.rid)}")
        print(f"Target BUS: \t\t {txn.dw24.cfg.rbus}")
        print(f"Target Device: \t\t {txn.dw24.cfg.rdev}")
        print(f"Target Function: \t {txn.dw24.cfg.rfun}")
        print(f"Register: \t\t {txn.dw24.cfg.reg}")
        





# Test the code with this entry for a memory transaction
#decode(0x01000003, 0x99000000, 0x00000000, 0x00000000)

# Test the code with this entry for a configuration
decode(0x21000003, 0x99000000, 0x000054a0, 0x00000000)

