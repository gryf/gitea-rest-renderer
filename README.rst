Restructured text renderer for Gitea
====================================

This is simple custom rst2html5 renderer for `Gitea`_ for reStructuredText
files.


Installation
------------

Before starting deployment of Gitea using docker or docker-compose, you'll need
to create an altered image which would contain `docutils`_ and `pygments`_
python packages. There is a simple Dockerfile attached, which can be adjusted
to your needs (i.e. it might be needed to pin to stable version of gitea), than
let's assume, that we tag the image with ``:rst``:

.. code:: shell

   $ docker build -t gitea:rst -f Dockerfile .

Procedure of running dockerized deployment is `same as documented`_ - of course
you'll need to change line with image to align newly created altered image.


Now, as you have it up and running, there is still a need for altering
configuration. Stop the container, and alter file
``path-to/gitea/conf/app.ini``, and add external renderer section:

.. code:: ini

   [markup.restructuredtext]
   ENABLED = true
   FILE_EXTENSIONS = .rst
   RENDER_COMMAND = "rst2htmlbody"
   IS_INPUT_FILE = false

(see also section below)

And that's it! You can run your gitea instance again and enjoy html generated
preview for reStructuredText.

Unfortunately, you'll need to repeat those steps every time you'd like to
update gitea.


Syntax highlighting
-------------------

Gitea already have syntax highlighting support for markdown files, which uses
`chroma`_ library which, as description says is heavily based on `pygments`_,
which is pretty convenient, since it shares most of the mechanisms and ideas,
including naming convention for the language elements inside ``code`` block. In
other words, it seem to be super easy to adopt this little program to include
also syntax highlighting, instead of generating (i.e. by using ``pygmentize``
commandline tool) and adding separate CSS file as another step.

The only thing which is needed to include is the ``class`` attribute for HTML
element for ``code`` tag. To achieve that it's just a matter of additional
entry in ``app.ini``, and that can be done together with altering ``app.ini``
from previous section:

.. code:: ini

   [markup.sanitizer.restructuredtext.1]
   ELEMENT = code
   ALLOW_ATTR = class

And that should be enough for having colored syntax highlighting.


Testing
-------

You don't need to run docker-compose for running container based on the image,
for testing purposes you could just run:

.. code:: shell

   $ docker build -t gitea:rst -f Dockerfile .
   $ docker run --name gitea-test -p 3000:3000 -p 3022:22 -v ${PWD}/data:/data gitea:rst

Adjust the settings in a browser, wait for them to propagate, than ``ctrl-c``
to stop container, change the ``app.ini`` and start it again with:

.. code:: shell

   $ docker start gitea-test


License
-------

This project is licensed under the MIT License. See the LICENSE file for the
full license text.


.. _docutils: https://docutils.sourceforge.io
.. _gitea: https://gitea.io
.. _same as documented: https://docs.gitea.io/en-us/install-with-docker/
.. _chroma: https://github.com/alecthomas/chroma
.. _pygments: http://pygments.org
