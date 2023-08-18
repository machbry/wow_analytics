import cherrypy


class Data:
    @cherrypy.expose
    def index(self):
        return """
        <!DOCTYPE html>
        <html>
        <head>
            <title>Data back office</title>
        </head>
        <body>
            <h1>Available databases :</h1>
            <a href="./reports">Reports</a>
        </body>
        </html>
        """

    @cherrypy.expose
    def reports(self):
        return "Reports database."


class Root(object):
    data = Data()

    @cherrypy.expose
    def index(self):
        return """
        <!DOCTYPE html>
        <html>
        <head>
            <title>Back office homepage</title>
        </head>
        <body>
            <h1>Back office homepage</h1>
            <a href="./data">Data</a>
        </body>
        </html>
        """


def start_back_office():
    root = Root()

    cherrypy.tree.mount(
        root=root,
        script_name='/',
        config=None
    )

    cherrypy.engine.start()
    cherrypy.engine.block()
