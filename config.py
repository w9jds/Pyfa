import os
import sys

from logbook import Logger

pyfalog = Logger(__name__)

# Load variable overrides specific to distribution type
try:
    import configforced
except ImportError:
    pyfalog.warning("Failed to import: configforced")
    configforced = None

# Turns on debug mode
debug = False
# Defines if our saveddata will be in pyfa root or not
saveInRoot = False

# Version data
version = "2017.04.07"
if hasattr(sys, 'frozen'):
    tag = "(release)"
else:
    tag = "(live)"
expansionName = "YC119.3"
expansionVersion = "1.0"
evemonMinVersion = "4081"

pyfaPath = None
savePath = None
saveDB = None
gameDB = None
logPath = None


def isFrozen():
    if hasattr(sys, 'frozen'):
        return True
    else:
        return False


def __createDirs(path):
    if not os.path.exists(path):
        os.makedirs(path)


def defPaths(customSavePath):
    global debug
    global pyfaPath
    global savePath
    global saveDB
    global gameDB
    global saveInRoot

    pyfalog.debug("Configuring Pyfa")

    # The main pyfa directory which contains run.py
    # Python 2.X uses ANSI by default, so we need to convert the character encoding
    pyfaPath = getattr(configforced, "pyfaPath", pyfaPath)
    if pyfaPath is None:
        pyfaPath = getPyfaPath()

    # Where we store the saved fits etc, default is the current users home directory
    if saveInRoot is True:
        savePath = getattr(configforced, "savePath", None)
        if savePath is None:
            savePath = getPyfaPath(u"saveddata")
    else:
        savePath = getattr(configforced, "savePath", None)
        if savePath is None:
            if customSavePath is None:  # customSavePath is not overriden
                savePath = getSavePath()
            else:
                savePath = customSavePath

    __createDirs(savePath)

    if isFrozen():
        os.environ["REQUESTS_CA_BUNDLE"] = getPyfaPath(u"cacert.pem")
        os.environ["SSL_CERT_FILE"] = getPyfaPath(u"cacert.pem")

    # The database where we store all the fits etc
    saveDB = getSavePath("saveddata.db")

    # The database where the static EVE data from the datadump is kept.
    # This is not the standard sqlite datadump but a modified version created by eos
    # maintenance script
    gameDB = getPyfaPath("eve.db")

    # DON'T MODIFY ANYTHING BELOW
    import eos.config

    # Caching modifiers, disable all gamedata caching, its unneeded.
    eos.config.gamedataCache = False
    # saveddata db location modifier, shouldn't ever need to touch this
    eos.config.saveddata_connectionstring = "sqlite:///" + saveDB + "?check_same_thread=False"
    eos.config.gamedata_connectionstring = "sqlite:///" + gameDB + "?check_same_thread=False"


def getPyfaPath(Append=None):
    base = __file__
    base_alt = sys.argv[0]

    try:
        base = unicode(base)
        base_alt = unicode(base_alt)
    except:
        base = unicode(base, sys.getfilesystemencoding())
        base_alt = unicode(base_alt, sys.getfilesystemencoding())

    root = os.path.dirname(os.path.realpath(base))

    if not os.path.isdir(root):
        root = os.path.dirname(os.path.realpath(base_alt))

    if not Append:
        return root

    try:
        Append = unicode(Append)
    except:
        Append = unicode(Append, sys.getfilesystemencoding())

    path = os.path.realpath(os.path.join(root, Append))

    return path


def getSavePath(Append=None):
    root = os.path.expanduser(os.path.join(u"~", u".pyfa"))

    if not Append:
        return root

    try:
        Append = unicode(Append)
    except:
        Append = unicode(Append, sys.getfilesystemencoding())

    path = os.path.realpath(os.path.join(root, Append))

    return path
