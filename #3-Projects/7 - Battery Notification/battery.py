#7. A battery notification tool

#Logic
"""
On execution, the program reads the system battery
Outputs the battery as a percentage
"""

#Map
"""
Fetch modules to read the battery
Read the battery
Output the battery as a percentage
"""

#Implementation

#Modules
import psutil

#Read the battery
battery = psutil.sensors_battery()

print(f'Your battery is: {battery.percent}%')



#Notes
"""
psutil (python system and process utilities) is a cross-platform library for retrieving information on running processes and system utilization (CPU, memory, disks, network, sensors) in Python.
It is useful mainly for system monitoring, profiling, limiting process resources and the management of running processes.
It implements many functionalities offered by UNIX command line tools such as:
    pstop, lsof, netstat, ifconfig, who, df, kill, free, nice, ionice, iostat, iotop, uptime, pidof, tty, taskset, pmap
    
psutil currently supports the following platforms:
    linux, windows, macOS, FreeBSD, OpenBSD, NetBSD, Sun Solaris, AIX

Reference: https://psutil.readthedocs.io/en/latest/
"""