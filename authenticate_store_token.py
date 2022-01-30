import requests, json, sys

# This code will authenticate with NX-OS device running API and return the token, common task for everything.
# Defines function to authneticate and get token. Give user, pass, and IP in X.X.X.X quoted format 
# Example use: nx_authenticate('admin', 'cisco!123', '10.82.138.153') 

def nx_authenticate_get_token(un, pw, IP):
    # This is the payload dictionary. Here you should replace this with environment variables or your user:pw
    payload = {'aaaUser': {'attributes': {'name': un, 'pwd': pw}}}

    # This makes the request to the proper end point, constructs URL and then uses requests for POST 
    endpoint = 'https://' + IP + '/api/mo/aaaLogin.json'
    r = requests.post(endpoint, json=payload, verify=False)

    # This grabs the token by taking value of dictionary, list, dictionary and returns 
    token = r.json()['imdata'][0]['aaaLogin']['attributes']['token']
    return(token)

# If code is run from terminal, pass three arguments and print the token value on CLI
if __name__ == "__main__":
    un = sys.argv[1]
    pw = sys.argv[2]
    IP = sys.argv[3]
    token = nx_authenticate_get_token(un, pw, IP)
    print('\n' + "success! token is " + token)
