import web

from web.template import ALLOWED_AST_NODES
ALLOWED_AST_NODES.append('Constant')

urls = (
    '/(.*)', 'mvc.controllers.vistas.Visitas'
)
app = web.application(urls, globals())

if __name__ == "__main__":
    app.run()
