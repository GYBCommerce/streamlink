Configuration file
==================

Writing the command-line options every time is inconvenient, that's why Streamlink
is capable of reading options from a configuration file instead.

Location
--------

Streamlink will look for config files in different locations depending on
your platform:

.. rst-class:: table-custom-layout table-custom-layout-platform-locations

================= ====================================================
Platform          Location
================= ====================================================
Linux, BSD        - ``${XDG_CONFIG_HOME:-${HOME}/.config}/streamlink/config``

                  Deprecated:

                  - ``${HOME}/.streamlinkrc``
macOS             - ``${HOME}/Library/Application Support/streamlink/config``

                  Deprecated:

                  - ``${XDG_CONFIG_HOME:-${HOME}/.config}/streamlink/config``
                  - ``${HOME}/.streamlinkrc``
Windows           - ``%APPDATA%\streamlink\config``

                  Deprecated:

                  - ``%APPDATA%\streamlink\streamlinkrc``
================= ====================================================

You can also specify the location yourself using the :option:`--config` option.

.. warning::

  Streamlink's Windows installers automatically create a config file if it doesn't exist yet, but on any
  other platform or installation method, you must create the file yourself.

.. note::

   The ``XDG_CONFIG_HOME`` environment variable is part of the `XDG base directory specification`_ (`Arch Wiki <xdg-base-dir-arch-wiki_>`_).

   The ``${VARIABLENAME:-DEFAULTVALUE}`` syntax is explained `here <Parameter expansion_>`_.

.. _XDG base directory specification: https://specifications.freedesktop.org/basedir-spec/basedir-spec-latest.html
.. _xdg-base-dir-arch-wiki: https://wiki.archlinux.org/title/XDG_Base_Directory
.. _Parameter expansion: https://wiki.bash-hackers.org/syntax/pe


Syntax
------

The config file is a simple text file and should contain one
:ref:`command-line option <cli:Command-line usage>` (omitting the leading dashes) per
line in the format::

  option=value

or for an option without value::

  option

.. warning::

    Any quotes will be used as part of the argument value.

Example
^^^^^^^

.. code-block:: bash

    # Player options
    player=mpv --cache 2048
    player-no-close

.. note::

    Full player paths are supported via configuration file options such as
    ``player=C:\mpv-x86_64\mpv``


Plugin specific configuration file
----------------------------------

You may want to use specific options for some plugins only. This
can be accomplished by placing those settings inside a plugin specific
config file. Options inside these config files will override the main
config file when a URL matching the plugin is used.

Streamlink expects this config to be named like the main config but
with ``.<plugin name>`` attached to the end.

Examples
^^^^^^^^

.. rst-class:: table-custom-layout table-custom-layout-platform-locations

================= ====================================================
Platform          Location
================= ====================================================
Linux, BSD        - ``${XDG_CONFIG_HOME:-${HOME}/.config}/streamlink/config.pluginname``

                  Deprecated:

                  - ``${HOME}/.streamlinkrc.pluginname``
macOS             - ``${HOME}/Library/Application Support/streamlink/config.pluginname``

                  Deprecated:

                  - ``${XDG_CONFIG_HOME:-${HOME}/.config}/streamlink/config.pluginname``
                  - ``${HOME}/.streamlinkrc.pluginname``
Windows           - ``%APPDATA%\streamlink\config.pluginname``

                  Deprecated:

                  - ``%APPDATA%\streamlink\streamlinkrc.pluginname``
================= ====================================================

Have a look at the :ref:`list of plugins <plugins:Plugins>`, or
check the :option:`--plugins` option to see the name of each built-in plugin.
