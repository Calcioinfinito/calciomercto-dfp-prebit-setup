from googleads import dfp
from dfp.client import get_client


def approve(order_id):
    dfp_client = get_client()

    order_service = dfp_client.GetService('OrderService', version='v201802')

    query = "WHERE orderId = (%s)" % int(order_id)
    statement = dfp.FilterStatement(query)

    result = order_service.performOrderAction({'xsi_type': 'ApproveOrders'}, statement.ToStatement())
    if result and int(result['numChanges']) > 0:
        print('Order %s approved.' % order_id)
    else:
        print('Order %s not approved.' % order_id)
