# moduleBonusWarfareLinkInfo
#
# Used by:
# Variations of module: Information Command Burst I (2 of 2)

effectType = "active", "gang"


def handler(fit, container, context, **kwargs):
    for x in xrange(1, 5):
        if container.getModifiedChargeAttr("warfareBuff{}ID".format(x)):
            value = container.getModifiedItemAttr("warfareBuff{}Value".format(x))
            warfare_buff_id = container.getModifiedChargeAttr("warfareBuff{}ID".format(x))

            if warfare_buff_id:
                fit.addCommandBonus(warfare_buff_id, value, container, kwargs['effect'])
