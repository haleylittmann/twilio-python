# coding=utf-8
"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /       
"""

from twilio import deserialize
from twilio import serialize
from twilio import values
from twilio.instance_context import InstanceContext
from twilio.instance_resource import InstanceResource
from twilio.list_resource import ListResource
from twilio.page import Page


class MediaList(ListResource):

    def __init__(self, version, account_sid, message_sid):
        """
        Initialize the MediaList
        
        :param Version version: Version that contains the resource
        :param account_sid: The unique sid that identifies this account
        :param message_sid: A string that uniquely identifies this message
        
        :returns: MediaList
        :rtype: MediaList
        """
        super(MediaList, self).__init__(version)
        
        # Path Solution
        self._solution = {
            'account_sid': account_sid,
            'message_sid': message_sid,
        }
        self._uri = '/Accounts/{account_sid}/Messages/{message_sid}/Media.json'.format(**self._solution)

    def stream(self, date_created_before=values.unset, date_created=values.unset,
               date_created_after=values.unset, limit=None, page_size=None):
        """
        Streams MediaInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.
        
        :param date date_created_before: Filter by date created
        :param date date_created: Filter by date created
        :param date date_created_after: Filter by date created
        :param int limit: Upper limit for the number of records to return. stream()
                          guarantees to never return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, stream() will attempt to read the
                              limit with the most efficient page size, i.e. min(limit, 1000)
        
        :returns: Generator that will yield up to limit results
        :rtype: generator
        """
        limits = self._version.read_limits(limit, page_size)
        
        page = self.page(
            date_created_before=date_created_before,
            date_created=date_created,
            date_created_after=date_created_after,
            page_size=limits['page_size'],
        )
        
        return self._version.stream(page, limits['limit'], limits['page_limit'])

    def read(self, date_created_before=values.unset, date_created=values.unset,
             date_created_after=values.unset, limit=None, page_size=values.unset):
        """
        Reads MediaInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.
        
        :param date date_created_before: Filter by date created
        :param date date_created: Filter by date created
        :param date date_created_after: Filter by date created
        :param int limit: Upper limit for the number of records to return. read() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, read() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)
        
        :returns: Generator that will yield up to limit results
        :rtype: generator
        """
        return list(self.stream(
            date_created_before=date_created_before,
            date_created=date_created,
            date_created_after=date_created_after,
            limit=limit,
            page_size=page_size,
        ))

    def page(self, date_created_before=values.unset, date_created=values.unset,
             date_created_after=values.unset, page_token=values.unset,
             page_number=values.unset, page_size=values.unset):
        """
        Retrieve a single page of MediaInstance records from the API.
        Request is executed immediately
        
        :param date date_created_before: Filter by date created
        :param date date_created: Filter by date created
        :param date date_created_after: Filter by date created
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50
        
        :returns: Page of MediaInstance
        :rtype: Page
        """
        params = values.of({
            'DateCreated<': serialize.iso8601_date(date_created_before),
            'DateCreated': serialize.iso8601_date(date_created),
            'DateCreated>': serialize.iso8601_date(date_created_after),
            'PageToken': page_token,
            'Page': page_number,
            'PageSize': page_size,
        })
        
        response = self._version.page(
            'GET',
            self._uri,
            params=params,
        )
        
        return MediaPage(
            self._version,
            response,
            account_sid=self._solution['account_sid'],
            message_sid=self._solution['message_sid'],
        )

    def get(self, sid):
        """
        Constructs a MediaContext
        
        :param sid: Fetch by unique media Sid
        
        :returns: MediaContext
        :rtype: MediaContext
        """
        return MediaContext(
            self._version,
            account_sid=self._solution['account_sid'],
            message_sid=self._solution['message_sid'],
            sid=sid,
        )

    def __call__(self, sid):
        """
        Constructs a MediaContext
        
        :param sid: Fetch by unique media Sid
        
        :returns: MediaContext
        :rtype: MediaContext
        """
        return MediaContext(
            self._version,
            account_sid=self._solution['account_sid'],
            message_sid=self._solution['message_sid'],
            sid=sid,
        )

    def __repr__(self):
        """
        Provide a friendly representation
        
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V2010.MediaList>'


class MediaPage(Page):

    def __init__(self, version, response, account_sid, message_sid):
        """
        Initialize the MediaPage
        
        :param Version version: Version that contains the resource
        :param Response response: Response from the API
        :param account_sid: The unique sid that identifies this account
        :param message_sid: A string that uniquely identifies this message
        
        :returns: MediaPage
        :rtype: MediaPage
        """
        super(MediaPage, self).__init__(version, response)
        
        # Path Solution
        self._solution = {
            'account_sid': account_sid,
            'message_sid': message_sid,
        }

    def get_instance(self, payload):
        """
        Build an instance of MediaInstance
        
        :param dict payload: Payload response from the API
        
        :returns: MediaInstance
        :rtype: MediaInstance
        """
        return MediaInstance(
            self._version,
            payload,
            account_sid=self._solution['account_sid'],
            message_sid=self._solution['message_sid'],
        )

    def __repr__(self):
        """
        Provide a friendly representation
        
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V2010.MediaPage>'


class MediaContext(InstanceContext):

    def __init__(self, version, account_sid, message_sid, sid):
        """
        Initialize the MediaContext
        
        :param Version version: Version that contains the resource
        :param account_sid: The account_sid
        :param message_sid: The message_sid
        :param sid: Fetch by unique media Sid
        
        :returns: MediaContext
        :rtype: MediaContext
        """
        super(MediaContext, self).__init__(version)
        
        # Path Solution
        self._solution = {
            'account_sid': account_sid,
            'message_sid': message_sid,
            'sid': sid,
        }
        self._uri = '/Accounts/{account_sid}/Messages/{message_sid}/Media/{sid}.json'.format(**self._solution)

    def delete(self):
        """
        Deletes the MediaInstance
        
        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._version.delete('delete', self._uri)

    def fetch(self):
        """
        Fetch a MediaInstance
        
        :returns: Fetched MediaInstance
        :rtype: MediaInstance
        """
        params = values.of({})
        
        payload = self._version.fetch(
            'GET',
            self._uri,
            params=params,
        )
        
        return MediaInstance(
            self._version,
            payload,
            account_sid=self._solution['account_sid'],
            message_sid=self._solution['message_sid'],
            sid=self._solution['sid'],
        )

    def __repr__(self):
        """
        Provide a friendly representation
        
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Api.V2010.MediaContext {}>'.format(context)


class MediaInstance(InstanceResource):

    def __init__(self, version, payload, account_sid, message_sid, sid=None):
        """
        Initialize the MediaInstance
        
        :returns: MediaInstance
        :rtype: MediaInstance
        """
        super(MediaInstance, self).__init__(version)
        
        # Marshaled Properties
        self._properties = {
            'account_sid': payload['account_sid'],
            'content_type': payload['content_type'],
            'date_created': deserialize.rfc2822_datetime(payload['date_created']),
            'date_updated': deserialize.rfc2822_datetime(payload['date_updated']),
            'parent_sid': payload['parent_sid'],
            'sid': payload['sid'],
            'uri': payload['uri'],
        }
        
        # Context
        self._context = None
        self._solution = {
            'account_sid': account_sid,
            'message_sid': message_sid,
            'sid': sid or self._properties['sid'],
        }

    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions.  All instance actions are proxied to the context
        
        :returns: MediaContext for this MediaInstance
        :rtype: MediaContext
        """
        if self._context is None:
            self._context = MediaContext(
                self._version,
                account_sid=self._solution['account_sid'],
                message_sid=self._solution['message_sid'],
                sid=self._solution['sid'],
            )
        return self._context

    @property
    def account_sid(self):
        """
        :returns: The unique sid that identifies this account
        :rtype: unicode
        """
        return self._properties['account_sid']

    @property
    def content_type(self):
        """
        :returns: The default mime-type of the media
        :rtype: unicode
        """
        return self._properties['content_type']

    @property
    def date_created(self):
        """
        :returns: The date this resource was created
        :rtype: datetime
        """
        return self._properties['date_created']

    @property
    def date_updated(self):
        """
        :returns: The date this resource was last updated
        :rtype: datetime
        """
        return self._properties['date_updated']

    @property
    def parent_sid(self):
        """
        :returns: The unique id of the resource that created the media.
        :rtype: unicode
        """
        return self._properties['parent_sid']

    @property
    def sid(self):
        """
        :returns: A string that uniquely identifies this media
        :rtype: unicode
        """
        return self._properties['sid']

    @property
    def uri(self):
        """
        :returns: The URI for this resource
        :rtype: unicode
        """
        return self._properties['uri']

    def delete(self):
        """
        Deletes the MediaInstance
        
        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._proxy.delete()

    def fetch(self):
        """
        Fetch a MediaInstance
        
        :returns: Fetched MediaInstance
        :rtype: MediaInstance
        """
        return self._proxy.fetch()

    def __repr__(self):
        """
        Provide a friendly representation
        
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Api.V2010.MediaInstance {}>'.format(context)
