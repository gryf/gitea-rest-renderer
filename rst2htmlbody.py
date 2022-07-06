#!/usr/bin/env python3
import sys

from docutils import core
from docutils.writers import html5_polyglot


# add class "chroma" to the code block, to get the syntax highlighting
class CustomHTMLTranslator(html5_polyglot.HTMLTranslator):
    def visit_literal_block(self, node):
        self.body.append(self.starttag(node, 'pre', '', CLASS='literal-block'))
        if 'code' in node.get('classes', []):
            self.body.append('<code class="chroma">')


class CustomWriter(html5_polyglot.Writer):
    def __init__(self):
        super().__init__()
        self.translator_class = CustomHTMLTranslator


def main():
    if not sys.stdin.isatty():
        text = sys.stdin.readlines()
    else:
        if len(sys.argv) != 2:
            print("There is no piped reSt source nor provided file, abort.")
            sys.exit(4)
        with open(sys.argv[1]) as fobj:
            text = fobj.read()

    try:
        import pygments
        settings = {'syntax_highlight': 'short'}
    except ImportError:
        settings = {'syntax_highlight': 'none'}

    parts = core.publish_parts(writer=CustomWriter(),
                               source=''.join(text),
                               settings_overrides=settings)

    print(parts.get('body', ''))


if __name__ == '__main__':
    main()
