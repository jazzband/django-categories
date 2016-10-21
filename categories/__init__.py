__version_info__ = {
    'major': 1,
    'minor': 4,
    'micro': 3,
    'releaselevel': 'final',
    'serial': 1
}


def get_version(short=False):
    assert __version_info__['releaselevel'] in ('alpha', 'beta', 'final')
    vers = ["%(major)i.%(minor)i" % __version_info__, ]
    if __version_info__['micro'] and not short:
        vers.append(".%(micro)i" % __version_info__)
    if __version_info__['releaselevel'] != 'final' and not short:
        vers.append('%s%i' % (__version_info__['releaselevel'][0], __version_info__['serial']))
    return ''.join(vers)

__version__ = get_version()


default_app_config = 'categories.apps.CategoriesConfig'


def register():
    from categories import settings
    from categories.registration import (_process_registry, registry)
    _process_registry(settings.FK_REGISTRY, registry.register_fk)
    _process_registry(settings.M2M_REGISTRY, registry.register_m2m)
try:
    register()
except Exception as e:
    print(e)
