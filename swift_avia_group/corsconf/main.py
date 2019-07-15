CORS_URLS_REGEX=r'^/api/.*$'
CORS_ORIGIN_WHITELIST = (
	'localhost:4200',
	'127.0.0.1'
)
CORS_ORIGIN_ALLOW_ALL=True

from corsheaders.defaults import default_headers

CORS_ALLOW_HEADERS = default_headers + ('X-CSRFToken',)