# Not used by any item
effectType = "projected", "active"


def handler(fit, container, context):
    if "projected" in context:
        # jam formula: 1 - (1- (jammer str/ship str))^(# of jam mods with same str))
        strModifier = 1 - container.getModifiedItemAttr("scan{0}StrengthBonus".format(fit.scanType)) / fit.scanStrength

        fit.ecmProjectedStr *= strModifier
