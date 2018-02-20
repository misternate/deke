import app

'''
This is the little guy that gets everything started. Use Deke to access
your apps or app data and settings.
'''


class Deke():
    def __init__(self, token, identifier=None):
        if identifier is None:
            app.Apps.__init__(self, token)
        else:
            app.App.__init__(self, token, identifier)
