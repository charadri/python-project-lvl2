# -*- coding:utf-8 -*-

"""Something."""

import argparse


def main():
    """Parse at least."""
    parser = argparse.ArgumentParser(
        prog='gendiff',
    )
    parser.add_argument('first_file')
    parser.add_argument('second_file')


if __name__ == 'main':
    main()
