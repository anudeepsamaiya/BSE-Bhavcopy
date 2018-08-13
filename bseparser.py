
import os
import cherrypy
import jinja2
import pandas as pd
import redis


# jinja2 template renderer
ENV  = jinja2.Environment(loader=jinja2.FileSystemLoader(os.path.join(BASE_DIR, 'templates')))

def render_template(template, **context):
    global ENV
    template = ENV.get_template(template+'.html')
    return template.render(context)


CSVFILE = BASE_DIR + '/EQ060618_CSV/EQ060618.CSV'
BASE_DIR = os.path.dirname(os.path.realpath(__file__))
r = redis.StrictRedis(host='localhost', port=6379, db=1)

def populate_data_into_redis(csv_file, date):
    self.df = pd.read_csv(csv_file)
    self.data = self.df.T.loc[['SC_CODE','SC_NAME','OPEN','HIGH', 'LOW', 'CLOSE']].to_dict()
    for d in self.data.values():
        code, nm = d.get('SC_CODE'), d.get('SC_NAME')
        key = '%s:%s' %(code, nm and nm.strip())
        r.hmset(key, d)


class BSEParser(object):

    @cherrypy.expose
    def index(self):
        return 'Hello inhabitants of Earth \V/'

    @cherrypy.expose
    def get_data(self):
        return render_template('csvdump', data=dict())

    @cherrypy.expose
    def find_scrip(self):
        csvdata = pd.read_csv(csvfile)
        return render_template('csvdump', data=dict())


if __name__=='__main__':
    cherrypy.quickstart(BSEParser())
