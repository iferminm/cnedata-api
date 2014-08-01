#coding=utf-8
import cherrypy


@cherrypy.popargs('name', 'year', 'object')
class Eleccion(object):
    def __init__(self):
        self.centros = 'Centros acá'

    @cherrypy.expose
    def index(self, name, year):
        return 'Eleccion %s de %s' % (name, year)



if __name__ == '__main__':
    cherrypy.quickstart(Eleccion())
