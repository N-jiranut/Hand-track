# import pandas as pd
# print(a)

# importing the module
import pandas as pd
# a = pd.read_excel('data/Book2.xlsx')  
# # creating the DataFrame
# marks_data = pd.DataFrame({'ID': ["c","d"],
#                            'Name': ["c","d"]})
# main = pd.concat([a, marks_data], ignore_index=True)
main = {}
main = pd.DataFrame(main)
# data={}
# for i in range(21):
#        data.update({"LH"+str(i):[None]})
# for i in range(21):
#        data.update({"RH"+str(i):[None]})
# for i in range(33):
#        data.update({"B"+str(i):[None]})
        
# new = pd.DataFrame({'ID': ["a","b"],'Name': ["a","b"]})

# a = 200
# b = 20
# print(new)
# determining the name of the file
# file_name = 'data/Book3.xlsx'

# saving the excel
# xd=pd.DataFrame(data)
# df = pd.concat([marks_data, new], ignore_index=True)
# print(main)
# data["LH"+str(1)] = (str(a)+"-"+str(b))
# data=pd.DataFrame(data)
# data.to_excel('data/test.xlsx')
# print(data["LH"+str(1)])
main.to_excel('data/test.xlsx')
print('reset successfully.')
