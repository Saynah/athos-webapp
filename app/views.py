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

	# mpld3 to create plot 
	fig, ax = plt.subplots()
	ax.plot([3,1,4,1,5], 'k-')
	my_plot = mpld3.fig_to_html(fig)

	return render_template('dashboard.html',
		user = {'nickname': name},
		my_plot = my_plot
		)

# for some reason, this does not render all the time