#!/usr/bin/env python3

INSTRUCTION_COUNT = 14
FUNC_COUNT = 8

#                    AluSrc1 AluSrc2[2] WriteReg WriteRegSrc[3] WriteLO WriteHI WriteMem IsFlowOp PcSrc BchAluSrc1 BranchEq BranchNeg  Reg2Src
SIGNAL_TUPLE_SIZE = (1,       2,         1,       3,             1,      1,      1,       1,        1,       1,         1,       1,     1)

RTYPE_SIGNAL_TABLE = [
# AluSrc1    AluSrc2      WriteReg    WriteRegSrc   WriteLO      WriteHI      WriteMem  IsFlowOp    PcSrc         BchAluSrc1   BranchEq     BranchNeg   Reg2Src
(0,           0,           1,           0,           0,           0,           0,        0,         None,           None,        0,           None,      0), # 0 SLL
(0,           0,           1,           0,           0,           0,           0,        0,         None,           None,        0,           None,      0), # 1 SRL
(0,           0,           1,           0,           0,           0,           0,        0,         None,           None,        0,           None,      0), # 2 ADD
(0,           0,           1,           0,           0,           0,           0,        0,         None,           None,        0,           None,      0), # 3 AND
(0,           0,           1,           0,           0,           0,           0,        0,         None,           None,        0,           None,      0), # 4 OR
(0,           0,           1,           0,           0,           0,           0,        0,         None,           None,        0,           None,      0), # 5 XOR
(0,           0,           1,           0,           0,           0,           0,        0,         None,           None,        0,           None,      0), # 6 SLT
(0,           0,           0,           None,        1,           1,           0,        0,         None,           None,        0,           None,      0), # 7 MULT
]

SIGNAL_TABLE = [
# AluSrc1    AluSrc2      WriteReg    WriteRegSrc   WriteLO      WriteHI      WriteMem   IsFlowOp   PcSrc         BchAluSrc1   BranchEq     BranchNeg   Reg2Src
(None,        None,        None,        None,        None,        None,        None,     None,      None,       None,        None,        None,      None), # R-Type (!)
(1,           2,           0,           None,        1,           0,           0,        0,         None,       None,        0,           None,      None), # LUI
(None,        None,        1,           1,           0,           0,           0,        1,         0,          None,        0,           None,      None), # J
(None,        None,        1,           1,           0,           0,           0,        1,         1,          1,           0,           None,      None), # JR
(0,           0,           0,           None,        0,           0,           0,        1,         1,          0,           1,           0,         1),    # BEQ
(0,           0,           0,           None,        0,           0,           0,        1,         1,          0,           1,           1,         1),    # BNE
(0,           1,           1,           0,           0,           0,           0,        0,         None,       None,        0,           None,      None), # ADDI
(0,           1,           1,           0,           0,           0,           0,        0,         None,       None,        0,           None,      None), # SLTI
(0,           1,           1,           0,           0,           0,           0,        0,         None,       None,        0,           None,      None), # ANDI
(0,           1,           1,           0,           0,           0,           0,        0,         None,       None,        0,           None,      None), # ORI
(0,           1,           1,           2,           0,           0,           0,        0,         None,       None,        0,           None,      None), # LH
(0,           1,           0,           None,        0,           0,           1,        0,         None,       None,        0,           None,      1),    # SH
(None,        None,        1,           3,           0,           0,           0,        0,         None,       None,        0,           None,      None), # MFHI
(None,        None,        1,           4,           0,           0,           0,        0,         None,       None,        0,           None,      None), # MFLO
]



def signal_tuple_for(op, funct):
    if op == 0:
        return RTYPE_SIGNAL_TABLE[funct]
    else:
        return SIGNAL_TABLE[op]

def stringify_signal_tuple(sigtuple):
    strings = []
    for i, signal in enumerate(sigtuple):
        if signal is not None:
            strings.append(str(signal))
        else:
            strings.append('x' * SIGNAL_TUPLE_SIZE[i])
    return ' '.join(strings)

if __name__ == "__main__":
    import os
    print("# Do not edit, automatically generated by " + os.path.basename(__file__))
    print("Opcode[4] Funct[3] AluSrc1 AluSrc2[2] WriteReg WriteRegSrc[3] WriteLO WriteHI WriteMem IsFlowOp PcSrc BchAluSrc1 BranchEq BranchNeg Reg2Src")
    for op in range(0, INSTRUCTION_COUNT):
        for funct in range(0, FUNC_COUNT):
            sigtuple = signal_tuple_for(op, funct)
            sigstring = stringify_signal_tuple(sigtuple)            
            print("0x{:X} 0x{:X} {}".format(op, funct, sigstring))