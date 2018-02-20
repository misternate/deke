Deke 🏒
=======

A convenient HockeyApp API package making it easier than ever to manage
apps, gather specific app statistics, and download builds. Use with in
your automated tests, dashboards, or whatever the heck you desire!

Installation
------------

.. code-block:: bash

    1. git clone https://github.com/misternate/deke.git
    2. cd deke
    3. pip install -r requirements.txt

Visit https://support.hockeyapp.net/kb/api/api-apps to gather your app
credentials.

Usage
-----

The project includes a ``demo.py`` file to get started. Open ``demo.py``
and update ``app_token`` and ``app_identifier`` with the values
associated with your applications.

.. code-block:: python

    apps = deke.Apps('app_token')
    available_apps = apps.list_apps()

    app = deke.App(app_token, app_identifier)
    versions = app.list_versions()
    crash_groups = app.crash_groups('last_crash_at')

    ...

For a detailed listing of all the endpoints and parameters available to
you, and to information on gather your application token, visit
https://support.hockeyapp.net/kb/api/api-apps.

Improvements
------------

Apps
~~~~

-  Create new apps (.ipa, .apk, .zip)
-  Update app data and settings
-  Delete apps and select versions

Crashes
~~~~~~~

-  Create custom crashes
-  Set the status of a crash group
-  Add, update, and delete crash group annotations
-  Plot a histogram of crashes between specific dates

Distribution
~~~~~~~~~~~~

-  Create distribution groups
-  Add and remove users from distribution groups
-  Invite and remove distribution groups and users from apps

Miscellaneous
~~~~~~~~~~~~

-  CLI
-  Persist user/app configs for quicker access to what you need
-  Cleanup all the things!
-  Tests

Author
------

Nate Edwards ([@misternate](https://twitter.com/misternate))