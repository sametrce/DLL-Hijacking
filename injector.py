import sys
from ctypes import*

PAGE_READWRITE     =   0x04
PROCESS_ALL_ACCESS =   ( 0x000F0000 | 0x001  00000 | 0xFFF )
VIRTUAL_MEM        =   ( 0x1000 | 0x2000 )

kernel32 = windll.kernel32
pid      = sys.argv[1]
dll_path = sys.argv[2]
dll_len  = len(dll_path)

#Get a handle to the process we are injecting into
h_process = kernel32.OpenProcess( PROCESS_ALL_ACCESS, False, int(pid) )

if not h_process:
  print "[*] Couldn't acquire a handle to PID: %s" % pid
  sys.exit(0)
