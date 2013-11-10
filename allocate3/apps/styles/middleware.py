

class StylesMiddleware(object):
    '''Store the view on the request for later'''
    def process_view(self, request, view, args, kwargs):
        setattr(request, 'view', view)
        return None