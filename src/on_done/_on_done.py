from IPython.core.magic import Magics, magics_class, cell_magic


@magics_class
class OnDone(Magics):

    @cell_magic
    def on_done(self, line, cell):
        try:
            self.shell.ex(cell)
        finally:
            self.shell.ex(line)
