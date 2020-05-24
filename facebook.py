"""Facebook API Handler."""


from requests import HTTPError
import requests
import logging
import yaml

basicConfig(level=logging.DEBUG,
            format="[%(levelname)s] %(asctime)s: %(message)s",
            datefmt="%Y-%d-%m %H:%M:%S %z")

class Facebook():
  """Interact with Facebook handler."""

  HOST = "https://graph.facebook.com/"

  def __init__(self, config_path="configs.yaml"):
    self.CONFIG_PATH = config_path

    with open(config_path, "r") as config:
      self.CONFIG_YAML = yaml.loads(config, Loader=yaml.SafeLoader)

    self.ExchangeShortForLongToken()


    self.SendRequest()


  
  def SendRequest(self, url_params={}):
    """Wrapper for sending GET to Facebook.
  
    Args:
      url_params: Dictionary of parameters to add to GET.
  
    Returns:
      HTTP response or error.
    """
    host = HOST + f"/{config['user_id']}/"
    params = {"fields": "id,name",
              "access_token": config['user_token']}
  
    params.update(url_params)
    
    try:
      response = requests.get(host, params=params)
      logging.info(f"Sending to Facebook: {response.status_code}")
  
      response.encoding = "utf-8"
      return json.dumps(response.text, indent=4)
  
    except HTTPError as e:
      return e


  def ExchangeShortForLongToken(self):
    """Short lived token replaced with long lived.

    Short lived token lasts for several hours, a long lived lasts for 
    two months. Long lived token appended to config file.  
    """
    auth_host = HOST + "/oauth/access_token"

    logging.info(f"Exchanging short lived token in config file with long lived token \
                   \n Using URL: {auth_host}")
    try:
      response = requests.get(auth_host, 
                              params={'grant_type': 'fb_exchange_token', 
                                      'client_id': self.CONFIG_YAML['app_id'],
                                      'client_secret': self.CONFIG_YAML['secret'],
                                      'fb_exchange_token': self.CONFIG_YAML['short_lived_user_token'],
                                      'access_token': self.CONFIG_YAML['short_lived_user_token'])

      response.raise_for_status

    except HTTPError as e:
      logging.error(e)
    except yaml.YAMLError as ye:
      logging.error(f"Check config file, likely a field is missing.  \
                      Refer to the template in GitHub repo. {ye}")

    logging.info(f"Exchange finished. Loading long lived token in config file {self.CONFIG_PATH}.")

    with open(self.CONFIG_PATH, "ar") as config:
      config.write(f"long_lived_token: {response.text}  # PROGRAM GENERATED TOKEN")
      logging.info(f"Added long lived token.")

      logging.info("Refreshing config file to use new data.")
      self.CONFIG_YAML = yaml.load(config, Loader=yaml.SafeLoader)


