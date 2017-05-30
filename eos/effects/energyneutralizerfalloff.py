# energyNeutralizerFalloff
#
# Used by:
# Modules from group: Energy Neutralizer (51 of 51)
from eos.saveddata.module import State
from eos.modifiedAttributeDict import ModifiedAttributeDict

effectType = "active", "projected"


def handler(fit, src, context, **kwargs):
    if "projected" in context and ((hasattr(src, "state") and src.state >= State.ACTIVE) or
                                       hasattr(src, "amountActive")):
        amount = src.getModifiedItemAttr("energyNeutralizerAmount")
        time = src.cycleTime

        if 'effect' in kwargs:
            amount *= ModifiedAttributeDict.getResistance(fit, kwargs['effect'])

        time = src.getModifiedItemAttr("duration")

        fit.addDrain(src, time, amount, 0)
