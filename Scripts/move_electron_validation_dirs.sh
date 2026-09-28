#!/bin/bash

TGT=10_3_0_pre2
REF=10_3_0_pre1

MINIAOD_DIR=${TGT}_miniAOD_DQM_std/GedvsGed_${TGT}_miniAOD_DQM_std
PMX_DIR=${TGT}_pmx_DQM_std/GedvsGed_${TGT}_pmx_DQM_std
RECO_DIR=${TGT}_DQM_std/GedvsGed_${REF}_DQM_std

# Move miniAOD
mkdir -p $MINIAOD_DIR
mv ${TGT}_DQM_std/FullvsFull_${TGT}/RECO-miniAOD_SingleElectronPt10 $MINIAOD_DIR/Fullgedvsged_RelValSingleElectronPt10_gedGsfE_Startup
mv ${TGT}_DQM_std/FullvsFull_${TGT}/RECO-miniAOD_TTbar_13 $MINIAOD_DIR/Fullgedvsged_RelValTTbar_13_gedGsfE_Startup
mv ${TGT}_DQM_std/FullvsFull_${TGT}/RECO-miniAOD_ZEE_13 $MINIAOD_DIR/Fullgedvsged_RelValZEE_13_gedGsfE_Startup

## Move PMX
#mkdir -p $PMX_DIR
#mv ${TGT}_DQM_std/FullvsFull_${TGT}/PUpmx25-PU25_TTbar_13 $PMX_DIR/PUpmx25ns_RelValTTbar_13_gedGsfE_Startup
#mv ${TGT}_DQM_std/FullvsFull_${TGT}/PUpmx25-PU25_ZEE_13 $PMX_DIR/PUpmx25ns_RelValZEE_13_gedGsfE_Startup

## Move RECO
#mkdir -p $RECO_DIR
#mv ${TGT}_DQM_std/FullvsFull_${REF}/PU25-PU25_TTbar_13 $RECO_DIR/PU25ns_RelValTTbar_13_gedGsfE_Startup
#mv ${TGT}_DQM_std/FullvsFull_${REF}/PU25-PU25_ZEE_13 $RECO_DIR/PU25ns_RelValZEE_13_gedGsfE_Startup
#mv ${TGT}_DQM_std/FullvsFull_${REF}/RECO-RECO_QCD_Pt_80_120_13 $RECO_DIR/Fullgedvsged_RelValQCD_Pt_80_120_13_gedGsfE_Startup
#mv ${TGT}_DQM_std/FullvsFull_${REF}/RECO-RECO_SingleElectronPt10 $RECO_DIR/Fullgedvsged_RelValSingleElectronPt10_gedGsfE_Startup
#mv ${TGT}_DQM_std/FullvsFull_${REF}/RECO-RECO_SingleElectronPt1000 $RECO_DIR/Fullgedvsged_RelValSingleElectronPt1000_gedGsfE_Startup
#mv ${TGT}_DQM_std/FullvsFull_${REF}/RECO-RECO_SingleElectronPt35 $RECO_DIR/Fullgedvsged_RelValSingleElectronPt35_gedGsfE_Startup
#mv ${TGT}_DQM_std/FullvsFull_${REF}/RECO-RECO_TTbar_13 $RECO_DIR/Fullgedvsged_RelValTTbar_13_gedGsfE_Startup
#mv ${TGT}_DQM_std/FullvsFull_${REF}/RECO-RECO_ZEE_13 $RECO_DIR/Fullgedvsged_RelValZEE_13_gedGsfE_Startup
