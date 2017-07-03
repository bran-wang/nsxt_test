import requests


class RESTClient(object):
    _VERB_RESTP_CODES = {
        'get': [requests.codes.ok],
        'post': [requests.codes.created, requests.codes.ok],
    }

    _DEFAULT_HEADERS = {'Accept': 'application/json',
                        'Content-Type': 'application/json'}

    def __init__(self, nsxt_uri, nsxt_user, nsxt_password, insecure, ca_file, default_headers=_DEFAULT_HEADERS):
        session = requests.Session()
        session.auth = (nsxt_user, nsxt_password)
        session.max_redirects = 0
        session.verify = not insecure
        if session.verify and ca_file:
            session.verify = ca_file

        self._conn = session
        if nsxt_uri.startswith('https://'):
            self._url_prefix = "%s/api/v1/" % nsxt_uri
        else:
            self._url_prefix = "https://%s/api/v1/" % nsxt_uri

        self._default_headers = default_headers

    def url_post(self, url, body):
        return self._rest_call(url, method='POST', body=body)

    def url_get(self, url):
        return self._rest_call(url, method='GET')

    def _rest_call(self, url, method='GET', body=None):
        if body is not None:
            body = json.dumps(body)
        request_headers = {}
        request_headers.update(self._default_headers)
        request_url = self._build_url(url)

        do_request = getattr(self._conn, method.lower())

        print "request_url = %s" % request_url
        
        result = do_request(request_url, data=body, headers=request_headers)

        print "result = %s" % result

        self._validate_result(result, RESTClient._VERB_RESTP_CODES[method.lower()], ("%(verb)s %(url)s") % {'verb': method, 'url': request_url})
        return result.json() if result.content else result

    def _build_url(self, uri):
        return self._url_prefix + uri

    def _validate_result(self, result, expected, operation):
        if result.status_code not in expected:
            result_msg = result.json() if result.content else ''
            if type(result_msg) is dict:
                result_msg = result_msg.get('error_message', result_msg)
            raise Exception('Requested operation %s \nUnexpected response %s received with msg %s' % (operation, result.status_code, result_msg))


