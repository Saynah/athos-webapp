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
	# text input
	name = 'Marruecos'

	# line plot input
	x = [1, 2, 3, 4, 5]
	y = [2, 6, 2, 7, 8]

	# pie chart input
	sizes = [15, 30, 45, 10]
	explode = (0, 0.1, 0, 0)
	labels = 'Frogs', 'Hogs', 'Dogs', 'Logs'

	#
	return render_template('dashboard.html',
		user = {'nickname': name},
		my_plot = html_line_plot( x, y ),
		my_pie = html_pie_chart( sizes, explode, labels )
		)

def html_line_plot(x,y):
	# mpld3 to create line plot 
	fig, ax = plt.subplots()
	ax.plot(x, y, 'k-')
	return mpld3.fig_to_html(fig)

def html_pie_chart(sizes, explode, labels):
	# mpld3 to create bar chart
	colors = ['yellowgreen', 'gold', 'lightskyblue', 'lightcoral']

	fig, ax = plt.subplots()
	ax.pie(sizes, explode=explode, labels=labels, colors=colors,
	        autopct='%1.1f%%', shadow=True, startangle=90)
	# Set aspect ratio to be equal so that pie is drawn as a circle.
	ax.axis('equal')
	return mpld3.fig_to_html(fig)
