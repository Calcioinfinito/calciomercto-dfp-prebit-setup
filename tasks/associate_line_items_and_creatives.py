import argparse
import dfp.associate_line_items_and_creatives
import dfp.get_order_creative
import dfp.get_order_line_items
import settings

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Approve DFP order.')
    parser.add_argument('--orderId', action='store', default=None,
                        help='DFP Order Id.')

    args = parser.parse_args()

    order_id = args.orderId

    line_item_ids = dfp.get_order_line_items.execute(order_id)
    # creative_ids = dfp.get_order_creative.execute(order_id)
    creative_ids = [
        138227101311,
        138227101314,
        138227142353,
        138227101317,
        138227101320,
        138227142359,
        138227101323,
        138227101326,
        138227142362,
        138227101329,
        138227101332,
        138227101335,
        138227101338,
    ]

    sizes = getattr(settings, 'DFP_PLACEMENT_SIZES', None)
    if sizes is None:
        print('error: "DFP_PLACEMENT_SIZES" is empty')
    elif len(sizes) < 1:
        print('The setting "DFP_PLACEMENT_SIZES" must contain at least one size object.')

    dfp.associate_line_items_and_creatives.make_licas(line_item_ids, creative_ids, size_overrides=sizes)
