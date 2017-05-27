# moduleTitanEffectGenerator
#
# Used by:
# Modules from group: Titan Phenomena Generator (4 of 4)
effectType = "active", "gang"


def handler(fit, container, context, **kwargs):
    for x in xrange(1, 5):
        if container.getModifiedItemAttr("warfareBuff{}ID".format(x)):
            value = container.getModifiedItemAttr("warfareBuff{}Value".format(x))
            id = container.getModifiedItemAttr("warfareBuff{}ID".format(x))

            if id:
                fit.addCommandBonus(id, value, container, kwargs['effect'])
