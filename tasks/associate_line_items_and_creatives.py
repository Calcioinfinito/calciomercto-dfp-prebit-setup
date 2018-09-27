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

    # prebid_adform2
    creative_ids = [
        138245498992,
        138245295752,
        138245295758,
        138245295764,
        138245295767,
        138245303532,
        138245499004,
        138245303541,
        138245303544,
        138245499007,
        138245303547,
        138245498671,
        138245499010,
    ]

    # prebid_adform3
    # creative_ids = [
    #     138228214631,
    #     138228214634,
    #     138228169848,
    #     138228169854,
    #     138228169857,
    #     138228169860,
    #     138228169866,
    #     138228169869,
    #     138228169872,
    #     138228169875,
    #     138228297931,
    #     138228297937,
    #     138228297943,
    # ]

    # prebid_adform4
    # creative_ids = [
    #     138228305182,
    #     138228305185,
    #     138228305191,
    #     138228305194,
    #     138228304972,
    #     138228304978,
    #     138228304981,
    #     138228304984,
    #     138228305197,
    #     138228217736,
    #     138228304993,
    #     138228304999,
    #     138228305209,
    # ]

    # prebid_adform5
    # creative_ids = [
    #     138228183639,
    #     138228183642,
    #     138228183645,
    #     138228183648,
    #     138228313717,
    #     138228313720,
    #     138228313723,
    #     138228313726,
    #     138228313729,
    #     138228313735,
    #     138228313738,
    #     138228313741,
    #     138228313750,
    # ]

    sizes = getattr(settings, 'DFP_PLACEMENT_SIZES', None)
    if sizes is None:
        print('error: "DFP_PLACEMENT_SIZES" is empty')
    elif len(sizes) < 1:
        print('The setting "DFP_PLACEMENT_SIZES" must contain at least one size object.')

    dfp.associate_line_items_and_creatives.make_licas(line_item_ids, creative_ids, size_overrides=sizes)
