import xmlrpc.client

conn = xmlrpc.client.ServerProxy("http://www.pythonchallenge.com/pc/phonebook.php")

conn.system.listMethods()
# ['phone', 'system.listMethods', 'system.methodHelp', 'system.methodSignature', 'system.multicall', 'system.getCapabilities']

conn.system.methodHelp("phone")
# 'Returns the phone of a person'

conn.system.methodSignature("phone")
# [['string', 'string']]

conn.phone("Bert")
# '555-ITALY'