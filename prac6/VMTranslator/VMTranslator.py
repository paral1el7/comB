class VMTranslator:
    
    lable_num = -1
    
    def new_label():
        
        VMTranslator.lable_num += 1
        return str(VMTranslator.lable_num)


    def vm_push(segment, offset):
        '''Generate Hack Assembly code for a VM push operation'''
        
        ass_str = ""  # assembly code
        if (segment == "constant"):
            new_seg = str(offset)
        if (segment == "static"):
            new_seg = str(16+offset)
        if (segment == "local"):
            new_seg = "LCL"
        if (segment == "pointer"):
            new_seg = "R" + str(3 + offset)
        if (segment == "temp"):
            new_seg = "R" + str(5 + offset)
        if (segment == "argument"):
            new_seg = "ARG"
        if (segment == "this"):
            new_seg = "THIS"
        if (segment == "that"):
            new_seg = "THAT"
            
        
        if segment == "constant":
                ass_str += f"@{new_seg}\nD = A\n"
                
        if (segment == "static" or segment == "pointer" or segment == "temp"):
                ass_str += f"@{new_seg}\nD = M\n"


        if (segment == "local" or segment == "this" or segment == "that" or segment == "argument"):
            ass_str += (f"@{new_seg}\n"
                        "D = M\n"
                        f"@{str(offset)}\n"
                        "A = D + A\nD=M\n")
      
        
        ass_str += ("@SP\n"
                    "A = M\n"
                    "M = D\n"
                    "@SP\n"
                    "M = M + 1\n")

        return ass_str
        

    def vm_pop(segment, offset):
        '''Generate Hack Assembly code for a VM pop operation'''
        
        ass_str = ""  # assembly code

        if segment == "constant":
            new_seg = str(offset)
        elif segment == "static":
            new_seg = str(16 + offset)
        elif segment == "local":
            new_seg = "LCL"
        elif segment == "pointer":
            new_seg = "R" + str(3 + offset)
        elif segment == "temp":
            new_seg = "R" + str(5 + offset)
        elif segment == "argument":
            new_seg = "ARG"
        elif segment == "this":
            new_seg = "THIS"
        elif segment == "that":
            new_seg = "THAT"
            
        ass_str += f"@{new_seg}\n"

        if (segment == "static" or segment == "temp" or segment == "pointer"):
            ass_str += "D = A\n"
        elif (segment == "local" or segment == "this" or segment == "that" or segment == "argument"):
            ass_str += ("D = M\n"
                        f"@{str(offset)}\n"
                        "D = D + A\n")

        ass_str += ("@R13\n"
                      "M = D\n"
                      "@SP\n"
                      "AM = M - 1\n"
                      "D = M\n"
                      "@R13\n"
                      "A = M\n"
                      "M = D\n")

        return ass_str


    def vm_add():
        '''Generate Hack Assembly code for a VM add operation'''

        return ("@SP\n"
                "AM = M-1\n"
                "D = M\n"
                "A = A-1\n"
                "M = D + M")

    def vm_sub():
        '''Generate Hack Assembly code for a VM sub operation'''
        
        return ("@SP\n"
                "AM = M - 1\n"
                "D = M\n"
                "A = A - 1\n"
                "M = M - D")

    def vm_neg():
        '''Generate Hack Assembly code for a VM neg operation'''
        
        return ("@SP\n"
                "A = M - 1\n"
                "M = !M\n"
                "M = M + 1")

    def vm_eq():
        '''Generate Hack Assembly code for a VM eq operation'''
        
        label = VMTranslator.new_label()
        
        return ("@SP\n"
                "AM = M - 1\n"
                "D = M\n"
                "A = A - 1\n"
                "D = M - D\n"
                f"@EQ.true_{label}\n"
                "D;JEQ\n"
                "@SP\n"
                "A = M - 1\n"
                "M = 0\n"
                f"@EQ.skip_{label}\n"
                "0;JMP\n"
                f"(EQ.true_{label})\n"
                "@SP\n"
                "A = M - 1\n"
                "M = -1\n"
                f"(EQ.skip_{label})")


    def vm_gt():
        '''Generate Hack Assembly code for a VM gt operation'''
        
        label = VMTranslator.new_label()
        
        return ("@SP\n"
                "AM = M - 1\n"
                "D = M\n"
                "A = A - 1\n"
                "D = M - D\n"
                f"@GT.true{label}\n"
                "D;JGT\n"
                "@SP\n"
                "A = M - 1\n"
                "M = 0\n"
                f"@GT.skip{label}\n"
                "0;JMP\n"
                f"(GT.true{label})\n"
                "@SP\n"
                "A = M - 1\n"
                "M = -1\n"
                f"(GT.skip{label})")

    def vm_lt():
        '''Generate Hack Assembly code for a VM lt operation'''
        
        label = VMTranslator.new_label()
        
        return ("@SP\n"
                "AM = M - 1\n"
                "D = M\n"
                "A = A - 1\n"
                "D = M - D\n"
                f"@LT.true{label}\n"
                "D; JLT\n"
                "@SP\n"
                "A = M - 1\n"
                "M = 0\n"
                f"@LT.skip{label}\n"
                "0; JMP\n"
                f"(LT.true{label})\n"
                "@SP\n"
                "A = M - 1\n"
                "M = -1\n"
                f"(LT.skip{label})"
            )

    def vm_and():
        '''Generate Hack Assembly code for a VM and operation'''
        
        return ("@SP\n"
                "AM = M - 1\n"
                "D = M\n"
                "A = A - 1\n"
                "M = M & D")

    def vm_or():
        '''Generate Hack Assembly code for a VM or operation'''
        
        return ("@SP\n"
                "AM = M - 1\n"
                "D = M\n"
                "A = A - 1\n"
                "M = M | D")

    def vm_not():
        '''Generate Hack Assembly code for a VM not operation'''
        
        return ("@SP\n"
                "A = M - 1\n"
                "M = !M")

    def vm_label(label):
        '''Generate Hack Assembly code for a VM label operation'''
        
        return f"({label})"


    def vm_goto(label):
        '''Generate Hack Assembly code for a VM goto operation'''
        
        return f"@{label}\n0;JMP"


    def vm_if(label):
        '''Generate Hack Assembly code for a VM if-goto operation'''
        
        return ("@SP\n"
                "AM = M - 1\n"
                "D = M\n"
                f"@{label}\n"
                "D;JNE")


    def vm_function(function_name, n_vars):
        '''Generate Hack Assembly code for a VM function operation'''
        
        ass_str = (f"(FUNC.defMod.{function_name})\n"
                    "@SP\n"
                    "A = M\n")
        
        for i in range(n_vars):
            ass_str += "M=0\nA=A+1\n"
            
        ass_str += ("D=A\n"
                    "@SP\n"
                    "M=D")

        return ass_str


    def vm_call(function_name, n_args):
        '''Generate Hack Assembly code for a VM call operation'''
        
        label = VMTranslator.new_label()
        
        return ("@SP\n"
                "D = M\n"
                "@R13\n"
                "M = D\n"
                f"@RET.{label}\n"
                "D = A\n"
                "@SP\n"
                "A = M\n"
                "M = D\n"
                "@SP\n"
                "M = M + 1\n"
                "@LCL\n"
                "D = M\n"
                "@SP\n"
                "A = M\n"
                "M = D\n"
                "@SP\n"
                "M = M + 1\n" 
                "@ARG\n"
                "D = M\n"
                "@SP\n"
                "A = M\n"
                "M = D\n"
                "@SP\n"
                "M = M + 1\n"
                "@THIS\n"
                "D = M\n"
                "@SP\n"
                "A = M\n"
                "M = D\n"
                "@SP\n"
                "M = M + 1\n"
                "@THAT\n"
                "D = M\n"
                "@SP\n"
                "A = M\n"
                "M = D\n"
                "@SP\n"
                "M = M + 1\n"
                "@R13\n"
                "D = M\n"
                f"@{n_args}\n"
                "D = D - A\n"
                "@ARG\n"
                "M = D\n"
                "@SP\n"
                "D = M\n"
                "@LCL\n"
                "M = D\n"
                f"@FUNC.defMod.{function_name}\n"
                "0;JMP\n"
                f"(RET.{label})")


    def vm_return():
        '''Generate Hack Assembly code for a VM return operation'''
        
        return ("@LCL\n"
                "D = M\n"
                "@5\n"
                "A = D - A\n"
                "D = M\n"
                "@R13\n"
                "M = D\n"
                "@SP\n"
                "A = M - 1\n"
                "D = M\n"
                "@ARG\n"
                "A = M\n"
                "M = D\n"
                "D = A + 1\n"
                "@SP\n"
                "M = D\n"
                "@LCL\n"
                "AM = M - 1\n"
                "D = M\n"
                "@THAT\n"
                "M = D\n"
                "@LCL\n"
                "AM = M - 1\n"
                "D = M\n"
                "@THIS\n"
                "M = D\n"
                "@LCL\n"
                "AM = M - 1\n"
                "D = M\n"
                "@ARG\n"
                "M = D\n"
                "@LCL\n"
                "A = M - 1\n"
                "D = M\n"
                "@LCL\n"
                "M = D\n"
                "@R13\n"
                "A = M\n"
                "0; JMP")


# A quick-and-dirty parser when run as a standalone script.
if __name__ == "__main__":
    import sys
    if(len(sys.argv) > 1):
        with open(sys.argv[1], "r") as a_file:
            for line in a_file:
                tokens = line.strip().lower().split()
                if(len(tokens)==1):
                    if(tokens[0]=='add'):
                        print(VMTranslator.vm_add())
                    elif(tokens[0]=='sub'):
                        print(VMTranslator.vm_sub())
                    elif(tokens[0]=='neg'):
                        print(VMTranslator.vm_neg())
                    elif(tokens[0]=='eq'):
                        print(VMTranslator.vm_eq())
                    elif(tokens[0]=='gt'):
                        print(VMTranslator.vm_gt())
                    elif(tokens[0]=='lt'):
                        print(VMTranslator.vm_lt())
                    elif(tokens[0]=='and'):
                        print(VMTranslator.vm_and())
                    elif(tokens[0]=='or'):
                        print(VMTranslator.vm_or())
                    elif(tokens[0]=='not'):
                        print(VMTranslator.vm_not())
                    elif(tokens[0]=='return'):
                        print(VMTranslator.vm_return())
                elif(len(tokens)==2):
                    if(tokens[0]=='label'):
                        print(VMTranslator.vm_label(tokens[1]))
                    elif(tokens[0]=='goto'):
                        print(VMTranslator.vm_goto(tokens[1]))
                    elif(tokens[0]=='if-goto'):
                        print(VMTranslator.vm_if(tokens[1]))
                elif(len(tokens)==3):
                    if(tokens[0]=='push'):
                        print(VMTranslator.vm_push(tokens[1],int(tokens[2])))
                    elif(tokens[0]=='pop'):
                        print(VMTranslator.vm_pop(tokens[1],int(tokens[2])))
                    elif(tokens[0]=='function'):
                        print(VMTranslator.vm_function(tokens[1],int(tokens[2])))
                    elif(tokens[0]=='call'):
                        print(VMTranslator.vm_call(tokens[1],int(tokens[2])))

        
