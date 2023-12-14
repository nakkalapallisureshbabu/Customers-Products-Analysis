from bottle import Bottle,template, redirect, request,static_file
import database
app = Bottle()
@app.route('/static/<filename:path>')
def serve_static(filename):
    return static_file(filename, root='')
@app.route("/")
def get_list():
    rows = database.get_items()
    n=database.get_borrowers()
    return template("list", customers=rows,products=n)
@app.post('/search')
def search():
    search_query = request.forms.get('search_query', '')
    results=database.search_book(search_query)
    return template('search_results', results=results, search_query=search_query)
@app.route("/add")
def get_add():
    return template("add_item.tpl")

@app.post("/add")
def post_add():
    cust_id = request.forms.get("cust_id")
    cust_name=request.forms.get("cust_name")
    ph_no=request.forms.get("ph_no")
    email=request.forms.get("email")
    prod_id=request.forms.get("prod_id")
    database.add_item(cust_id,cust_name,ph_no,email,prod_id)
    redirect("/")
@app.route("/update/<id>")
def get_update(id):
    rows = database.get_items(id)
    if len(rows) != 1:
        redirect("/")
    cust_id= rows[0]['cust_id']
    cust_name = rows[0]['cust_name']
    ph_no = rows[0]['ph_no']
    email = rows[0]['email']
    prod_id = rows[0]['prod_id']

    return template("update_item.tpl", cust_id=cust_id,cust_name=cust_name,ph_no=ph_no,email=email,prod_id=prod_id)

@app.post("/update")
def post_update():
    cust_id = request.forms.get("cust_id")
    cust_name=request.forms.get("cust_name")
    ph_no=request.forms.get("ph_no")
    email=request.forms.get("email")
    prod_id=request.forms.get("prod_id")
    id = request.forms.get("id")
    database.update_item(cust_id, cust_name,ph_no,email,prod_id,id)
    redirect("/")
@app.route("/delete/<id>")
def get_delete(id):
    database.delete_item(id)
    redirect("/")
@app.route("/addb")
def get_addb():
    return template("add_bor.tpl")
@app.post("/addb")
def post_add():
   
    prod_id = request.forms.get("prod_id")
    prod_name=request.forms.get("prod_name")
    use_by_date=request.forms.get("use_by_date")
    database.add_bor(prod_id, prod_name ,use_by_date)
    redirect("/")

@app.route("/deletebor/<id>")
def get_delete(id):
    database.delete_bor(id)
    redirect("/")
@app.route("/updateb/<id>")
def get_updatebor(id):
    b = database.get_borrowers(id)
    if len(b) != 1:
        redirect("/list")
    prod_id = b[0]['prod_id']
    prod_name = b[0]['prod_name']
    use_by_date = b[0]['use_by_date']

    return template("update_bor.tpl", id=id,prod_id=prod_id,prod_name=prod_name,use_by_date=use_by_date)

@app.post("/updateb")
def post_updatebor():
    id = request.forms.get("id")
    id=int(id)
    prod_id = request.forms.get("prod_id")
    prod_name=request.forms.get("prod_name")
    use_by_date=request.forms.get("use_by_date")
    use_by_date=int(use_by_date)
    database.update_bor(id,prod_id,prod_name,use_by_date)
    redirect("/")
if '_name_' == '_main_':
    app.run(host='localhost', port=8080, debug=True)

from bottle import route, post, run, template, redirect, request
import database
@route("/")
def get_index():
    redirect("/list")
@route("/list")
def get_list():
    items = database.get_customers()
    return template("list.tpl", customers=items)
@route("/add")
def get_add():
    return template("add_item.tpl")
run(host='localhost', port=8080)
