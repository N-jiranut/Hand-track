# import pandas as pd
# # main={}
# # main = pd.DataFrame(main)
# # main.to_excel('data/test1.xlsx')
# # print('reset successfully.')


# from openpyxl import load_workbook

# # Existing Excel file
# existing_file = 'data/test1.xlsx'

# # New data to append
# new_data = [['aaa', 28, 55000],["bbb", 22, 20000,000]]

# # Load existing workbook
# wb = load_workbook(existing_file)

# # Select the active sheet
# ws = wb.active

# # Append new data
# for row in new_data:
#     print(row)
#     ws.append(row)

# Save the workbook
# wb.save(existing_file)

# test = []
# add = ["asdasd","555ตลก"]
# new = ["abc","efg"]
# for i in range(len(add)):
#     test.append(add[i])
#     test.append("abc")
# for i in range(21):
#     print(i)
# add.extend(new)
# print(add)



words = ["Hey", "there","kuy"]
for i, word in enumerate(words):
    # print(f"'Word #{i}: <{word}> has {len(word)} letters.'")
    print(word)
