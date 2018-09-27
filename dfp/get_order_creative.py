from googleads import dfp
from dfp.client import get_client


def execute(order_id):
    return []
    dfp_client = get_client()

    creative_service = dfp_client.GetService('CreativeService', version='v201802')

    # query = "WHERE isMissingCreatives = :isMissingCreatives AND orderId = :orderId"
    query = "WHERE orderId = :orderId"

    values = [
        # {
        #     'key': 'status',
        #     'value': {
        #         'xsi_type': 'TextValue',
        #         'value': 'INACTIVE'
        #     }
        # },
        # {
        #     'key': 'isMissingCreatives',
        #     'value': {
        #         'xsi_type': 'BooleanValue',
        #         'value': True
        #     }
        # },
        {
            'key': 'orderId',
            'value': {
                'xsi_type': 'NumberValue',
                'value': int(order_id)
            }
        }
    ]

    statement = dfp.FilterStatement(query, values)

    response = creative_service.getCreativesByStatement(statement.ToStatement())

    return response
