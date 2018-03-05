from googleads import dfp
from dfp.client import get_client


def activate(order_id):
    dfp_client = get_client()

    line_item_service = dfp_client.GetService('LineItemService', version='v201702')

    query = "WHERE status = 'INACTIVE' AND orderId = (%s)" % int(order_id)
    statement = dfp.FilterStatement(query)

    line_items_activated = 0

    while True:
        response = line_item_service.getLineItemsByStatement(statement.ToStatement())
        if 'results' in response:
            for line_item in response['results']:
                print('Line item with id "%s", belonging to order id "%s", and '
                      'name "%s" will be activated.' % (line_item['id'], line_item['orderId'], line_item['name']))

            result = line_item_service.performLineItemAction({'xsi_type': 'ActivateLineItems'}, statement.ToStatement())
            if result and int(result['numChanges']) > 0:
                line_items_activated += int(result['numChanges'])
            statement.offset += dfp.SUGGESTED_PAGE_LIMIT
        else:
            break

    if line_items_activated > 0:
        print('Number of line items activated: %s' % line_items_activated)
    else:
        print('No line items were activated.')
