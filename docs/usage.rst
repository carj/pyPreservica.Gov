
Usage
------------


Once installed you can run pyPreservica.Gov directly from the command line

.. code-block:: console

        $ python -m  pyPreservicaGov

The first time the module is run, it will create a credentials.properties file in the local directory and then exit

Edit the credentials.properties, the first section should contain your Preservica username, password and hostname of
the Preservica system you would like to connect to.

The second section contains the security tag which should be assigned to the records as they are ingested. For example
records which can be published immediately on the Preservica access portal should be set to "public".

The site_name parameter should point to the URL of the Modern.Gov system you would like to harvest.

parent.folder should be the UUID of the Preservica collection the Committee folders will be ingested into.

The committee.FromDate and committee.ToDate parameters specify the date range of meetings which will be harvested.

.. code-block:: console

    [credentials]
    username=test@test.com
    password=1234567
    server=uk.preservica.com

    [Modern.Gov]
    security.tag=open
    site_name=https://democracy.local_authority.gov.uk/
    parent.folder=372d2881-7cce-4c2e-99f7-386c3cf4a922
    committee.FromDate=01/01/1980
    committee.ToDate=01/01/2024


Once the credentials.properties has been updated you can run pyPreservica.Gov again directly from the command line
to start the harvest process.

.. code-block:: console

    $ python -m  pyPreservicaGov

