import requests

class RDS():
  BASE_URL = 'https://digicare.rcs-rds.ro',
  HEADERS = {
    'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.8',
    'Connection': 'keep-alive',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Host': 'digicare.rcs-rds.ro',
    'Origin': 'https://digicare.rcs-rds.ro',
    'Referer': 'https://digicare.rcs-rds.ro/'
  }

  def __init__(self, username, password):
    self.config = dict()
    self.config['username'] = username
    self.config['password'] = password

    self.session = requests.Session()
    self.login()

  def login(self):
    '''
    Authenticates user with username and password.
    '''
    payload = {
      'do': 'call-static',
      'instance': 'Client',
      'args': '["%s", "%s"]' % (self.config['username'], self.config['password']),
      'method': 'login',
      'v': 198
    }
    return self.rpc(payload)

  def get_news(self):
    '''
    Gets the lates news related to RCS&RDS activity.
    '''
    return self.rpc_load('/news')

  def get_client_info(self):
    '''
    Gets client info, such as client name, type and address.
    '''
    return self.rpc_load('/info')

  def get_account_info(self):
    '''
    Gets account info, such account number, email, last authentication and creation dates.
    '''
    return self.rpc_load('/info/account')

  def get_locations(self):
    '''
    Gets a list of client locations.
    '''
    return self.rpc_load('/locations')

  def get_location(self, locationId):
    '''
    Gets location details by location id.
    '''
    return self.rpc_load('Location:%s' % locationId)

  def get_install_addresses(self):
    '''
    Gets a list of addresses where the client has services installed.
    '''
    return self.rpc_load('/locations/installAddresses')

  def get_installed_services_at_address(self, addressId):
    '''
    Gets a list of services installed at a speciffic address.
    '''
    return self.rpc_load('Location_Address_Service:%s' % addressId)

  def get_services(self):
    '''
    Gets a list of installed services.
    '''
    return self.rpc_load('/services')

  def get_invoices(self):
    '''
    Gets a list of invoices.
    '''
    return self.rpc_load('/invoices')

  def download_invoice(self, invoiceId):
    '''
    Downloads an invoice by id.
    '''
    return self.session.get('%s/xhr-download-invoice.php' % self.BASE_URL, headers=self.HEADERS, data={'id': invoiceId})

  def rpc_load(self, id):
    '''
    Makes a RCP load request for the specified resource.
    '''
    payload = {
      'do': 'load',
      'id': id,
      'v': 256
    }
    return self.rpc(payload)

  def rpc(self, payload):
    '''
    Makes a RPC request with the specified payload.
    '''
    response = self.session.post('%s/rpc.php' % self.BASE_URL, headers=self.HEADERS, data=payload)
    return response.json()
