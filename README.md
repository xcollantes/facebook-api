Facebook API handler automates token management for sending and receiving common transactions. 

Official Facebook Graph API [documentation](https://developers.facebook.com/docs/graph-api/reference/user).  

# Getting Started
**Library installation**
1. `pip install facebookapi`
1. Import library as `from facebookapi import Facebook`

**Config file**
1. Make a copy of `config.yaml.template` called `config.yaml`.
1. Find user info and place in `config.yaml`. //(TODO): Facebook API UI instructions. 

**Call API**
1. Create class `<my_fb_connection> = Facebook()`
1. Make API calls with methods below.  

**(Optional) Exchange short lived token for long lived token**

  Short lived token
  : Token expiring in 24 hours.

  Long lived token
  : Token expiring in two months. 


# Class methods

## SendRequest
`<my_fb_connection>.SendRequest(dictionary_of_fields)` 

Accepts a dictionary of parameters. 
```
{
    'fields': 'birthday,email,hometown',
}
```

Returns a string object.  
```
{
  "name": "Tester McTestface",
  "hometown": "Cleaveland, Ohio"
  "birthday": "01/01/1970",
  "email": "mctestface@facebook.com",
  "id": "{your-user-id}"
}
```



([docs](https://developers.facebook.com/docs/graph-api/using-graph-api/#reading))
