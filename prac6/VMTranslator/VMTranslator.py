class VMTranslator:

    def vm_push(segment, offset):
        '''Generate Hack Assembly code for a VM push operation'''
        assembly_code = []
        if segment == "constant":
            assembly_code.append(f"@{offset}")
            assembly_code.append("D=A")
        elif segment == "local":
            assembly_code.append(f"@{offset}")
            assembly_code.append("D=A")
            assembly_code.append("@LCL")
            assembly_code.append("A=M+D")
            assembly_code.append("D=M")
        # 处理其他 segment (argument, this, that, temp, pointer, static, etc.)
        
        # 将 D 推入堆栈
        assembly_code.append("@SP")
        assembly_code.append("A=M")
        assembly_code.append("M=D")
        assembly_code.append("@SP")
        assembly_code.append("M=M+1")
        return "\n".join(assembly_code)

    def vm_pop(segment, offset):
        '''Generate Hack Assembly code for a VM pop operation'''
        assembly_code = []
        if segment in ["local", "argument", "this", "that"]:
            if segment == "local":
                base = "LCL"
            elif segment == "argument":
                base = "ARG"
            elif segment == "this":
                base = "THIS"
            elif segment == "that":
                base = "THAT"
            # 将目标地址存到 R13
            assembly_code.append(f"@{offset}")
            assembly_code.append("D=A")
            assembly_code.append(f"@{base}")
            assembly_code.append("D=M+D")
            assembly_code.append("@R13")
            assembly_code.append("M=D")
            # 从堆栈弹出
            assembly_code.append("@SP")
            assembly_code.append("M=M-1")
            assembly_code.append("A=M")
            assembly_code.append("D=M")
            # 将堆栈中的值存到目标地址
            assembly_code.append("@R13")
            assembly_code.append("A=M")
            assembly_code.append("M=D")
        # 处理 temp, pointer, static 等 segment
        return "\n".join(assembly_code)

    def vm_add():
        '''Generate Hack Assembly code for a VM add operation'''
        return "@SP\nM=M-1\nA=M\nD=M\n@SP\nM=M-1\nA=M\nM=M+D\n@SP\nM=M+1\n"

    def vm_sub():
        '''Generate Hack Assembly code for a VM sub operation'''
        return "@SP\nM=M-1\nA=M\nD=M\n@SP\nM=M-1\nA=M\nM=M-D\n@SP\nM=M+1\n"

    # 实现其他命令：eq, lt, gt, and, or, not

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        input_file = sys.argv[1]
        output_file = input_file.replace(".vm", ".asm")  # 生成 .asm 文件
        assembly_code = []

        with open(input_file, "r") as vm_file:
            for line in vm_file:
                tokens = line.strip().split()
                if len(tokens) == 3:
                    if tokens[0] == "push":
                        assembly_code.append(VMTranslator.vm_push(tokens[1], int(tokens[2])))
                    elif tokens[0] == "pop":
                        assembly_code.append(VMTranslator.vm_pop(tokens[1], int(tokens[2])))
                elif len(tokens) == 1:
                    if tokens[0] == "add":
                        assembly_code.append(VMTranslator.vm_add())
                    elif tokens[0] == "sub":
                        assembly_code.append(VMTranslator.vm_sub())
                    # 处理其他命令：neg, eq, gt, lt, and, or, not 等

        # 将汇编代码写入输出文件
        with open(output_file, "w") as asm_file:
            asm_file.write("\n".join(assembly_code))

        print(f"Translated {input_file} to {output_file}")
