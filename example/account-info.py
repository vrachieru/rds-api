import sys
sys.path.append('../')

from rds import RDS

rds = RDS('username', 'password')
client = rds.get_client_info()
client = client['data']['items']

print 'Client id: %s' % client['clientId']
print 'Type: %s\n' % client['type']

print 'Name: %s' % client['name']
print 'BI: %s' % client['bi']
print 'CNP: %s' % client['cnp']
print 'Address: %s, %s, %s' % (client['address'], client['city'], client['state'])
print 'Email: %s\n' % client['email']

print 'Blacklisted: %s' % client['isBlacklisted']
print 'Suspended: %s' % client['isSuspended']
print 'Direct debit: %s' % (client['hasDirectDebit'] != '0')
print 'Email invoice: %s' % (client['hasEmailInvoice'] != 0)
