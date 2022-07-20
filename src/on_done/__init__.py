from ._on_done import OnDone


def load_ipython_extension(ipython):
    ipython.register_magics(OnDone)
