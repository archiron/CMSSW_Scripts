#!/bin/bash

#Black        0;30     Dark Gray     1;30
#Red          0;31     Light Red     1;31
#Green        0;32     Light Green   1;32
#Brown/Orange 0;33     Yellow        1;33
#Blue         0;34     Light Blue    1;34
#Purple       0;35     Light Purple  1;35
#Cyan         0;36     Light Cyan    1;36
#Light Gray   0;37     White         1;37
B_BLUE="\\e[1;34m"
B_GREEN="\033[1;32m"
RED='\033[0;31m'
BLUE='\033[0;34m'
GREEN='\033[0;32m'

NC='\033[0m' # No Color

LOG_DEST=/eos/cms/store/group/phys_egamma/ElectronValidationArchives/attic
cd /eos/project-c/cmsweb/www/egamma/validation/Electrons/Releases

a=($(ls -d */))
i=0
for item in "${a[@]}"
do
  name=${item::-1}
  echo -e "=== ${B_BLUE}$name${NC}"
  if [[ -f $name ]];
  then
    b=2
  elif [[ -d $name ]];
  then
    firstchar=${name:0:3}
    if [[ $firstchar == "12_" ]];
    then
      printf "%2s - %s\n" "$(($i+1))" "$name"
      dest=${name::-1}.tar.gz
      chmod 766 $name/
      tar -czf $dest $name/
      mv $dest $LOG_DEST/$dest
      ((i=i+1))
    fi
  else
    echo "$name is not a directory nor a file"  
  fi
done

cd /eos/user/a/archiron/Scripts


