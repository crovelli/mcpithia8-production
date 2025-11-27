import FWCore.ParameterSet.Config as cms

from Configuration.Generator.Pythia8CommonSettings_cfi import *
from Configuration.Generator.MCTunesRun3ECM13p6TeV.PythiaCP5Settings_cfi import *
from GeneratorInterface.EvtGenInterface.EvtGenSetting_cff import *

_generator = cms.EDFilter(
    "Pythia8GeneratorFilter",
    pythiaHepMCVerbosity = cms.untracked.bool(False),
    maxEventsToPrint = cms.untracked.int32(0),
    pythiaPylistVerbosity = cms.untracked.int32(0),
    comEnergy = cms.double(13600.0),
    ExternalDecays = cms.PSet(
        EvtGen130 = cms.untracked.PSet(
            decay_table = cms.string('GeneratorInterface/EvtGenInterface/data/DECAY_2014_NOLONGLIFE.DEC'),
            particle_property_file = cms.FileInPath('GeneratorInterface/EvtGenInterface/data/evt_2014.pdl'),
            list_forced_decays     = cms.vstring('MyB+','MyB-'),        
            operates_on_particles = cms.vint32(521, -521),
            convertPythiaCodes = cms.untracked.bool(False),
            user_decay_embedded= cms.vstring([
                # https://github.com/cms-data/GeneratorInterface-EvtGenInterface/blob/master/DECAY_2020_NOLONGLIFE.DEC
                # https://github.com/cms-data/GeneratorInterface-EvtGenInterface/blob/master/Bu_3munu.dec 
		'Alias      MyB+      B+',
		'Alias      MyB-      B-',
		'ChargeConj MyB-      MyB+',
                'Decay MyB+',
                '   1.000    mu+     mu-     mu+     nu_mu     PHSP;',
                'Enddecay',
                'CDecay MyB-',
                'End',
            ]),
        ),
        parameterSets = cms.vstring('EvtGen130')
    ),
    PythiaParameters = cms.PSet(
        pythia8CommonSettingsBlock,
        pythia8CP5SettingsBlock,
        processParameters = cms.vstring(
            'SoftQCD:nonDiffractive = on',
            'PTFilter:filter = on', # this turn on the filter
            'PTFilter:quarkToFilter = 5', # PDG id of q quark
            'PTFilter:scaleToFilter = 1.0',
		),
        parameterSets = cms.vstring(
            'pythia8CommonSettings',
            'pythia8CP5Settings',
            'processParameters',
        ),
    ),
)

_generator.PythiaParameters.processParameters.extend(EvtGenExtraParticles)
from GeneratorInterface.Core.ExternalGeneratorFilter import ExternalGeneratorFilter
generator = ExternalGeneratorFilter(_generator)

ThreeMuonFilter = cms.EDFilter(
    "MCMultiParticleFilter",
    NumRequired = cms.int32(3),
    AcceptMore  = cms.bool(True),
    ParticleID  = cms.vint32(13,-13),
    PtMin       = cms.vdouble(1.0),
    EtaMax      = cms.vdouble(2.5),
    Status      = cms.vint32(1),
)

OneNeutrinoFilter = cms.EDFilter(
    "MCMultiParticleFilter",
    NumRequired = cms.int32(1),
    AcceptMore  = cms.bool(True),
    ParticleID  = cms.vint32(14,-14),
    PtMin       = cms.vdouble(1.0),
    EtaMax      = cms.vdouble(2.5),
    Status      = cms.vint32(1),
)

ProductionFilterSequence = cms.Sequence(generator*ThreeMuonFilter*OneNeutrinoFilter)
