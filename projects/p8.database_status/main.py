import MySQLdb as mysql

from rich.console import Console
from rich.text import Text


def cp(string):
    console.print(Text(string, style='bold #00FF00'))


def rp(string):
    console.print(Text(string, style='bold red'))


try:
    console = Console()
    db = mysql.connect(host='localhost', user='root',
                       password='root', db="INFORMATION_SCHEMA")
    cur = db.cursor()
    cur.execute('SHOW STATUS')
    res = cur.fetchall()

    r = dict(res)
    cp(f"Uptime => {r['Uptime']}")
    cp(f"Threads_created => {r['Threads_created']}")
    cp(f"Threads_connected => {r['Threads_connected']}")
    cp(f"Threads_running => {r['Threads_running']}")
    cp(f"Queries => {r['Queries']}")
    cp(f"Max_used_connections => {r['Max_used_connections']}")
    cur.close()
except:
    rp('use with sudo instead')
finally:
    cp('execution done')
