from google.colab import auth
import os
from oauth2client.client import GoogleCredentials
import getpass
auth.authenticate_user()
creds = GoogleCredentials.get_application_default()
# os.system(f"google-drive-ocamlfuse -headless -id={creds.client_id} -secret={creds.client_secret} < /dev/null 2>&1 | grep URL")
# vcode = getpass.getpass()
# os.system(f"echo {vcode} | google-drive-ocamlfuse -headless -id={creds.client_id} -secret={creds.client_secret}")