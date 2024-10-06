// Test file Mult01 for Mult.vm
// Follows the Test Scripting Language format described in 
// Appendix B of the book "The Elements of Computing Systems"

load Mult.vm,
output-file Mult01.out,
compare-to Mult01.cmp,
output-list sp%D1.6.1 local%D1.6.1 argument%D1.8.1 this%D1.6.1 that%D1.6.1
            RAM[16]%D1.6.1 RAM[17]%D1.6.1 RAM[18]%D1.6.1
            local[0]%D1.8.1 local[1]%D1.8.1 local[2]%D1.8.1
            argument[0]%D1.11.1 argument[1]%D1.11.1 argument[2]%D1.11.1;

set sp 256,        // stack pointer
set local 310,     // base address of the local segment
set argument 410,  // base address of the argument segment
set this 3010,     // base address of the this segment
set that 3020,     // base address of the that segment

set RAM[16] 5,   // static 0 (x = 5)
set RAM[17] 7,   // static 1 (y = 7)
set RAM[18] 0,   // static 2

set local[0] 1,  // local 0
set local[1] 2,  // local 1
set local[2] 3,  // local 2

set argument[0] 110,  // argument 0
set argument[1] 210,  // argument 1
set argument[2] 310;  // argument 2

repeat 100 {        // Adjust this number based on the VM file's instructions
  vmstep;
}
output;
