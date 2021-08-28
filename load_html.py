def template(directory, **kwargs):

    with open(directory, 'r').read() as html:
        if 'data' in kwargs:
            html = html.format(**kwargs['data'])