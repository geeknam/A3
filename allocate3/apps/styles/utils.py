
from styles.settings import VIEW_STYLES_MAP

IGNORE_APPS = [
    'grappelli',
    'django',
]

def get_view_labels(view):
    '''Return app_label, view_name for the view'''
    try:
        view_name = view.__name__
    except AttributeError:
        return None, None
    app_label = view.__module__

    if any(map(app_label.startswith, IGNORE_APPS)):
        return None, None

    config = VIEW_STYLES_MAP.get(view_name, None)
    if config is not None:
        view_name = config['view_class']
        app_label = config['app_class']

    elif app_label.endswith('.views'):
        app_label = app_label[:-6]

    app_label = app_label.replace('.', '_')

    return app_label, view_name

def create_classes_from_request(request):
    """
    Creates app_class and view_class names for the views we care about, i.e.
    the ones that display content on the front-end.

    Store those class names in the request.session for use when retrieving stylesheets
    particular to the app or view.
    """
    view = getattr(request, 'view', None)

    return get_view_labels(view)

