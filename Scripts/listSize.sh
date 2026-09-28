#!/bin/bash

LOG_DEST=/eos/cms/store/group/phys_egamma/ElectronValidationArchives/attic

a=($(ls -d */))
i=0
for item in "${a[@]}"
do
  name=${item::-1}
  #echo "$name\n"
  b=`du -sh $name`
  printf "%2s - %s\n" "$(($i+1))" "$b"
  ((i=i+1))
done


