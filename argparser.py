import argparse


def cli_parser():
    parser = argparse.ArgumentParser(description='Task 1')
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-j', '--json',
                       nargs='+', type=str,
                       help="Dump to json")
    group.add_argument('-x', '--xml',
                       nargs='+', type=str,
                       help="Dump to XML")
    console_args = vars(parser.parse_args())
    format, files = tuple(*{arg: value for arg, value in console_args.items() if value}.items())
    return format, files
