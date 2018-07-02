test_file = open('/work/pj/09_test.txt','a+')
text1 = test_file.read()
print(text1)
test_file.write('append part for testing.')
test_file = open('/work/pj/test.txt','r')
text2 = test_file.read()
print(text2)
test_file.close()

