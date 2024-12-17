import sqlite3

from flask import Flask, render_template_string, render_template

app = Flask(__name__)

@app.route('/gifts')

def get_gifts():

    try:

        con=sqlite3.connect("C:\\temp\\gifts.db")

        cursor=con.cursor()

        xgifts = []

   

        xsql = 'SELECT id, name, gift, cost, status FROM gifts'


        cursor.execute(xsql, ())

        xcolumns = [column[0] for column in cursor.description]

        xrows = cursor.fetchall()


        for row in xrows:

          xgifts.append(dict(zip(xcolumns, row)))

           

        source = """<table border="1"><thead><tr>

<th>ФИО</th>

<th>Подарок</th>

<th>Стоимость</th>

<th>Статус</th>

</tr></thead>

<tbody>

{% for row in data %}

<tr> <td>{{row['name']}}</td>

<td>{{row['gift']}}</td>

<td>{{row['cost']}}</td>

<td>{{ 'куплен' if row['status'] == 1 else 'не куплен'}}</td>

</tr>

{% endfor %}

</tbody>

</table>"""

        return render_template_string(source, data=xgifts)

        #return render_template('C:/temp/gifts.html', data=xgifts) шаблон gifts.html не подключился на компьютере

    except Exception as e:

        return e

    finally:

        con.close()

 

if (__name__ == '__main__'):

    app.run()