sentry-pagerduty
=============

A plugin for sentry that enables sending events on to a pagerduty instance.

Install
-------

Install the package with ``pip``::

    pip install git+git://github.com/depop/sentry-pagerduty.git


Configuration
-------------

Go to your project's configuration page (Projects -> [Project]) and click on "Manage Plugins".
Switch on Pagerduty by ticking "Enabled" in the appropriate column. Click "Save Changes". 
Then select the "Pagerduty" tab and enter the pagerduty api-key, your sentry service-key and the domain name of your pagerduty instance.
