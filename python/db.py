import zorder

class CollieDB(list):
    def __init__(self, *args):
        list.__init__(self, args)
        self.views = {}
        self.filters = {}
    def append(self, item):
        if not isinstance(item, dict):
            raise TypeError('item is not of type %s' % dict)
        list.append(self, item)

    def view(self, view, filt=None):
        if not 'rows' in self.views[view]:
            self.build_view(view)
        rows = self.views[view]['rows']
        if filt:
            rows = filter(self.filters[filt], rows)
        return rows
    def build_view(self, view):
        self.views[view]['rows'] = zorder.zorder(map(self.views[view]['map'], self))
    def build_all_views(self):
        for view in self.views:
            self.build_view(view)

