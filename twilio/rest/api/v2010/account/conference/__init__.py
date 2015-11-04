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
from twilio.rest.api.v2010.account.conference.participant import ParticipantList


class ConferenceList(ListResource):

    def __init__(self, version, account_sid):
        """
        Initialize the ConferenceList
        
        :param Version version: Version that contains the resource
        :param account_sid: The unique sid that identifies this account
        
        :returns: ConferenceList
        :rtype: ConferenceList
        """
        super(ConferenceList, self).__init__(version)
        
        # Path Solution
        self._solution = {
            'account_sid': account_sid,
        }
        self._uri = '/Accounts/{account_sid}/Conferences.json'.format(**self._solution)

    def stream(self, date_created_before=values.unset, date_created=values.unset,
               date_created_after=values.unset, date_updated_before=values.unset,
               date_updated=values.unset, date_updated_after=values.unset,
               friendly_name=values.unset, status=values.unset, limit=None,
               page_size=None):
        """
        Streams ConferenceInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.
        
        :param date date_created_before: Filter by date created
        :param date date_created: Filter by date created
        :param date date_created_after: Filter by date created
        :param date date_updated_before: Filter by date updated
        :param date date_updated: Filter by date updated
        :param date date_updated_after: Filter by date updated
        :param unicode friendly_name: Filter by friendly name
        :param conference.status status: The status of the conference
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
            date_updated_before=date_updated_before,
            date_updated=date_updated,
            date_updated_after=date_updated_after,
            friendly_name=friendly_name,
            status=status,
            page_size=limits['page_size'],
        )
        
        return self._version.stream(page, limits['limit'], limits['page_limit'])

    def read(self, date_created_before=values.unset, date_created=values.unset,
             date_created_after=values.unset, date_updated_before=values.unset,
             date_updated=values.unset, date_updated_after=values.unset,
             friendly_name=values.unset, status=values.unset, limit=None,
             page_size=values.unset):
        """
        Reads ConferenceInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.
        
        :param date date_created_before: Filter by date created
        :param date date_created: Filter by date created
        :param date date_created_after: Filter by date created
        :param date date_updated_before: Filter by date updated
        :param date date_updated: Filter by date updated
        :param date date_updated_after: Filter by date updated
        :param unicode friendly_name: Filter by friendly name
        :param conference.status status: The status of the conference
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
            date_updated_before=date_updated_before,
            date_updated=date_updated,
            date_updated_after=date_updated_after,
            friendly_name=friendly_name,
            status=status,
            limit=limit,
            page_size=page_size,
        ))

    def page(self, date_created_before=values.unset, date_created=values.unset,
             date_created_after=values.unset, date_updated_before=values.unset,
             date_updated=values.unset, date_updated_after=values.unset,
             friendly_name=values.unset, status=values.unset,
             page_token=values.unset, page_number=values.unset,
             page_size=values.unset):
        """
        Retrieve a single page of ConferenceInstance records from the API.
        Request is executed immediately
        
        :param date date_created_before: Filter by date created
        :param date date_created: Filter by date created
        :param date date_created_after: Filter by date created
        :param date date_updated_before: Filter by date updated
        :param date date_updated: Filter by date updated
        :param date date_updated_after: Filter by date updated
        :param unicode friendly_name: Filter by friendly name
        :param conference.status status: The status of the conference
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50
        
        :returns: Page of ConferenceInstance
        :rtype: Page
        """
        params = values.of({
            'DateCreated<': serialize.iso8601_date(date_created_before),
            'DateCreated': serialize.iso8601_date(date_created),
            'DateCreated>': serialize.iso8601_date(date_created_after),
            'DateUpdated<': serialize.iso8601_date(date_updated_before),
            'DateUpdated': serialize.iso8601_date(date_updated),
            'DateUpdated>': serialize.iso8601_date(date_updated_after),
            'FriendlyName': friendly_name,
            'Status': status,
            'PageToken': page_token,
            'Page': page_number,
            'PageSize': page_size,
        })
        
        response = self._version.page(
            'GET',
            self._uri,
            params=params,
        )
        
        return ConferencePage(
            self._version,
            response,
            account_sid=self._solution['account_sid'],
        )

    def get(self, sid):
        """
        Constructs a ConferenceContext
        
        :param sid: Fetch by unique conference Sid
        
        :returns: ConferenceContext
        :rtype: ConferenceContext
        """
        return ConferenceContext(
            self._version,
            account_sid=self._solution['account_sid'],
            sid=sid,
        )

    def __call__(self, sid):
        """
        Constructs a ConferenceContext
        
        :param sid: Fetch by unique conference Sid
        
        :returns: ConferenceContext
        :rtype: ConferenceContext
        """
        return ConferenceContext(
            self._version,
            account_sid=self._solution['account_sid'],
            sid=sid,
        )

    def __repr__(self):
        """
        Provide a friendly representation
        
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V2010.ConferenceList>'


class ConferencePage(Page):

    def __init__(self, version, response, account_sid):
        """
        Initialize the ConferencePage
        
        :param Version version: Version that contains the resource
        :param Response response: Response from the API
        :param account_sid: The unique sid that identifies this account
        
        :returns: ConferencePage
        :rtype: ConferencePage
        """
        super(ConferencePage, self).__init__(version, response)
        
        # Path Solution
        self._solution = {
            'account_sid': account_sid,
        }

    def get_instance(self, payload):
        """
        Build an instance of ConferenceInstance
        
        :param dict payload: Payload response from the API
        
        :returns: ConferenceInstance
        :rtype: ConferenceInstance
        """
        return ConferenceInstance(
            self._version,
            payload,
            account_sid=self._solution['account_sid'],
        )

    def __repr__(self):
        """
        Provide a friendly representation
        
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V2010.ConferencePage>'


class ConferenceContext(InstanceContext):

    def __init__(self, version, account_sid, sid):
        """
        Initialize the ConferenceContext
        
        :param Version version: Version that contains the resource
        :param account_sid: The account_sid
        :param sid: Fetch by unique conference Sid
        
        :returns: ConferenceContext
        :rtype: ConferenceContext
        """
        super(ConferenceContext, self).__init__(version)
        
        # Path Solution
        self._solution = {
            'account_sid': account_sid,
            'sid': sid,
        }
        self._uri = '/Accounts/{account_sid}/Conferences/{sid}.json'.format(**self._solution)
        
        # Dependents
        self._participants = None

    def fetch(self):
        """
        Fetch a ConferenceInstance
        
        :returns: Fetched ConferenceInstance
        :rtype: ConferenceInstance
        """
        params = values.of({})
        
        payload = self._version.fetch(
            'GET',
            self._uri,
            params=params,
        )
        
        return ConferenceInstance(
            self._version,
            payload,
            account_sid=self._solution['account_sid'],
            sid=self._solution['sid'],
        )

    @property
    def participants(self):
        """
        Access the participants
        
        :returns: ParticipantList
        :rtype: ParticipantList
        """
        if self._participants is None:
            self._participants = ParticipantList(
                self._version,
                account_sid=self._solution['account_sid'],
                conference_sid=self._solution['sid'],
            )
        return self._participants

    def __repr__(self):
        """
        Provide a friendly representation
        
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Api.V2010.ConferenceContext {}>'.format(context)


class ConferenceInstance(InstanceResource):

    def __init__(self, version, payload, account_sid, sid=None):
        """
        Initialize the ConferenceInstance
        
        :returns: ConferenceInstance
        :rtype: ConferenceInstance
        """
        super(ConferenceInstance, self).__init__(version)
        
        # Marshaled Properties
        self._properties = {
            'account_sid': payload['account_sid'],
            'date_created': deserialize.rfc2822_datetime(payload['date_created']),
            'date_updated': deserialize.rfc2822_datetime(payload['date_updated']),
            'api_version': payload['api_version'],
            'friendly_name': payload['friendly_name'],
            'sid': payload['sid'],
            'status': payload['status'],
            'uri': payload['uri'],
        }
        
        # Context
        self._context = None
        self._solution = {
            'account_sid': account_sid,
            'sid': sid or self._properties['sid'],
        }

    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions.  All instance actions are proxied to the context
        
        :returns: ConferenceContext for this ConferenceInstance
        :rtype: ConferenceContext
        """
        if self._context is None:
            self._context = ConferenceContext(
                self._version,
                account_sid=self._solution['account_sid'],
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
    def api_version(self):
        """
        :returns: The api_version
        :rtype: unicode
        """
        return self._properties['api_version']

    @property
    def friendly_name(self):
        """
        :returns: A human readable description of this resource
        :rtype: unicode
        """
        return self._properties['friendly_name']

    @property
    def sid(self):
        """
        :returns: A string that uniquely identifies this conference
        :rtype: unicode
        """
        return self._properties['sid']

    @property
    def status(self):
        """
        :returns: The status of the conference
        :rtype: conference.status
        """
        return self._properties['status']

    @property
    def uri(self):
        """
        :returns: The URI for this resource
        :rtype: unicode
        """
        return self._properties['uri']

    def fetch(self):
        """
        Fetch a ConferenceInstance
        
        :returns: Fetched ConferenceInstance
        :rtype: ConferenceInstance
        """
        return self._proxy.fetch()

    @property
    def participants(self):
        """
        Access the participants
        
        :returns: participants
        :rtype: participants
        """
        return self._proxy.participants

    def __repr__(self):
        """
        Provide a friendly representation
        
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Api.V2010.ConferenceInstance {}>'.format(context)
