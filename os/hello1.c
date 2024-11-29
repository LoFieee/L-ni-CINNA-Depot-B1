void _start()
{
    const char message[] = "Hello, World!\n";
    asm volatile(
        "mov $4, %%eax\n\t"     // Syscall number for write (4 in 32-bit)
        "mov $1, %%ebx\n\t"     // File descriptor 1 (stdout)
        "mov %[msg], %%ecx\n\t" // Pointer to the message
        "mov %[len], %%edx\n\t" // Length of the message
        "int $0x80"             // Make the syscall (32-bit interrupt)
        :
        : [msg] "r"(message), [len] "r"(14)
        : "eax", "ebx", "ecx", "edx");

    asm volatile(
        "mov $1, %%eax\n\t"    // Syscall number for exit (1 in 32-bit)
        "xor %%ebx, %%ebx\n\t" // Exit code 0
        "int $0x80"            // Make the syscall
        :
        :
        : "eax", "ebx");
}
