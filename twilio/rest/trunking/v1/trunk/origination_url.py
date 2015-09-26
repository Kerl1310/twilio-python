# coding=utf-8
"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /       
"""

from twilio import values
from twilio.rest import deserialize
from twilio.rest.base import InstanceContext
from twilio.rest.base import InstanceResource
from twilio.rest.base import ListResource


class OriginationUrlList(ListResource):

    def __init__(self, version, trunk_sid):
        """
        Initialize the OriginationUrlList
        
        :param Version version: Version that contains the resource
        :param trunk_sid: Contextual trunk_sid
        
        :returns: OriginationUrlList
        :rtype: OriginationUrlList
        """
        super(OriginationUrlList, self).__init__(version)
        
        # Path Solution
        self._kwargs = {
            'trunk_sid': trunk_sid,
        }
        self._uri = '/Trunks/{trunk_sid}/OriginationUrls'.format(**self._kwargs)

    def create(self, weight, priority, enabled, friendly_name, sip_url):
        data = values.of({
            'Weight': weight,
            'Priority': priority,
            'Enabled': enabled,
            'FriendlyName': friendly_name,
            'SipUrl': sip_url,
        })
        
        return self._version.create(
            OriginationUrlInstance,
            self._kwargs,
            'POST',
            self._uri,
            data=data,
        )

    def read(self, limit=None, page_size=None, **kwargs):
        limits = self._version.read_limits(limit, page_size)
        
        params = values.of({
            'PageSize': limits['page_size'],
        })
        params.update(kwargs)
        
        return self._version.read(
            self,
            OriginationUrlInstance,
            self._kwargs,
            'GET',
            self._uri,
            limits['limit'],
            limits['page_limit'],
            params=params,
        )

    def page(self, page_token=None, page_number=None, page_size=None, **kwargs):
        params = values.of({
            'PageToken': page_token,
            'Page': page_number,
            'PageSize': page_size,
        })
        params.update(kwargs)
        
        return self._version.page(
            self,
            OriginationUrlInstance,
            self._kwargs,
            'GET',
            self._uri,
            params=params,
        )

    def __call__(self, sid):
        """
        Constructs a OriginationUrlContext
        
        :param sid: Contextual sid
        
        :returns: OriginationUrlContext
        :rtype: OriginationUrlContext
        """
        return OriginationUrlContext(self._version, sid=sid, **self._kwargs)

    def __repr__(self):
        """
        Provide a friendly representation
        
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Trunking.V1.OriginationUrlList>'


class OriginationUrlContext(InstanceContext):

    def __init__(self, version, trunk_sid, sid):
        """
        Initialize the OriginationUrlContext
        
        :param Version version
        :param sid: Contextual sid
        :param trunk_sid: Contextual trunk_sid
        
        :returns: OriginationUrlContext
        :rtype: OriginationUrlContext
        """
        super(OriginationUrlContext, self).__init__(version)
        
        # Path Solution
        self._kwargs = {
            'trunk_sid': trunk_sid,
            'sid': sid,
        }
        self._uri = '/Trunks/{trunk_sid}/OriginationUrls/{sid}'.format(**self._kwargs)

    def fetch(self):
        params = values.of({})
        
        return self._version.fetch(
            OriginationUrlInstance,
            self._kwargs,
            'GET',
            self._uri,
            params=params,
        )

    def delete(self):
        return self._version.delete('delete', self._uri)

    def update(self, weight=values.unset, priority=values.unset,
               enabled=values.unset, friendly_name=values.unset,
               sip_url=values.unset):
        data = values.of({
            'Weight': weight,
            'Priority': priority,
            'Enabled': enabled,
            'FriendlyName': friendly_name,
            'SipUrl': sip_url,
        })
        
        return self._version.update(
            OriginationUrlInstance,
            self._kwargs,
            'POST',
            self._uri,
            data=data,
        )

    def __repr__(self):
        """
        Provide a friendly representation
        
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._kwargs.items())
        return '<Twilio.Trunking.V1.OriginationUrlContext {}>'.format(context)


class OriginationUrlInstance(InstanceResource):

    def __init__(self, version, payload, trunk_sid, sid=None):
        """
        Initialize the OriginationUrlInstance
        
        :returns: OriginationUrlInstance
        :rtype: OriginationUrlInstance
        """
        super(OriginationUrlInstance, self).__init__(version)
        
        # Marshaled Properties
        self._properties = {
            'account_sid': payload['account_sid'],
            'sid': payload['sid'],
            'trunk_sid': payload['trunk_sid'],
            'weight': payload['weight'],
            'enabled': payload['enabled'],
            'sip_url': payload['sip_url'],
            'friendly_name': payload['friendly_name'],
            'priority': payload['priority'],
            'date_created': deserialize.iso8601_datetime(payload['date_created']),
            'date_updated': deserialize.iso8601_datetime(payload['date_updated']),
            'url': payload['url'],
        }
        
        # Context
        self._instance_context = None
        self._kwargs = {
            'trunk_sid': trunk_sid,
            'sid': sid or self._properties['sid'],
        }

    @property
    def _context(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions.  All instance actions are proxied to the context
        
        :returns: OriginationUrlContext for this OriginationUrlInstance
        :rtype: OriginationUrlContext
        """
        if self._instance_context is None:
            self._instance_context = OriginationUrlContext(
                self._version,
                self._kwargs['trunk_sid'],
                self._kwargs['sid'],
            )
        return self._instance_context

    @property
    def account_sid(self):
        """
        :returns: The account_sid
        :rtype: str
        """
        return self._properties['account_sid']

    @property
    def sid(self):
        """
        :returns: The sid
        :rtype: str
        """
        return self._properties['sid']

    @property
    def trunk_sid(self):
        """
        :returns: The trunk_sid
        :rtype: str
        """
        return self._properties['trunk_sid']

    @property
    def weight(self):
        """
        :returns: The weight
        :rtype: str
        """
        return self._properties['weight']

    @property
    def enabled(self):
        """
        :returns: The enabled
        :rtype: bool
        """
        return self._properties['enabled']

    @property
    def sip_url(self):
        """
        :returns: The sip_url
        :rtype: str
        """
        return self._properties['sip_url']

    @property
    def friendly_name(self):
        """
        :returns: The friendly_name
        :rtype: str
        """
        return self._properties['friendly_name']

    @property
    def priority(self):
        """
        :returns: The priority
        :rtype: str
        """
        return self._properties['priority']

    @property
    def date_created(self):
        """
        :returns: The date_created
        :rtype: datetime
        """
        return self._properties['date_created']

    @property
    def date_updated(self):
        """
        :returns: The date_updated
        :rtype: datetime
        """
        return self._properties['date_updated']

    @property
    def url(self):
        """
        :returns: The url
        :rtype: str
        """
        return self._properties['url']

    def fetch(self):
        self._context.fetch()

    def delete(self):
        self._context.delete()

    def update(self, weight=values.unset, priority=values.unset,
               enabled=values.unset, friendly_name=values.unset,
               sip_url=values.unset):
        self._context.update(
            weight=weight,
            priority=priority,
            enabled=enabled,
            friendly_name=friendly_name,
            sip_url=sip_url,
        )

    def __repr__(self):
        """
        Provide a friendly representation
        
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._kwargs.items())
        return '<Twilio.Trunking.V1.OriginationUrlInstance {}>'.format(context)