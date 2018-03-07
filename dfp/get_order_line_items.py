from googleads import dfp
from dfp.client import get_client


def execute(order_id):
    dfp_client = get_client()

    line_item_service = dfp_client.GetService('LineItemService', version='v201702')

    query = "WHERE isMissingCreatives = :isMissingCreatives AND orderId = :orderId"

    values = [
        # {
        #     'key': 'status',
        #     'value': {
        #         'xsi_type': 'TextValue',
        #         'value': 'INACTIVE'
        #     }
        # },
        {
            'key': 'isMissingCreatives',
            'value': {
                'xsi_type': 'BooleanValue',
                'value': True
            }
        },
        {
            'key': 'orderId',
            'value': {
                'xsi_type': 'NumberValue',
                'value': int(order_id)
            }
        }
    ]
    statement = dfp.FilterStatement(query, values)

    response = line_item_service.getLineItemsByStatement(statement.ToStatement())

    line_item_ids = []
    if 'results' in response:
        for line_item in response['results'][:200]:
            line_item_ids.append(line_item['id'])

    return line_item_ids
