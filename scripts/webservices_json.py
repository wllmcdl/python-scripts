import json

data = '''
{
    "name":"William",
    "phone": 
    {
        "type":"intl",
        "number":"+1 888 888 888"
    },
    "email": 
    {
        "hide":"yes"
    }
}
'''

info = json.loads(data)
print('Name:', info["name"])
print('Hide:', info["email"]["hide"])