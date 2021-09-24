from load_html import template

def run(command, **kwargs):
    if command == '':
        return template('template.html')