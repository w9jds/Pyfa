# eliteBonusJumpFreighterArmorHP1
#
# Used by:
# Ship: Anshar
# Ship: Ark
effectType = "passive"


def handler(fit, ship, context):
    fit.ship.boostItemAttr("armorHP", ship.getModifiedItemAttr("eliteBonusJumpFreighter1"), skill="Jump Freighters")
