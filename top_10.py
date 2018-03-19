import os

#changed the directory to root in order to scan the whole system

os.chdir("/")


print(os.system("du -hsx * 2>/dev/null | sort -rh | head -10"))

"""
du command -h option : display sizes in human readable format (e.g., 1K, 234M, 2G).
du command -s option : show only a total for each argument (summary).
du command -x option : skip directories on different file systems.
sort command -r option : reverse the result of comparisons.
sort command -h option : compare human readable numbers. This is GNU sort specific option only.
head command -10 OR -n 10 option : show the first 10 lines.

"""