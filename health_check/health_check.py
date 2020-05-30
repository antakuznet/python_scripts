#!/usr/bin/env python3
import psutil
# gives a single float value
psutil.cpu_percent()
# gives an object with many fields
psutil.virtual_memory()
# you can convert that object to a dictionary
dict(psutil.virtual_memory()._asdict())
