import os
from importlib import import_module


def threadedEosEffectsImport():
    # Walk eos.effects and add all effects so we can import them properly
    print("Starting Eos Effects Import")

    for root, __, files in os.walk("eos/effects"):
        for file_ in files:
            if file_.endswith(".py") and not file_.startswith("_"):
                root = root.replace("../", "")
                root = root.replace("/", ".")
                mod_name = "{}.{}".format(
                        root,
                        file_.split(".py")[0],
                )

                try:
                    import_module(mod_name)
                except:
                    print("Module failed to import: ", str(mod_name))
    print("Completed Eos Effects Import")
