#!/bin/sh
# This file is called ./zee_flow.sh for CCA computers.
###################
## CCA computers ##
###################

#chemin='/afs/cern.ch/work/a/archiron/private/PR_place/CMSSW_14_1_0_pre6-inf/src/Validation/RecoEgamma/test' # CERN path
chemin='/home/llr/info/chiron_u/TESTS/CMSSW_14_1_0_pre6-inf/src/Validation/RecoEgamma/test' # LLR path
nb_evts=3000 #9000
result_folder=$chemin # where you want the results files will be located.
initialSEED=0.

echo "nb evts : $nb_evts"
echo "chemin : $chemin"
echo "result folder : $result_folder"
echo "initial SEED : $initialSEED"
echo ""

name1="step1_$(printf "%04d" $nb_evts)_$(printf "%03d" $nb).root"
name2="step2_$(printf "%04d" $3)_$(printf "%03d" $1).root"
name31="step3_$(printf "%04d" $3)_$(printf "%03d" $1).root"
name32="step3_inDQM_$(printf "%04d" $3)_$(printf "%03d" $1).root"
name33="step3_inMINIAODSIM_$(printf "%04d" $3)_$(printf "%03d" $1).root"
name34="step3_inNANOEDMAODSIM_$(printf "%04d" $3)_$(printf "%03d" $1).root"

cd $chemin
eval `scramv1 runtime -sh`
cd -

## NOTE
## the command time is not necessary if you do not want time stats.
## the rm commands are used if you does not need previous files.

time cmsRun $chemin/step1.py $nb $chemin $nb_evts $result_folder > ~/outStep1_$nb.log 2>&1 &

## if you want the step2 result ROOT file will be into 3 parts
#for nb in {1..3} 
#    do
#        time cmsRun $chemin/step2.py $nb $chemin $nb_evts $result_folder > ~/outStep2_$nb.log 2>&1 &
#        sleep 30s # Waits 30 secondes.
#    done

#rm $result_folder/$name1

nb=1
echo "nb : $nb"

## if you want the step2 result ROOT file will be into 1 part
time cmsRun $chemin/step2.py $nb $chemin $nb_evts $result_folder > ~/outStep2_$nb.log 2>&1 &

time cmsRun $chemin/step3.py $nb $chemin $nb_evts $result_folder > ~/outStep3_$nb.log 2>&1 &
#rm $result_folder/$name2

#time cmsRun $chemin/step4.py $nb $chemin $nb_evts $result_folder  > ~/outStep4_$nb.log 2>&1 &
#rm $result_folder/$name31
#rm $result_folder/$name32
#rm $result_folder/$name33
#rm $result_folder/$name34
