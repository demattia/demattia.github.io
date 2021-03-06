import FWCore.ParameterSet.Config as cms

process = cms.Process("Reader")

process.MessageLogger = cms.Service("MessageLogger",
    debugModules = cms.untracked.vstring('cout'),
    threshold = cms.untracked.string('INFO'),
    destinations = cms.untracked.vstring('cout') #Reader.log, cout
)

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(-1)
)

process.source = cms.Source("EmptyIOVSource",
    firstValue = cms.uint64(111673),
    lastValue = cms.uint64(111673),
    timetype = cms.string('runnumber'),
    interval = cms.uint64(1)
)

process.poolDBESSource = cms.ESSource("PoolDBESSource",
   BlobStreamerName = cms.untracked.string('TBufferBlobStreamingService'),
   DBParameters = cms.PSet(
        messageLevel = cms.untracked.int32(2),
        authenticationPath = cms.untracked.string('/afs/cern.ch/cms/DB/conddb')
    ),
    timetype = cms.untracked.string('runnumber'),
    connect = cms.string('sqlite_file:../dbfile.db'),
    toGet = cms.VPSet(cms.PSet(
        record = cms.string('SiStripPedestalsRcd'),
        tag = cms.string('SiStripPedestals_FromDQM_V1')
    ))
)

process.DQMStore = cms.Service("DQMStore",
    referenceFileName = cms.untracked.string(''),
    verbose = cms.untracked.int32(1)
)

process.load("DQM.SiStripMonitorSummary.SiStripMonitorCondData_cfi")

process.CondDataMonitoring.OutputFileName = 'SiStripPedestals_GR09_31X_v1_hlt_Run_111673.root'
process.CondDataMonitoring.MonitorSiStripPedestal      = True
process.CondDataMonitoring.MonitorSiStripNoise         = False
process.CondDataMonitoring.MonitorSiStripQuality       = False
process.CondDataMonitoring.MonitorSiStripCabling       = False
process.CondDataMonitoring.MonitorSiStripApvGain       = False
process.CondDataMonitoring.MonitorSiStripLorentzAngle  = False
process.CondDataMonitoring.MonitorSiStripLowThreshold  = False
process.CondDataMonitoring.MonitorSiStripHighThreshold = False
process.CondDataMonitoring.OutputMEsInRootFile         = True
process.CondDataMonitoring.FillConditions_PSet.OutputSummaryAtLayerLevelAsImage           = True
process.CondDataMonitoring.FillConditions_PSet.OutputSummaryProfileAtLayerLevelAsImage    = False # This should be saved only in case of LA (because for LA no SummaryAtLayerLevel is available)
process.CondDataMonitoring.FillConditions_PSet.OutputCumulativeSummaryAtLayerLevelAsImage = False
process.CondDataMonitoring.FillConditions_PSet.HistoMaps_On     = False
process.CondDataMonitoring.FillConditions_PSet.TkMap_On         = True # This is just for test until TkMap is included in all classes!!! Uncomment!!!!
process.CondDataMonitoring.FillConditions_PSet.ActiveDetIds_On  = True # This should be set to False only for Lorentz Angle

process.CondDataMonitoring.SiStripPedestalsDQM_PSet.FillSummaryAtLayerLevel     = True
process.CondDataMonitoring.SiStripNoisesDQM_PSet.FillSummaryAtLayerLevel        = True
process.CondDataMonitoring.SiStripQualityDQM_PSet.FillSummaryAtLayerLevel       = True
process.CondDataMonitoring.SiStripApvGainsDQM_PSet.FillSummaryAtLayerLevel      = True
process.CondDataMonitoring.SiStripLowThresholdDQM_PSet.FillSummaryAtLayerLevel  = True
process.CondDataMonitoring.SiStripHighThresholdDQM_PSet.FillSummaryAtLayerLevel = True

process.CondDataMonitoring.SiStripCablingDQM_PSet.CondObj_fillId       = 'ProfileAndCumul'
process.CondDataMonitoring.SiStripPedestalsDQM_PSet.CondObj_fillId     = 'onlyProfile'
process.CondDataMonitoring.SiStripNoisesDQM_PSet.CondObj_fillId        = 'onlyCumul'
process.CondDataMonitoring.SiStripQualityDQM_PSet.CondObj_fillId       = 'onlyProfile'
process.CondDataMonitoring.SiStripApvGainsDQM_PSet.CondObj_fillId      = 'ProfileAndCumul'
process.CondDataMonitoring.SiStripLorentzAngleDQM_PSet.CondObj_fillId  = 'ProfileAndCumul'
process.CondDataMonitoring.SiStripLowThresholdDQM_PSet.CondObj_fillId  = 'onlyProfile'
process.CondDataMonitoring.SiStripHighThresholdDQM_PSet.CondObj_fillId = 'onlyProfile'

## --- TkMap specific Configurable options:

process.CondDataMonitoring.SiStripCablingDQM_PSet.TkMap_On     = True
process.CondDataMonitoring.SiStripCablingDQM_PSet.TkMapName    = 'CablingTkMap.png'
process.CondDataMonitoring.SiStripCablingDQM_PSet.minValue     = 0.
process.CondDataMonitoring.SiStripCablingDQM_PSet.maxValue     = 6.

process.CondDataMonitoring.SiStripPedestalsDQM_PSet.TkMap_On     = True
process.CondDataMonitoring.SiStripPedestalsDQM_PSet.TkMapName    = 'PedestalTkMap.png'
process.CondDataMonitoring.SiStripPedestalsDQM_PSet.minValue     = 0.
process.CondDataMonitoring.SiStripPedestalsDQM_PSet.maxValue     = 400.

process.CondDataMonitoring.SiStripNoisesDQM_PSet.TkMap_On     = True
process.CondDataMonitoring.SiStripNoisesDQM_PSet.TkMapName    = 'NoiseTkMap.png'
process.CondDataMonitoring.SiStripNoisesDQM_PSet.minValue     = 3.
process.CondDataMonitoring.SiStripNoisesDQM_PSet.maxValue     = 9.

process.CondDataMonitoring.SiStripApvGainsDQM_PSet.TkMap_On     = True
process.CondDataMonitoring.SiStripApvGainsDQM_PSet.TkMapName    = 'GainTkMap.png'
process.CondDataMonitoring.SiStripApvGainsDQM_PSet.minValue     = 0.
process.CondDataMonitoring.SiStripApvGainsDQM_PSet.maxValue     = 1.5

process.CondDataMonitoring.SiStripLorentzAngleDQM_PSet.TkMap_On     = True
process.CondDataMonitoring.SiStripLorentzAngleDQM_PSet.TkMapName    = 'LorentzAngleTkMap.png'
process.CondDataMonitoring.SiStripLorentzAngleDQM_PSet.minValue     = 0.01
process.CondDataMonitoring.SiStripLorentzAngleDQM_PSet.maxValue     = 0.03

process.CondDataMonitoring.SiStripLowThresholdDQM_PSet.TkMap_On     = True
process.CondDataMonitoring.SiStripLowThresholdDQM_PSet.TkMapName     = 'LowThresholdTkMap.png'
process.CondDataMonitoring.SiStripLowThresholdDQM_PSet.minValue     = 0.
process.CondDataMonitoring.SiStripLowThresholdDQM_PSet.maxValue     = 10.

process.CondDataMonitoring.SiStripHighThresholdDQM_PSet.TkMap_On     = True
process.CondDataMonitoring.SiStripHighThresholdDQM_PSet.TkMapName     = 'HighThresholdTkMap.png'
process.CondDataMonitoring.SiStripHighThresholdDQM_PSet.minValue     = 0.
process.CondDataMonitoring.SiStripHighThresholdDQM_PSet.maxValue     = 10.


process.p1 = cms.Path(process.CondDataMonitoring)
