import deke.api as api


class Apps():
    def __init__(self, token):
        self.token = token

    def list_apps(self):
        request_fragments = ['apps']
        apps = api.Request(self.token)
        response = apps._get(request_fragments)

        return response

    def new(self, title, bundle_identifier, platform="iOS"):
        request_fragments = ['apps', 'new']
        app = api.Request(self.token)
        response = app._post(
            request_fragments,
            {
                'title': title, 
                'bundle_identifier': bundle_identifier,
                'platform': platform
            }
        )

        return response

    def delete(self, app_id, app_version=None, version_id=None):
        request_fragments = ['apps', app_id, app_version, version_id]
        app = api.Request(self.token)
        response = app._delete(request_fragments)


class App():
    def __init__(self, token, identifier=None):
        self.token = token
        self.identifier = identifier

        if identifier is None:
            raise ValueError('No identifier provided.')
        else:
            self.identifier = identifier

    def crash_groups(self, sort_by=None):
        request_fragments = ['apps', self.identifier, 'crash_reasons']
        app = api.Request(self.token, self.identifier)
        response = app._get(request_fragments, {'sort': sort_by})

        return response

    def crashes_histogram(self, start_date, end_date):
        request_fragments = ['apps', self.identifier, 'crashes', 'histogram']
        app = api.Request(self.token, self.identifier)
        response = app._get(request_fragments, {'start_date': start_date, 'end_date': end_date})

        return response

    def download(self, latest=True):
        request_fragments = ['apps', self.identifier, 'app_versions']
        app = api.Request(self.token, self.identifier, True)
        app._download_build(request_fragments)

    def list_versions(self):
        if self.identifier is None:
            raise ValueError('No identifier provided.')
        else:
            request_fragments = ['apps', self.identifier, 'app_versions']
            app = api.Request(self.token, self.identifier)
            response = app._get(request_fragments)

            return response

    def new(self):
        request_fragments = ['apps', self.identifier, 'new']
        app = api.Request(self.token, self.identifier)
        response = app._post(
            request_fragments,
            {
                'bundle_short_version': title, 
                'bundle_identifier': bundle_identifier,
                'platform': platform
            }
        )

    def statistics(self):
        request_fragments = ['apps', self.identifier, 'statistics']
        app = api.Request(self.token, self.identifier)
        response = app._get(request_fragments)

        return response
