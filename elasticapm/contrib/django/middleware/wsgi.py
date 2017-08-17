"""
elasticapm.contrib.django.middleware.wsgi
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:copyright: (c) 2011-2012 Opbeat

Large portions are
:copyright: (c) 2010 by the Sentry Team, see AUTHORS for more details.
:license: BSD, see LICENSE for more details.
"""

from elasticapm.middleware import ElasticAPM as ElasticAPMBase


class ElasticAPM(ElasticAPMBase):
    """
    Identical to the default WSGI middleware except that
    the client comes dynamically via ``get_client

    >>> from elasticapm.contrib.django.middleware.wsgi import ElasticAPM
    >>> application = ElasticAPM(application)
    """
    def __init__(self, application):
        self.application = application

    @property
    def client(self):
        from elasticapm.contrib.django.models import client
        return client
