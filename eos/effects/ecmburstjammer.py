# ECMBurstJammer
#
# Used by:
# Modules from group: Burst Jammer (11 of 11)
from eos.modifiedAttributeDict import ModifiedAttributeDict

effectType = "projected", "active"


def handler(fit, container, context, **kwargs):
    if "projected" in context:
        # jam formula: 1 - (1- (jammer str/ship str))^(# of jam mods with same str))
        strModifier = 1 - container.getModifiedItemAttr("scan{0}StrengthBonus".format(fit.scanType)) / fit.scanStrength

        if 'effect' in kwargs:
            strModifier *= ModifiedAttributeDict.getResistance(fit, kwargs['effect'])

        fit.ecmProjectedStr *= strModifier
