// Test file Abs02 for Abs.vm
// Follows the Test Scripting Language format described in 
// Appendix B of the book "The Elements of Computing Systems"

load Abs.vm,
output-file Abs02.out,
compare-to Abs02.cmp,
output-list sp%D1.6.1 local%D1.6.1 argument%D1.8.1 this%D1.6.1 that%D1.6.1
            RAM[16]%D1.6.1 RAM[17]%D1.6.1 RAM[18]%D1.6.1
            local[0]%D1.8.1 local[1]%D1.8.1 local[2]%D1.8.1
            argument[0]%D1.11.1 argument[1]%D1.11.1 argument[2]%D1.11.1;

set sp 256,        // stack pointer
set local 320,     // base address of the local segment
set argument 420,  // base address of the argument segment
set this 3020,     // base address of the this segment
set that 3030,     // base address of the that segment

set RAM[16] -9,  // static 0
set RAM[17] 5,  // static 1
set RAM[18] 0,  // static 2

set local[0] -50,  // local 0
set local[1] 30,  // local 1
set local[2] -25,  // local 2

set argument[0] 100,  // argument 0
set argument[1] -150,  // argument 1
set argument[2] 80;  // argument 2

repeat 25 {        // Adjust as needed
  vmstep;
}
output;
