def write_models_info(file_path, show_type=True):
    data = get_models_info(show_type)
    with open(file_path, 'w') as f:
        f.write(data)


def get_models_info(show_type=True):
    import json
    from django.apps import apps
    result = {
        'nodes': {},
        'edges': set(),
    }
    for model in apps.get_models():
        result['nodes'][model.__name__] = []
        for field in model._meta.fields:
            result['nodes'][model.__name__].append(get_field_name(field, show_type))
            if hasattr(field, 'related'):
                if hasattr(field, 'related_model'):
                    result['edges'].add('%s -> %s' % (field.related_model.__name__, model.__name__))
                elif hasattr(field.related, 'parent_model'):
                    result['edges'].add('%s -> %s' % (field.related.parent_model.__name__, model.__name__))

        for field in model._meta.many_to_many:
            result['nodes'][model.__name__].append(get_field_name(field, show_type))
            result['nodes'][field.rel.through.__name__] = []
            result['edges'].add('%s -> %s' % (model.__name__, field.rel.through.__name__))
            result['edges'].add('%s -> %s' % (field.rel.to.__name__, field.rel.through.__name__))
            for sub_field in field.rel.through._meta.fields:
                result['nodes'][field.rel.through.__name__].append(get_field_name(sub_field, show_type))

    result['edges'] = list(result['edges'])
    return json.dumps(result, indent=4)


def get_field_name(field, show_type):
    if show_type:
        return '%s: %s' % (field.name, field.__class__.__name__)
    return field.name
