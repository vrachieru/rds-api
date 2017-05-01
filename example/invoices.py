import sys
sys.path.append('../')

from rds import RDS
from datetime import datetime

rds = RDS('username', 'password')
invoices = rds.get_invoices()
invoices = invoices['data']['items']

for invoice in invoices:
  try:
    if invoices[invoice]['type'] != 'Invoice':
      continue
  except:
    continue

  invoice = invoices[invoice]['items']

  print 'Id: %s' % invoice['id']
  print 'Number: %s' % invoice['number']
  print 'Value: %s RON' % invoice['value']
  print 'Scadent: %s' % datetime.fromtimestamp(float(invoice['scadent']['$id'][5:])).strftime('%d.%m.%Y')
  print 'Status: %s' % invoice['status']
  print 'Comments: %s\n' % invoice['comments']
