
from styles.utils import create_classes_from_request


def styles_classes(request):
    """
    Styles Classes Context Processor

    Utilise these context variables to place suitable styling 'hooks'
    into our templates; such that each of our styling contexts can
    be suitably targeted.

    For example:

        <section class="{{ GLOBAL_CLASSNAMES }}">

    Will produce:

        <section class="k3_products_app products_view">

    """

    app_class, view_class = create_classes_from_request(request)

    if request.is_secure():
        ext = 'ssl.css'
    else:
        ext = 'css'

    STYLES = ['css/main.{}'.format(ext),]
    if app_class:
        STYLES.append('css/{}.{}'.format(app_class, ext))
        if view_class:
            STYLES.append('css/{}.{}.{}'.format(app_class, view_class, ext))

    return {
        'STYLES': STYLES,
        'APP_CLASS': app_class,
        'VIEW_CLASS': view_class,
        'GLOBAL_ID': '%s_view' % view_class,
        'GLOBAL_CLASSNAMES': '%s_app %s_view' % (
            app_class,
            view_class
        )
    }

