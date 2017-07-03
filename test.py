import  nsxtclient


def conn():
    return nsxtclient.NsxtClient("10.161.42.82", "admin", "Admin!23Admin", True)

def test_get_transport_zones():
    nsxt_client= conn()
    return nsxt_client.get_transport_zones()

def test_get_dhcp_profile():
    return conn().get_dhcp_profile()

def test_get_ip_block():
    return conn().get_ip_block()

def test_get_logical_router():
    return conn().get_logical_router()

if __name__ == '__main__':
    trans = test_get_transport_zones()
    print trans

    dhcp_profile = test_get_dhcp_profile()
    print dhcp_profile

    ip_block = test_get_ip_block()
    print ip_block


    logical_router = test_get_logical_router()
    print logical_router
