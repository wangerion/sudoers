import re

a = ["user1,user2,user3,user4    ALL=(ALL)       ALL",
     "user8    ALL=(ALL)       ALL",
     "user6    ALL=(ALL)       ALL",
     "user1,user2,user3,user4    ALL=(ALL)       ALL"
     ]
userstoremove = ["user1", "user3", "user8"]

for i, line in enumerate(a[:]):
    for user in userstoremove:
        if re.search(rf',{user},', a[i]):
            print(i)
            a[i] = re.sub(rf',{user},', ',', a[i])
            print(user)
        elif re.search(rf'{user},', a[i]):
            a[i] = re.sub(rf'{user},', '', a[i])
            print(user)
        elif re.search(rf',{user}', a[i]):
            a[i] = re.sub(rf',{user}', '', a[i])
            print(user)
        elif re.search(rf'{user}', a[i]):
            #a[i] = re.sub(rf'.*', '', a[i])
            a.remove(line)
            print(user)

print(a)
