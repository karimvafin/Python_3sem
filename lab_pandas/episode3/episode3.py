import pandas as pd
from matplotlib import pyplot as plt

df1 = pd.read_html("students/results_ejudge.html")[0]
df2 = pd.read_excel("students/students_info.xlsx")

df1.fillna(0, inplace=True)
df2.dropna(inplace=True)

# I part
df2["Solved"] = [int(df1.loc[df1.User == i].Solved) for i in df2.login]
faculty_groups = sorted(list(set(df2.group_faculty)))
groups_out = sorted(list(set(df2.group_out)))
average_per_faculty_groups = [round(df2.loc[df2.group_faculty == group].Solved.mean(), 1) for group in faculty_groups]
average_per_groups_out = [round(df2.loc[df2.group_out == group].Solved.mean(), 3) for group in groups_out]
fig, ax = plt.subplots(1, 2)

ax[0].bar(list(map(str, faculty_groups)), average_per_faculty_groups)
ax[0].set_xlabel('faculty_group')
ax[0].set_ylabel('average mark')

ax[1].bar(list(map(str, groups_out)), average_per_groups_out)
ax[1].set_xlabel('group_out')

fig.suptitle('Average mark in a group')
plt.savefig('average_marks.png')

# II part
users = df1.loc[(df1.H >= 10) | (df1.G >= 10)].User
print("Номера факультетских групп: ", set([int(df2[df2.login == login].group_faculty) for login in list(users)]))
print("Номера групп по информатике: ", set([int(df2[df2.login == login].group_out) for login in list(users)]))
