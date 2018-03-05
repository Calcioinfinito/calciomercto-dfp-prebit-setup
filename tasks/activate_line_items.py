import argparse
import dfp.activate_line_items

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Approve DFP order.')
    parser.add_argument('--orderId', action='store', default=None,
                        help='DFP Order Id.')

    args = parser.parse_args()

    dfp.activate_line_items.activate(args.orderId)
