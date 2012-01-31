from werkzeug import import_string, cached_property



class LazyLoad(object):

    def __init__(self, import_name):
        self.__module__, self.__name__ = import_name.rsplit('.', 1)
        self.import_name = import_name

    @cached_property
    def load(self):
        return import_string(self.import_name)

    def __call__(self, *args, **kwargs):
        return self.load(*args, **kwargs)