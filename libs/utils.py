# -*- coding: utf-8 -*-


def set_trace():
    from IPython.core.debugger import Pdb
    Pdb(color_scheme='Linux').set_trace()


def profile(log_file='log_profile', log_dir=None):
    import cProfile
    import os
    from datetime import datetime
    if not log_dir:
        log_dir = os.path.join(os.path.expanduser('~'), 'logs')

    def _outer(f):
        def _inner(*args, **kwargs):
            pr = cProfile.Profile()
            pr.enable()
            try:
                ret = f(*args, **kwargs)
            finally:
                pr.disable()
                log_name = os.path.join(log_dir, '%s_%s' % (log_file, datetime.now().strftime('%Y%m%d%H%M%S.%f')))
                pr.dump_stats(log_name)
            return ret
        return _inner
    return _outer
