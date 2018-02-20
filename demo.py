import deke

app_token = ''
app_identifier = ''

'''
A little demo to get you off the ground. All that's required
is a token for apps and a token and identifier for app-specific
features.
'''

apps = deke.Apps(app_token)
available_apps = apps.list_apps()

app = deke.App(app_token, app_identifier)
versions = app.list_versions()
crash_histogram = app.crashes_histogram('2018-01-01', '2018-01-31')
crash_groups = app.crash_groups('last_crash_at')
