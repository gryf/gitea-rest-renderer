#!/usr/bin/env python3
import sys

from docutils import core
from docutils.writers import html5_polyglot


def main():
    if not sys.stdin.isatty():
        text = sys.stdin.readlines()
    else:
        if len(sys.argv) != 2:
            print("There is no piped reSt source nor provided file, abort.")
            sys.exit(4)
        with open(sys.argv[1]) as fobj:
            text = fobj.read()

    parts = core.publish_parts(writer=html5_polyglot.Writer(),
                               source=''.join(text))

    print(parts.get('body', ''))


if __name__ == '__main__':
    main()
