import multiprocessing
#from service.threads.eosEffectImports import threadedEosEffectsImport
from service.threads.testThread import threadedEosEffectsImport

def executeStartupThreads():
    """
    These threads run _very_ early on.  You should not assume anything Pyfa related is available.
    """

    # Imports all Eos effects to speed up the first fit processing.
    job_eos_effects_import = multiprocessing.Process(name='EosEffectImport', target=threadedEosEffectsImport)
    multiprocessing.Process()
    job_eos_effects_import.daemon = True
    job_eos_effects_import.start()
