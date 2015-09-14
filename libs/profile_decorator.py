def profile(log_file='log.txt', log_dir=None):
    import cProfile
    import os
    if not log_dir:
        log_dir = os.path.join(os.path.expanduser('~'), 'logs')
    log_name = os.path.join(log_dir, log_file)

    def _outer(f):
        def _inner(*args, **kwargs):
            pr = cProfile.Profile()
            pr.enable()
            try:
                ret = f(*args, **kwargs)
            finally:
                pr.disable()
                pr.dump_stats(log_name)
            return ret
        return _inner
    return _outer
