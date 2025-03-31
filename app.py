from flask import Flask, render_template, abort
import sqlite3

app = Flask(__name__)

def get_number_by_uid(uid):
    conn = sqlite3.connect("data.db")
    cursor = conn.cursor()
    cursor.execute("SELECT number FROM entries WHERE uid=?", (uid,))
    result = cursor.fetchone()
    conn.close()
    return result

@app.route('/entry/<string:uid>')
def show_entry(uid):
    entry = get_number_by_uid(uid)
    if entry:
        return render_template('page.html', number=entry[0])
    else:
        abort(404)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
