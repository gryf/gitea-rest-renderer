Restructured text renderer for Gitea
====================================

This is simple custom rst2html5 renderer for `Gitea`_.

Installation
------------

Before starting deployment of Gitea using docker or docker-compose, you'll
need to create an altered image which would contain `docutils`_ python package.
There is a simple Dockerfile attached, which can be adjusted to your needs
(i.e. it might be needed to pin to stable version of gitea), than let's assume,
that we tag the image with ``:rst``:

.. code:: shell

   $ docker build -t gitea:rst -f Dockerfile .

Procedure of running dockerized deployment is `same as documented`_.

Now, as you have it up and running, there is still a need for altering
configuration. Stop the container, and alter file
``path-to/gitea/conf/app.ini``, and add external renderer section:

.. code:: ini

   [markup.restructuredtext]
   ENABLED = true
   FILE_EXTENSIONS = .rst
   RENDER_COMMAND = "rst2htmlbody"
   IS_INPUT_FILE = false


And that's it!

Unfortunately, you'll need to repeat those steps every time you'd like to
update gitea.


.. _docutils: https://docutils.sourceforge.io
.. _gitea: https://gitea.io
.. _same as documented: https://docs.gitea.io/en-us/install-with-docker/
