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
        map = getattr(cls, "_map", None)
        if map is None:
            map = cls._map = {}
            for _type in cls.getTypes():
                map[cls.getValue(_type)] = _type

        return map.get(v)

    @classmethod
    def getValue(cls, _type):
        return cls.__dict__[_type]
