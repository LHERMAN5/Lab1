import requests

#print(requests.__version__)

resp = requests.get("https://raw.githubusercontent.com/LHERMAN5/Lab1/main/lab1.py?token=GHSAT0AAAAAACHR3TSY5IE3D4ZULCY2WDFIZILPNRA")

print(resp.text)