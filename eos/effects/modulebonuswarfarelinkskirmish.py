# moduleBonusWarfareLinkSkirmish
#
# Used by:
# Variations of module: Skirmish Command Burst I (2 of 2)

effectType = "active", "gang"


def handler(fit, container, context, **kwargs):
    for x in xrange(1, 5):
        if container.getModifiedChargeAttr("warfareBuff{}ID".format(x)):
            value = container.getModifiedItemAttr("warfareBuff{}Value".format(x))
            container = container.getModifiedChargeAttr("warfareBuff{}ID".format(x))

            if container:
                fit.addCommandBonus(container, value, container, kwargs['effect'])
