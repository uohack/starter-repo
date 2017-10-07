import os, json

"""

get_secret() - Get secrets from secrets.json file

Requirements:
 - Global `here` variable that knows where project root is.

Arguments:
 - service: Name of service you need credentials for, should correspond to upper-level key
 - token: Name of token you need, should correspond to lower-level key

Example:
 - api_key = get_secret('twitter', 'secret')

"""

def get_secret(service, token='null'):
    secrets_path = os.path.abspath('.')
    with open("{}/secrets.json".format(secrets_path)) as data:
        s = json.load(data)
        # If there is no token, return whole parent object
        if token == 'null':
            secret = s['{}'.format(service)]
        else:
            secret = s['{}'.format(service)]['{}'.format(token)]
        return secret

# ----------------------------------------------------------------

"""

Main part of the script

"""

def tell_secret():
    print("Here's the secret: {}".format(get_secret("Rob")))

def ask():
    response = raw_input("Want to hear them? (y/n) ").lower()
    if (response == "y"):
        tell_secret()
    elif (response == "n"):
        print("That's very noble of you.")
    else:
        print("I don't know what that means. Try again")
        ask()

print("Hi. I'm a blabbermouth.\nI know secrets about Rob.")
ask()
print("I must go now, goodbye.")

