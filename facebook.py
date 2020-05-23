"""Facebook API Handler."""


from requests import HTTPError
import requests
import logging
import yaml


class Facebook():
  """Interact with Facebook handler."""

  def __init__(self, config_path="configs.yaml"):
    with open(config_path, "r") as config:
      config_yaml = yaml.loads(config, Loader=yaml.SafeLoader)


  

  
  def SendRequest(self, config, url_params={}):
    """Wrapper for sending GET to Facebook.
  
    Args:
      config: YAML object of config file.
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
