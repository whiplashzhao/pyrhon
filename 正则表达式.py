import re


def name_of_email(addr):
    m = re.match(r'<*([a-zA-Z]*[\s]*[a-zA-Z]*)>*[\s]*[a-zA-Z]*@[\w]*[(.com| .org)$]', addr).groups()
    return m[0]


assert name_of_email('<Tom Paris> tom@voyager.org') == 'Tom Paris'
assert name_of_email('tom@voyager.org') == 'tom'
print('ok')
