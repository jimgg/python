# -*- coding: utf-8 -*-

from multiprocessing.dummy import Process, Manager


def multi_load_data(instance, **kwargs):
    """多线程加载数据

    Args:
        instance: 实例或字典，承载返回的数据
        kwargs: data_name => {'f': data_function, 'args': data_args, 'kwargs': data_kwargs}
    """
    def _load(r_dict, r_name, f, f_args, f_kwargs):
        r_dict[r_name] = f(*f_args, **f_kwargs)

    manager = Manager()
    return_dict = manager.dict()
    ps = []
    for key, value in kwargs.items():
        p = Process(target=_load, args=(return_dict, key, value['f'], value.get('args', ()), value.get('kwargs', {})))
        p.start()
        ps.append(p)
    for p in ps:
        p.join()
    if isinstance(instance, dict):
        d = instance
    else:
        d = instance.__dict__
    for k, v in return_dict.items():
        d[k] = v
