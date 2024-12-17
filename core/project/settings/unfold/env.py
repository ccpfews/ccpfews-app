from core.project.settings import DEBUG, MAINTENANCE_MODE

# set environment callback in template


def environment_callback(request):
    """
    Callback has to return a list of two values representing text value and the color
    type of the label displayed in top right corner.
    """
    state = ''
    if DEBUG:
        if MAINTENANCE_MODE:
            state = 'Development/Maintenance'
        else:
            state = 'Development'
    else:
        if MAINTENANCE_MODE:
            state = 'Production/Maintenance'
        else:
            state = 'Production'

    return [state, 'danger']  # info, danger, warning, success
