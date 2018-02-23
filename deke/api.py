from deke.utils import constants

import logging

from tqdm import tqdm
import requests


class Request():

    def __init__(self, token, identifier=None):
        self.header = {'X-HockeyAppToken': token}
        self.token = token
        self.identifier = identifier

    def _constructor_uri(self, uri_fragments):
        if self.identifier is not None:
            return constants.API_URL + '/'.join(uri_fragments)
        else:
            if self.token is not None:
                return constants.API_URL + '/'.join(uri_fragments)

    def _get(self, uri_fragments, params=None):
        path = self._constructor_uri(uri_fragments)

        self.params = params

        try:
            response = requests.get(
                url=path,
                params=params,
                headers=self.header
            )
            return response.json()
        except requests.exceptions.RequestException:
            logging.error('The HTTP Request has failed.')
    
    def _post(self, uri_fragments, params=None):
        path = self._constructor_uri(uri_fragments)

        self.params = params

        try:
            response = requests.post(
                url=path,
                params=params,
                headers=self.header
            )
            return response.json()
        except requests.exceptions.RequestException:
            logging.error('The HTTP Request has failed.')

    def _delete(self, uri_fragments, params=None):
        path = self._constructor_uri(uri_fragments)
        print('PAth: ' + path)

        self.params = params

        try:
            response = requests.delete(
                url=path,
                params=params,
                headers=self.header
            )
        except requests.exceptions.RequestException:
            logging.error('The HTTP Request has failed.')

    def _download_build(self, uri_fragments):
        params = {"include_build_urls": "true"}
        app_versions = self._get(uri_fragments, params)
        latest_version = self._latest_version(app_versions)
        path = self._constructor_uri(uri_fragments)
        download_request = requests.get(latest_version['build_url'], stream=True)
        total_size = int(download_request.headers.get('content-length'))
        # This appears to be the only way to check if iOS or Android. Sorry...
        build_extension = 'ipa' if latest_version['device_family'] else 'apk'
        file_name = 'v{}b{}.{}'.format(
            latest_version['shortversion'],
            latest_version['version'],
            build_extension
        )

        with open(file_name, 'wb') as f:
            for data in tqdm(
                    download_request.iter_content(),
                    total=total_size,
                    unit='B',
                    unit_scale=True
                    ):
                f.write(data)

    def _latest_version(self, versions):
        max_version = 0
        build = {}
        for app in versions['app_versions']:
                if int(app['version']) > max_version:
                    max_version = int(app['version'])
                    build = app
        return build
