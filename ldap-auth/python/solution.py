from ldap3 import Server, Connection, ALL, NTLM
from dotenv import load_dotenv
import os

load_dotenv()

def authenticate_ad(url, user, password, get_info=ALL):
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

if __name__ == "__main__":
    server_url = os.getenv('SERVER_URL')
    domain = os.getenv('DOMAIN')
    username = os.getenv('USERNAME')
    password = os.getenv('PASSWORD')
    authenticate_ad(server_url, f'{domain}\\{username}', password)