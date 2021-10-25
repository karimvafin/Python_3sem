from matplotlib import pyplot as plt

with open('students.csv') as file:
    students = file.read().split('\n')

preps = {}
groups = {}

for st in students:
    st = st.split(';')
    if st[0] in preps.keys():
        preps[st[0]][st[2]] += 1
    else:
        preps[st[0]] = dict.fromkeys([str(i) for i in range(3, 11)], 0)
        preps[st[0]][st[2]] = 1
    if st[1] in groups.keys():
        groups[st[1]][st[2]] += 1
    else:
        groups[st[1]] = dict.fromkeys([str(i) for i in range(3, 11)], 0)
        groups[st[1]][st[2]] = 1

colors = ['mediumorchid', 'blueviolet', 'navy', 'royalblue', 'darkslategrey', 'limegreen', 'darkgreen', 'yellow']
clrs = {str(i): k for i, k in zip(range(3, 11), colors)}

i = 0

# comment if groups_plot is demanded
for prep in preps.keys():
    for mark in dict(sorted(preps[prep].items(), key=lambda mark: -mark[1])).keys():
        plt.bar([str(prep)], [preps[prep][mark]], color=clrs[mark])
        i += 1
    i = 0

for mark in clrs:
    plt.bar([str(list(preps.keys())[0])], [0], color=clrs[mark], label=mark)

# code for groups
"""
for group in groups.keys():
    for mark in dict(sorted(groups[group].items(), key=lambda mark: -mark[1])).keys():
        plt.bar([str(group)], [groups[group][mark]], color=clrs[mark])
        i += 1
    i = 0

for mark in clrs:
    plt.bar([str(list(groups.keys())[0])], [0], color=clrs[mark], label=mark)
"""
plt.legend()
plt.title('Marks per preps')
plt.xlabel('Prep')
plt.ylabel('Number of marks')
plt.savefig('preps.png')

