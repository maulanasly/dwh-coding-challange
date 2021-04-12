import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Process the warehouse data')
    parser.add_argument('-m', '--mode', type=str, help='execution mode')

    args = parser.parse_args()
    if args.mode == 'tabular-data':
        pass
    elif args.mode == 'historical-data':
        pass
    elif args.mode == 'summary':
        pass
    else:
        pass
