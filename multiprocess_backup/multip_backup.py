#!/usr/bin/env python

import subprocess
import os
from multiprocessing import Pool

base_path = ""
src = base_path + "/data/prod/"
dest = base_path + "/data/prod_backup/"

def run_sync(dir):
        subprocess.call(["rsync", "-arq", dir, dest])

def main():
        dir_list = []
        os.chdir(src)
        for root, dirs, files in os.walk("."):
                for dir in dirs:
                        dir_list.append(os.path.join(root, dir))
        p = Pool(len(dir_list))
        p.map(run_sync, dir_list)

if __name__ == "__main__":
        main()
