import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
        self._listYear = []
        self._listColor = []

    def fillDD(self):
        pass


    def handle_graph(self, e):
        self._model.creaGrafo(self._view._ddcolor.value)
        print(self._model.getNumNodes())



    def fillDDProduct(self):
        pass


    def handle_search(self, e):
        pass

    def fillColors(self):
        colori = self._model.getColors()
        for c in colori:
            self._view._ddcolor.options.append(ft.dropdown.Option(c))

