import argparse
from pathlib import Path


def cli_parser():
    parser = argparse.ArgumentParser(description='Task 1')
    parser.add_argument('-f', '--format', type=str,
                        help="Dump format")
    parser.add_argument('-fp', '--file', type=Path,
                        help="File for loading data")
    console_args = parser.parse_args()
    format, file = console_args.format, console_args.file
    return format, file
