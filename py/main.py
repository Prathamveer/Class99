import os
import shutil

correct_path = 'F:/WhitehatJr/Class99/'

print('Before copying files', os.listdir(correct_path))
source = 'F:/WhitehatJr/Class99/test.txt'
destination = 'F:/WhitehatJr/Class99/testcopy.txt'

best = shutil.copy(source, destination)
print('File has been copied.', os.listdir(correct_path))


# rootextension = os.path.splitext(correct_path)

# print('root part', rootextension[0])
# print('ext part', rootextension[1])



# wrong_path = 'abc/hello/sup/bonjour/'

# isExist1 = os.path.exists(wrong_path)
# isExist2 = os.path.exists(correct_path)

# print(isExist1)
# print(isExist2)


# os.mkdir('F:/WhitehatJr/Class99/backup_test')
# print(os.getcwd())