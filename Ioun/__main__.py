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


@app.route('/wiki/<title>')
def render_page(title):
    page = database.get_page(title)
    if page:
        return template(pages.default, page_title=page[0].replace('_', ' '), page_subtitle=page[1], pages=database.get_pages(), content=mistune.markdown(page[2]), css=pages.css)
    return template(pages.default, page_title=title.replace('_', ' '), page_subtitle="Unknown page.  Would you like to create it?", pages=database.get_pages(), content=pages.unknown_block.format(title), css=pages.css)


@app.get('/edit/<title>')
def edit_page(title):
    page = database.get_page(title)
    if page:
        return template(pages.edit, page_title=page[0].replace('_', ' '), page_subtitle=page[1], body=page[2], pages=database.get_pages(), css=pages.css)
    database.create_page(title)
    return template(pages.edit, page_title=title.replace('_', ' '), page_subtitle="", pages=database.get_pages(), css=pages.css, body="")


@app.post('/edit/<title>')
def save_page(title):
    msg = (request.forms.get('title'), request.forms.get('subtitle'), request.forms.get('content'))
    database.save_page(msg)
    return redirect('/wiki/{0}'.format(title))


@app.route('/delete/<title>')
def delete_page(title):
    database.delete_page(title)
    return redirect('/')

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