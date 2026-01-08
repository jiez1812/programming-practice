from ldap3 import Server, Connection, ALL, NTLM

def authenticate_ad(url, user, password):
    try:
        server = Server(url)
        conn = Connection(
            server,
            user=user,
            password=password,
            authentication=NTLM,
            auto_bind=True
        )
        print(f'Authenticated: {conn.bound}')
        conn.unbind()
        return True

    except Exception as e:
        print(f'Authentication failed: {e}')
        return False
    
def find_user_dn(url, user, password, search_base, search_filter):
    try:
        server = Server(url)
        conn = Connection(
            server,
            user=user,
            password=password,
            authentication=NTLM,
            auto_bind=True
        )
        
        conn.search(search_base, search_filter, attributes=['distinguishedName'])
        
        if conn.entries:
            user_dn = conn.entries[0].distinguishedName.value
            print(f'User DN: {user_dn}')
            conn.unbind()
            return user_dn
        else:
            print('User not found')
            conn.unbind()
            return None

    except Exception as e:
        print(f'Error finding user DN: {e}')
        return None