import pandas as pd
from matplotlib import pyplot as plt

df1 = pd.read_html("students/results_ejudge.html")[0]
df2 = pd.read_excel("students/students_info.xlsx")

df1.fillna(0, inplace=True)
df2.dropna(inplace=True)

df = df1.merge(df2, how='inner', left_on='User', right_on='login')

# I part
faculty_groups = df.groupby(['group_faculty']).Solved.mean().index
average_per_faculty_groups = df.groupby(['group_faculty']).Solved.mean().values

groups_out = df.groupby(['group_out']).Solved.mean().index
average_per_groups_out = df.groupby(['group_out']).Solved.mean().values

fig, ax = plt.subplots(1, 2)

ax[0].bar(list(map(str, faculty_groups)), average_per_faculty_groups)
ax[0].set_xlabel('faculty_group')
ax[0].set_ylabel('average mark')

ax[1].bar(list(map(str, groups_out)), average_per_groups_out)
ax[1].set_xlabel('group_out')

fig.suptitle('Average mark in a group')
plt.savefig('average_marks.png')

# II part

print("Номера факультетских групп: ", set(df.loc[(df1.H >= 10) | (df1.G >= 10)].group_faculty))
print("Номера групп по информатике: ", set(df.loc[(df1.H >= 10) | (df1.G >= 10)].group_out))
