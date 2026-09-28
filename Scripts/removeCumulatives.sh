#!/bin/bash
# This file is called . installKSTools.sh & NOT ./installKSTools.sh
#

aa=$(pwd)
cd /eos/project/c/cmsweb/www/egamma/validation/Electrons/Store/KS_Curves
a=`find . -type f -name "cumu*.png"`
for name in ${a[@]}
do
  echo $name
  rm $name
  #sed -i -e 's/9000\/CMSSW_12_1_0_pre5/9000/g' $name

done
cd $aa

echo "end"

