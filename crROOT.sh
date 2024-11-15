#!/bin/sh
# This file is called ./zee_flow.sh for CCA computers.
###################
## CCA computers ##
###################

#nb=1
#chemin='/afs/cern.ch/work/a/archiron/private/PR_place/CMSSW_14_1_0_pre6-inf/src/Validation/RecoEgamma/test'
chemin='/home/llr/info/chiron_u/TESTS/CMSSW_14_1_0_pre6-inf/src/Validation/RecoEgamma/test'
nb_evts=3000 #9000
result_folder=$chemin
initialSEED=0.
echo "nb : $nb"
echo "chemin : $chemin"
echo "nb evts : $nb_evts"
echo "result folder : $result_folder"
echo "initial SEED : $initialSEED"
echo ""

LOG_SOURCE=$2
echo "Step 1 in : $LOG_SOURCE"

name1="step1_$(printf "%04d" $nb_evts)_$(printf "%03d" $nb).root"
name2="step2_$(printf "%04d" $3)_$(printf "%03d" $1).root"
name31="step3_$(printf "%04d" $3)_$(printf "%03d" $1).root"
name32="step3_inDQM_$(printf "%04d" $3)_$(printf "%03d" $1).root"
name33="step3_inMINIAODSIM_$(printf "%04d" $3)_$(printf "%03d" $1).root"
#name34="step3_inNANOEDMAODSIM_$(printf "%04d" $3)_$(printf "%03d" $1).root"

echo "name1 :  $name1"
echo "name2 :  $name2"
echo "name31 :  $name31"
echo "name32 :  $name32"
echo "name33 :  $name33"
#echo "name34 :  $name34"

cd $chemin
eval `scramv1 runtime -sh`
cd -

#time cmsRun $chemin/step1.py $nb $chemin $nb_evts $result_folder 

#for nb in {1..3} 
#    do
#        time cmsRun $chemin/step2.py $nb $chemin $nb_evts $result_folder > ~/out$nb.log 2>&1 &
#        sleep 30s # Waits 30 secondes.
#    done
#rm $4/$name1

nb=1
time cmsRun $chemin/step3.py $nb $chemin $nb_evts $result_folder 
#rm $4/$name2

#time cmsRun $chemin/step4.py $nb $chemin $nb_evts $result_folder 
#rm $4/$name31
#rm $4/$name32
#rm $4/$name33
#rm $4/$name34
