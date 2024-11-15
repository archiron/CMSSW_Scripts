# Auto generated configuration file
# using: 
# Revision: 1.19 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: step2 --conditions auto:phase1_2024_realistic --datatier GEN-SIM-DIGI-RAW --era Run3_2024 --eventcontent FEVTDEBUGHLT --filein file:step1.root --fileout file:step2.root --geometry DB:Extended --nStreams 4 --nThreads 8 --no_exec --number 10 --pileup Run3_Flat55To75_PoissonOOTPU --pileup_input das:/RelValMinBias_14TeV/CMSSW_14_1_0_pre6-140X_mcRun3_2024_realistic_v15_STD_2024_MinBias-v1/GEN-SIM --python_filename step_2_cfg.py --step DIGI:pdigi_valid,L1,DIGI2RAW,HLT:@relval2024
import FWCore.ParameterSet.Config as cms

from Configuration.Eras.Era_Run3_2024_cff import Run3_2024

if len(sys.argv) > 1:
    print(sys.argv)
    print("step 2 - arg. 0 :", sys.argv[0]) # name of the script
    print("step 2 - arg. 1 :", sys.argv[1]) # index
    print("step 2 - arg. 2 :", sys.argv[2]) # path of the script ($LOG_SOURCE)
    print("step 2 - arg. 3 :", sys.argv[3]) # nb of evts
    print("step 2 - arg. 4 :", sys.argv[4]) # path of output
    ind = int(sys.argv[1])
    max_number = int(sys.argv[3])
    outputPath = sys.argv[4]
else:
    print("step 2 - rien")
    ind = 0
    path = ''
    max_number = 10 # number of events

max_skipped = (ind-1) * max_number

process = cms.Process('HLT',Run3_2024)

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mix_Run3_Flat55To75_PoissonOOTPU_cfi')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.MagneticField_cff')
process.load('Configuration.StandardSequences.Digi_cff')
process.load('Configuration.StandardSequences.SimL1Emulator_cff')
process.load('Configuration.StandardSequences.DigiToRaw_cff')
process.load('HLTrigger.Configuration.HLT_GRun_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(max_number),
    output = cms.optional.untracked.allowed(cms.int32,cms.PSet)
)

# Input source
process.source = cms.Source("PoolSource",
    dropDescendantsOfDroppedBranches = cms.untracked.bool(False),
    skipEvents = cms.untracked.uint32(max_skipped),
    #fileNames = cms.untracked.vstring('file:step1.root'),
    #fileNames = cms.untracked.vstring('file:' + outputPath + '/step1_' + '%0004d'%max_number + '_' + '%003d'%ind + '.root'),
    fileNames = cms.untracked.vstring('file:' + outputPath + '/step1_9000_001.root'),
    inputCommands = cms.untracked.vstring(
        'keep *',
        'drop *_genParticles_*_*',
        'drop *_genParticlesForJets_*_*',
        'drop *_kt4GenJets_*_*',
        'drop *_kt6GenJets_*_*',
        'drop *_iterativeCone5GenJets_*_*',
        'drop *_ak4GenJets_*_*',
        'drop *_ak7GenJets_*_*',
        'drop *_ak8GenJets_*_*',
        'drop *_ak4GenJetsNoNu_*_*',
        'drop *_ak8GenJetsNoNu_*_*',
        'drop *_genCandidatesForMET_*_*',
        'drop *_genParticlesForMETAllVisible_*_*',
        'drop *_genMetCalo_*_*',
        'drop *_genMetCaloAndNonPrompt_*_*',
        'drop *_genMetTrue_*_*',
        'drop *_genMetIC5GenJs_*_*'
    ),
    secondaryFileNames = cms.untracked.vstring()
)

process.options = cms.untracked.PSet(
    IgnoreCompletely = cms.untracked.vstring(),
    Rethrow = cms.untracked.vstring(),
    TryToContinue = cms.untracked.vstring(),
    accelerators = cms.untracked.vstring('*'),
    allowUnscheduled = cms.obsolete.untracked.bool,
    canDeleteEarly = cms.untracked.vstring(),
    deleteNonConsumedUnscheduledModules = cms.untracked.bool(True),
    dumpOptions = cms.untracked.bool(False),
    emptyRunLumiMode = cms.obsolete.untracked.string,
    eventSetup = cms.untracked.PSet(
        forceNumberOfConcurrentIOVs = cms.untracked.PSet(
            allowAnyLabel_=cms.required.untracked.uint32
        ),
        numberOfConcurrentIOVs = cms.untracked.uint32(0)
    ),
    fileMode = cms.untracked.string('FULLMERGE'),
    forceEventSetupCacheClearOnNewRun = cms.untracked.bool(False),
    holdsReferencesToDeleteEarly = cms.untracked.VPSet(),
    makeTriggerResults = cms.obsolete.untracked.bool,
    modulesToCallForTryToContinue = cms.untracked.vstring(),
    modulesToIgnoreForDeleteEarly = cms.untracked.vstring(),
    numberOfConcurrentLuminosityBlocks = cms.untracked.uint32(0),
    numberOfConcurrentRuns = cms.untracked.uint32(1),
    numberOfStreams = cms.untracked.uint32(0),
    numberOfThreads = cms.untracked.uint32(1),
    printDependencies = cms.untracked.bool(False),
    sizeOfStackForThreadsInKB = cms.optional.untracked.uint32,
    throwIfIllegalParameter = cms.untracked.bool(True),
    wantSummary = cms.untracked.bool(False)
)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    annotation = cms.untracked.string('step2 nevts:10'),
    name = cms.untracked.string('Applications'),
    version = cms.untracked.string('$Revision: 1.19 $')
)

# Output definition

process.FEVTDEBUGHLToutput = cms.OutputModule("PoolOutputModule",
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('GEN-SIM-DIGI-RAW'),
        filterName = cms.untracked.string('')
    ),
    #fileName = cms.untracked.string('file:step2.root'),
    fileName = cms.untracked.string('file:' + outputPath + '/step2_' + '%0004d'%max_number + '_' + '%003d'%ind + '.root'),
    outputCommands = process.FEVTDEBUGHLTEventContent.outputCommands,
    splitLevel = cms.untracked.int32(0)
)

# Additional output definition

# Other statements
process.mix.input.fileNames = cms.untracked.vstring(['/store/relval/CMSSW_14_1_0_pre6/RelValMinBias_14TeV/GEN-SIM/140X_mcRun3_2024_realistic_v15_STD_2024_MinBias-v1/2580000/0210860e-b5c5-4dfe-b546-2f4668bddf8f.root', '/store/relval/CMSSW_14_1_0_pre6/RelValMinBias_14TeV/GEN-SIM/140X_mcRun3_2024_realistic_v15_STD_2024_MinBias-v1/2580000/028c421e-c124-4243-af2b-e17c16c54f83.root', '/store/relval/CMSSW_14_1_0_pre6/RelValMinBias_14TeV/GEN-SIM/140X_mcRun3_2024_realistic_v15_STD_2024_MinBias-v1/2580000/0792c534-cec4-4460-b901-130f084268a8.root', '/store/relval/CMSSW_14_1_0_pre6/RelValMinBias_14TeV/GEN-SIM/140X_mcRun3_2024_realistic_v15_STD_2024_MinBias-v1/2580000/2027d428-9f89-422d-b9bb-3e4d80ab9ef3.root', '/store/relval/CMSSW_14_1_0_pre6/RelValMinBias_14TeV/GEN-SIM/140X_mcRun3_2024_realistic_v15_STD_2024_MinBias-v1/2580000/2bec988f-5242-473b-bc03-7ea6f66ba829.root', '/store/relval/CMSSW_14_1_0_pre6/RelValMinBias_14TeV/GEN-SIM/140X_mcRun3_2024_realistic_v15_STD_2024_MinBias-v1/2580000/34e5385b-7aaa-491b-a486-329b1238ca50.root', '/store/relval/CMSSW_14_1_0_pre6/RelValMinBias_14TeV/GEN-SIM/140X_mcRun3_2024_realistic_v15_STD_2024_MinBias-v1/2580000/3d8244f8-3fdd-436f-931b-c041fbbea5e3.root', '/store/relval/CMSSW_14_1_0_pre6/RelValMinBias_14TeV/GEN-SIM/140X_mcRun3_2024_realistic_v15_STD_2024_MinBias-v1/2580000/3f92993f-682d-4308-ac78-ddaa1eb15adf.root', '/store/relval/CMSSW_14_1_0_pre6/RelValMinBias_14TeV/GEN-SIM/140X_mcRun3_2024_realistic_v15_STD_2024_MinBias-v1/2580000/49644702-058a-4267-a379-1c33b6510e07.root', '/store/relval/CMSSW_14_1_0_pre6/RelValMinBias_14TeV/GEN-SIM/140X_mcRun3_2024_realistic_v15_STD_2024_MinBias-v1/2580000/4d79ee25-8e26-4e7d-a513-78b797887aac.root', '/store/relval/CMSSW_14_1_0_pre6/RelValMinBias_14TeV/GEN-SIM/140X_mcRun3_2024_realistic_v15_STD_2024_MinBias-v1/2580000/60c3aa0a-f20b-4a8c-8205-1a789610bf86.root', '/store/relval/CMSSW_14_1_0_pre6/RelValMinBias_14TeV/GEN-SIM/140X_mcRun3_2024_realistic_v15_STD_2024_MinBias-v1/2580000/736bfd97-827a-4ecc-8888-b06bb2ce99ad.root', '/store/relval/CMSSW_14_1_0_pre6/RelValMinBias_14TeV/GEN-SIM/140X_mcRun3_2024_realistic_v15_STD_2024_MinBias-v1/2580000/748fda78-10f6-4d09-818c-475d637b8fd9.root', '/store/relval/CMSSW_14_1_0_pre6/RelValMinBias_14TeV/GEN-SIM/140X_mcRun3_2024_realistic_v15_STD_2024_MinBias-v1/2580000/75b3a060-14af-4674-aaa3-8af8a97b6ebc.root', '/store/relval/CMSSW_14_1_0_pre6/RelValMinBias_14TeV/GEN-SIM/140X_mcRun3_2024_realistic_v15_STD_2024_MinBias-v1/2580000/773ae9f1-ccba-43c7-b8e4-90c7e157896e.root', '/store/relval/CMSSW_14_1_0_pre6/RelValMinBias_14TeV/GEN-SIM/140X_mcRun3_2024_realistic_v15_STD_2024_MinBias-v1/2580000/80efb22a-9bbd-47a5-a348-672a25b54c3c.root', '/store/relval/CMSSW_14_1_0_pre6/RelValMinBias_14TeV/GEN-SIM/140X_mcRun3_2024_realistic_v15_STD_2024_MinBias-v1/2580000/8ab55ee6-4585-41bf-a93d-425cf0e7bc36.root', '/store/relval/CMSSW_14_1_0_pre6/RelValMinBias_14TeV/GEN-SIM/140X_mcRun3_2024_realistic_v15_STD_2024_MinBias-v1/2580000/8ea845f0-97c4-4c2f-9caf-d41a60b830c2.root', '/store/relval/CMSSW_14_1_0_pre6/RelValMinBias_14TeV/GEN-SIM/140X_mcRun3_2024_realistic_v15_STD_2024_MinBias-v1/2580000/91414403-d859-4960-a273-914eeec99248.root', '/store/relval/CMSSW_14_1_0_pre6/RelValMinBias_14TeV/GEN-SIM/140X_mcRun3_2024_realistic_v15_STD_2024_MinBias-v1/2580000/9251c413-c6e0-4620-9cb0-2d4b1d463272.root', '/store/relval/CMSSW_14_1_0_pre6/RelValMinBias_14TeV/GEN-SIM/140X_mcRun3_2024_realistic_v15_STD_2024_MinBias-v1/2580000/92a1b952-654e-4aa3-a39e-b154222a1c82.root', '/store/relval/CMSSW_14_1_0_pre6/RelValMinBias_14TeV/GEN-SIM/140X_mcRun3_2024_realistic_v15_STD_2024_MinBias-v1/2580000/a12c3bf8-9cf0-437d-a00b-205a4adf1632.root', '/store/relval/CMSSW_14_1_0_pre6/RelValMinBias_14TeV/GEN-SIM/140X_mcRun3_2024_realistic_v15_STD_2024_MinBias-v1/2580000/a87262b3-dc35-4ffb-bc44-904204f8ac3e.root', '/store/relval/CMSSW_14_1_0_pre6/RelValMinBias_14TeV/GEN-SIM/140X_mcRun3_2024_realistic_v15_STD_2024_MinBias-v1/2580000/b74a3616-e6f0-4a04-8515-1ad2e911b928.root', '/store/relval/CMSSW_14_1_0_pre6/RelValMinBias_14TeV/GEN-SIM/140X_mcRun3_2024_realistic_v15_STD_2024_MinBias-v1/2580000/ca30ff05-e601-4780-8769-383f42b4f036.root', '/store/relval/CMSSW_14_1_0_pre6/RelValMinBias_14TeV/GEN-SIM/140X_mcRun3_2024_realistic_v15_STD_2024_MinBias-v1/2580000/d63a3dd3-ea7e-48e3-9735-415ab5fa767d.root', '/store/relval/CMSSW_14_1_0_pre6/RelValMinBias_14TeV/GEN-SIM/140X_mcRun3_2024_realistic_v15_STD_2024_MinBias-v1/2580000/ef27330a-0c3a-45c5-a728-0958553237c5.root', '/store/relval/CMSSW_14_1_0_pre6/RelValMinBias_14TeV/GEN-SIM/140X_mcRun3_2024_realistic_v15_STD_2024_MinBias-v1/2580000/f75a90a6-0eb2-447e-8915-7abf3551c0d6.root', '/store/relval/CMSSW_14_1_0_pre6/RelValMinBias_14TeV/GEN-SIM/140X_mcRun3_2024_realistic_v15_STD_2024_MinBias-v1/2580000/f94d2ef7-4931-4d42-a426-b6fc699ccffe.root', '/store/relval/CMSSW_14_1_0_pre6/RelValMinBias_14TeV/GEN-SIM/140X_mcRun3_2024_realistic_v15_STD_2024_MinBias-v1/2580000/fc85a38a-5b2b-4040-8e7d-2afffde21cce.root', '/store/relval/CMSSW_14_1_0_pre6/RelValMinBias_14TeV/GEN-SIM/140X_mcRun3_2024_realistic_v15_STD_2024_MinBias-v1/2580000/ffdd45d1-6d18-4c64-8cd5-4a6129e7a5eb.root'])
process.mix.digitizers = cms.PSet(process.theDigitizersValid)
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:phase1_2024_realistic', '')

# Path and EndPath definitions
process.digitisation_step = cms.Path(process.pdigi_valid)
process.L1simulation_step = cms.Path(process.SimL1Emulator)
process.digi2raw_step = cms.Path(process.DigiToRaw)
process.endjob_step = cms.EndPath(process.endOfProcess)
process.FEVTDEBUGHLToutput_step = cms.EndPath(process.FEVTDEBUGHLToutput)

# Schedule definition
# process.schedule imported from cff in HLTrigger.Configuration
process.schedule.insert(0, process.digitisation_step)
process.schedule.insert(1, process.L1simulation_step)
process.schedule.insert(2, process.digi2raw_step)
process.schedule.extend([process.endjob_step,process.FEVTDEBUGHLToutput_step])
from PhysicsTools.PatAlgos.tools.helpers import associatePatAlgosToolsTask
associatePatAlgosToolsTask(process)

#Setup FWK for multithreaded
process.options.numberOfThreads = 8
process.options.numberOfStreams = 4

# customisation of the process.

# Automatic addition of the customisation function from HLTrigger.Configuration.customizeHLTforMC
from HLTrigger.Configuration.customizeHLTforMC import customizeHLTforMC 

#call to customisation function customizeHLTforMC imported from HLTrigger.Configuration.customizeHLTforMC
process = customizeHLTforMC(process)

# End of customisation functions


# Customisation from command line

# Add early deletion of temporary data products to reduce peak memory need
from Configuration.StandardSequences.earlyDeleteSettings_cff import customiseEarlyDelete
process = customiseEarlyDelete(process)
# End adding early deletion
