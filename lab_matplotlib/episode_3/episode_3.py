from matplotlib import pyplot as plt
from collections import defaultdict

with open('students.csv') as file:
    students = file.read().split('\n')

preps = defaultdict(lambda: {str(i) : 0 for i in range(3, 11)})
groups = defaultdict(lambda: {str(i) : 0 for i in range(3, 11)})

for st in students:
    st = st.split(';')
    preps[st[0]][st[2]] += 1
    groups[st[1]][st[2]] += 1

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

