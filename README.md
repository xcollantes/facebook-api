Facebook API handler automates token management for sending and receiving common transactions. 

Official Facebook Graph API [documentation](https://developers.facebook.com/docs/graph-api/reference/user).  

# Getting Started
**Library installation**
1. `pip install facebookapi`
1. Import library as `from facebookapi import Facebook`
1. Create class `<my_facebook_connection> = Facebook()`
1. Make GET API calls `=<my_faceboon_connection>.SendRequest(dictionary_of_fields)`
1. (Optional) Exchange short lived token for long lived token. 

**Config file**
1. Make a copy of `config.yaml.template` called `config.yaml`.
1. Find user info and place in `config.yaml`. //(TODO): Facebook API UI instructions. 

# Class methods

## SendRequest
**Usage:** `SendRequest({flag_key: flag_value})`
