import apiclient

class NsxtClient(object):
    def __init__(self, uri, user, password, insecure, ca_file=None):
        self.uri = uri
        self.user = user
        self.password = password
        self.insecure = insecure
        self.ca_file = ca_file
        self.client =  apiclient.RESTClient(uri, user, password, insecure, ca_file)

    def get_transport_zones(self):
        result = self.client.url_get('transport-zones')
        return result

    def get_dhcp_profile(self):
        result = self.client.url_get('dhcp/server-profiles')
        return result

    def get_ip_block(self):
        result = self.client.url_get('pools/ip-blocks')
        return result

    def get_logical_router(self):
        result = self.client.url_get('logical-routers')
        return result
