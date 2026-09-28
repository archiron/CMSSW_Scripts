#!/bin/bash

LOG_DEST=/eos/cms/store/group/phys_egamma/ElectronValidationArchives/attic

#a=`ls`
a=($(ls -d */))
i=0
for name in "${a[@]}"
do
  #echo "$name\n"
  printf "%2s-%s\n" "$(($i+1))" "$name"
  ((i=i+1))
done


