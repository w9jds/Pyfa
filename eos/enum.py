class Enum(object):
    def __init__(self):
        pass

    @classmethod
    def getTypes(cls):
        for stuff in cls.__dict__:
            if stuff.upper() == stuff:
                yield stuff

    @classmethod
    def getName(cls, v):
        _map = getattr(cls, "_map", None)
        if _map is None:
            _map = cls._map = {}
            for _type in cls.getTypes():
                _map[cls.getValue(_type)] = _type

        return _map.get(v)

    @classmethod
    def getValue(cls, _type):
        return cls.__dict__[_type]
