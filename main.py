import subprocess
import re

subprocess.run(["cp", "sudoers", "sudoers.tmp"])
subprocess.run(["cp", "sudoers", "sudoers.bak"])

userstoremove = []

with open("file.txt", "r") as f:
    for line in f.readlines():
        userstoremove.append(line.rstrip())

# Read the current sudoers file
with open("sudoers.tmp", "r") as sudoers_file:
    sudoers_content = sudoers_file.readlines()

# Iterate through the list and remove each user from sudoers content
# (sudoers_content[:]) the meaning of this is that we iterate over a copy of the list
# Python can't change list values while iterating over it.
for i, line in enumerate(sudoers_content[:]):
    for user in userstoremove:
        if not re.search(rf'^#', sudoers_content[i]):
            # If we match this user on this specific line do the below:
            # 'rf' stands for: r = raw line data
            # and f = formatted string to allow use of variable placeholders like {user}
            if re.search(rf',{user},', sudoers_content[i]):
                sudoers_content[i] = re.sub(rf',{user},', ',', sudoers_content[i])
            elif re.search(rf'{user},', sudoers_content[i]):
                sudoers_content[i] = re.sub(rf'{user},', '', sudoers_content[i])
            elif re.search(rf',{user}', sudoers_content[i]):
                sudoers_content[i] = re.sub(rf',{user}', '', sudoers_content[i])
            elif re.search(rf'{user}', sudoers_content[i]):
                sudoers_content[i] = re.sub(rf'.*', '', sudoers_content[i])

# Write the modified sudoers content back to the file
with open("sudoers.tmp", "w") as sudoers_file:
    sudoers_file.writelines(sudoers_content)

check = subprocess.run(["sudo", "-S", "visudo", "-c", "-f", "sudoers.tmp"])
if check.returncode == 0:
    print("File safe to be copied.")
    print("Users removed from sudoers file.")
    # subprocess.run(["mv", "sudoers.tmp", "sudoers"])
    exit(0)
else:
    print("File not safe to be used")
    exit(1)
