
import logging
import os
import pprint

from googleads import dfp
from jinja2 import Template, FileSystemLoader, Environment

from dfp.client import get_client


logger = logging.getLogger(__name__)

def create_creatives(creatives):
  """
  Creates creatives in DFP.

  Args:
    creatives (arr): an array of objects, each a creative configuration
  Returns:
    an array: an array of created creative IDs
  """
  dfp_client = get_client()
  creative_service = dfp_client.GetService('CreativeService',
    version='v201802')
  creatives = creative_service.createCreatives(creatives)

  # Return IDs of created line items.
  created_creative_ids = []
  for creative in creatives:
    created_creative_ids.append(creative['id'])
    logger.info(u'Created creative "{id}" with name "{name}".'.format(name=creative['name'], id=creative['id']))
  return created_creative_ids

def create_creative_config(hb_biddercode, name, advertiser_id):
  """
  Creates a creative config object.

  Args:
    hb_biddercode (str): the bidder code, e.g.: 'hb_bidder' or 'hb_adid_appnexus'
    name (str): the name of the creative
    advertiser_id (int): the ID of the advertiser in DFP
  Returns:
    an object: the line item config
  """

  templateLoader = FileSystemLoader(searchpath="./template")
  templateEnv = Environment(loader=templateLoader)
  TEMPLATE_FILE = 'creative_snippet.html'
  template = templateEnv.get_template(TEMPLATE_FILE)
  snippet = template.render(hb_biddercode=hb_biddercode)

  # https://developers.google.com/doubleclick-publishers/docs/reference/v201802/CreativeService.Creative
  config = {
    'xsi_type': 'ThirdPartyCreative',
    'name': name,
    'advertiserId': advertiser_id,
    'size': {
      'width': '1',
      'height': '1'
    },
    'snippet': snippet,
    # https://github.com/prebid/Prebid.js/issues/418
    'isSafeFrameCompatible': False,
  }

  return config

def build_creative_name(bidder_code, order_name, creative_num):
    """
    Returns a name for a creative.

    Args:
      bidder_code (str): the bidder code for the header bidding partner
      order_name (int): the name of the order in DFP
      creative_num (int): the num_creatives distinguising this creative from any
        duplicates
    Returns:
      a string
    """
    return '{bidder_code}: HB {order_name}, #{num}'.format(
        bidder_code=bidder_code, order_name=order_name, num=creative_num)

def create_duplicate_creative_configs(hb_biddercode, bidder_code, order_name, advertiser_id, num_creatives=1):
  """
  Returns an array of creative config object.

  Args:
    bidder_code (str): the bidder code for the header bidding partner
    order_name (int): the name of the order in DFP
    advertiser_id (int): the ID of the advertiser in DFP
    num_creatives (int): how many creative configs to generate
  Returns:
    an array: an array of length `num_creatives`, each item a line item config
  """
  creative_configs = []
  for creative_num in range(1, num_creatives + 1):
    config = create_creative_config(
      hb_biddercode=hb_biddercode,
      name=build_creative_name(bidder_code, order_name, creative_num),
      advertiser_id=advertiser_id,
    )
    creative_configs.append(config)
  return creative_configs

