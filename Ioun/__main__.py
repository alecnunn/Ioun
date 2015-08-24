__author__ = 'Alec Nunn'

import pages
import common
import database

from bottle import Bottle, route, run, template, request, post, get, redirect, response, error
import mistune

app = Bottle()


@app.route('/')
def index():
    return template(pages.default, page_title="Ioun", page_subtitle="A Simple Wiki Platform", pages=database.get_pages(), content=pages.index_content, css=pages.css)


@app.route('/wiki/<title:path>')
def render_page(title):
    page = database.get_page(title)
    if page:
        return template(pages.default, page_title=page[0].replace('_', ' '), page_subtitle=page[1], pages=database.get_pages(), content=mistune.markdown(page[2]), css=pages.css)
    return template(pages.default, page_title=title.replace('_', ' '), page_subtitle="Unknown page.  Would you like to create it?", pages=database.get_pages(), content=pages.unknown_block.format(title), css=pages.css)


@app.get('/edit/<title:path>')
def edit_page(title):
    page = database.get_page(title)
    if page:
        return template(pages.edit, page_title=page[0].replace('_', ' '), page_subtitle=page[1], checked=page[3], body=page[2], pages=database.get_pages(), css=pages.css)
    database.create_page(title)
    return template(pages.edit, page_title=title.replace('_', ' '), page_subtitle="", checked=1, pages=database.get_pages(), css=pages.css, body="")


@app.post('/edit/<title:path>')
def save_page(title):
    visible = 1 if request.forms.get('visible') == 'on' else 0
    msg = (request.forms.get('title'), request.forms.get('subtitle'), request.forms.get('content'), visible)
    database.save_page(msg)
    return redirect('/wiki/{0}'.format(title))


@app.route('/delete/<title>')
def delete_page(title):
    database.delete_page(title)
    return redirect('/')


@app.route('/sitemap.xml')
def sitemap():
    res = database.query('select title from pages')
    response.content_type = 'application/xml'
    return template(pages.sitemap, results=res)


@app.route('/api/all')
def testAPI():
    from json import dumps
    response.content_type = 'application/json'
    return dumps([{"ip": "192.168.1.1", "status": "up"}, {"ip": "127.0.0.1", "status": "up"}, {"ip": "192.168.1.254", "status": "down"}])


@app.route('/api/test')
def testAPI():
    h = """
<html>
<head>
<script src="https://ajax.googleapis.com/ajax/libs/jquery/2.1.3/jquery.min.js"></script>
</head>
<body>
<script>
function execute() {
    $.ajax({
        type: 'GET',
        url: '/api/all',
        dataType: 'json',
    })
    .done(function(result) {
        console.log(result);
        for(var i in result) {
            $('body').append(result[i]['ip'] + ' -> ' + result[i]['status'] + '<br />');
        }
    });
    setTimeout(execute, 5000);
}

$(document).ready(function() {
    setTimeout(execute, 5000);
});
</script>
</body>
</html>
    """
    return h

if __name__ == "__main__":
    import sys
    import os
    if len(sys.argv) > 1:
        if sys.argv[1] == '-v' or sys.argv[1] == '--version':
            print("Ioun v{0}".format(common.__version__))
            sys.exit()
        elif sys.argv[1] == '-h' or sys.argv[1] == '--help':
            print(common.help_txt)
            sys.exit()
        elif sys.argv[1] == '-i' or sys.argv[1] == '--init':
            print("[+] Database Initialized")
            database.init_db()
            sys.exit()
        else:
            print("Unknown option.  Use '-h' to display the available options.")
            sys.exit()
    else:
        if not os.path.isfile('ioun.db'):
            print("You must initialize the database first!")
            sys.exit()
        print("Ioun is running on: http://0.0.0.0:8080")
        run(app, host='0.0.0.0', port=8080, quiet=False)