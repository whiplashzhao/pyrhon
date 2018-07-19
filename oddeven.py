def text_save(content, filename, mode='a'):
    # Try to save a list variable in txt file.
    file = open(filename, mode)
    for i in range(len(content)):
        file.write(str(content[i]))
    file.close()


name_str = 'aaa'

m = 0

IQ = open("a.txt", 'r')
line_output = ''
for line in IQ.readlines():
    if m == 0:
        line_output = line
    if m % 4 == 0 or m % 4 == 1:
        line_output = line_output + line
    m = m + 1
# 
# print(line_output)
# print(m)
name_file = str(name_str) + 'b.txt'
text_save(line_output, name_file)
IQ.close()
