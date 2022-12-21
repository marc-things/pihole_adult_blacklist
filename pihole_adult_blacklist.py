#!/usr/bin/env python3

import tarfile
import subprocess

# download tar.gz file
subprocess.call(['curl', '-o', 'adult.tar.gz', 'http://dsi.ut-capitole.fr/blacklists/download/adult.tar.gz'])

# extract the contents of the downloaded file
with tarfile.open('adult.tar.gz') as my_tar:
    
    import os
    
    def is_within_directory(directory, target):
        
        abs_directory = os.path.abspath(directory)
        abs_target = os.path.abspath(target)
    
        prefix = os.path.commonprefix([abs_directory, abs_target])
        
        return prefix == abs_directory
    
    def safe_extract(tar, path=".", members=None, *, numeric_owner=False):
    
        for member in tar.getmembers():
            member_path = os.path.join(path, member.name)
            if not is_within_directory(path, member_path):
                raise Exception("Attempted Path Traversal in Tar File")
    
        tar.extractall(path, members, numeric_owner=numeric_owner) 
        
    
    safe_extract(my_tar)

# add domain from each line in the specified file to pihole blacklist
with open('adult/domains', 'r') as adult_list:
    for line in adult_list.readlines():
        subprocess.call(['pihole', '-b', line.strip()])