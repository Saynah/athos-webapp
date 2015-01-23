from flask import render_template
from app import app
import matplotlib.pyplot as plt, mpld3

@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html",
       title = 'Home', user = { 'nickname': 'Mark' },
       )

# keep this page for debugging purposes
@app.route("/db_fancy")
def cities_page_fancy():
    with db:
        cur = db.cursor()
        cur.execute("SELECT Name, CountryCode, Population FROM City ORDER BY Population LIMIT 15;")

        query_results = cur.fetchall()
    cities = []
    for result in query_results:
        cities.append(dict(name=result[0], country=result[1], population=result[2]))
    return render_template('cities.html', cities=cities)

# page for the actual app
@app.route("/dashboard")
def my_dashboard():
	name = 'Marruecos'

	x = [1, 2, 3, 4, 5]
	y = [2, 6, 2, 7, 8]

	return render_template('dashboard.html',
		user = {'nickname': name},
		my_plot = html_line_plot(x,y)
		)

def html_line_plot(x,y):
	# mpld3 to create line plot 
	fig, ax = plt.subplots()
	ax.plot(x, y, 'k-')
	return mpld3.fig_to_html(fig)