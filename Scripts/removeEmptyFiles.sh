#!/bin/bash
# This file is called . installKSTools.sh & NOT ./installKSTools.sh
#
RED="\\e[0;31m"
B_RED="\\e[1;31m"
GREEN="\\e[0;32m"
BLUE="\\e[0;34m"
NC="\\e[0m"
path0=$PWD
path0="/eos/project-c/cmsweb/www/egamma/validation/Electrons"
echo "== $path0"
folder="BasketList"

for path1 in Releases Test Dev
do
  echo $path0/$path1/$folder
  cd $path0/$path1/$folder
  echo -e "${BLUE}$path1${NC}"
  a=`find . -type f -name "basket*.txt"`
  i_rm=0
  i_ke=0
  for name in ${a[@]}
  do
    #echo $name
    if [ ! -s $name ] ; then
      rm $name
      echo "$path1 - $name removed "
      ((i_rm++))
    else
      echo -e "${B_RED}$path1 - $name${NC} not empty"
      ((i_ke++))
    fi
  done
  echo -e "${GREEN}$path1${NC} $i_rm files removed for basket"
  echo -e "${GREEN}$path1${NC} $i_ke files kept for basket"

  b=`find . -type f -name "shared*.txt"`
  i_rm=0
  i_ke=0
  for name in ${b[@]}
  do
    #echo $name
    if [ ! -s $name ] ; then
      rm $name
      echo "$path1 - $name removed "
      ((i_rm++))
    else
      echo -e "${B_RED}$ipath1 - $name${NC} not empty"
      ((i_ke++))
    fi
  done
  echo -e "${GREEN}$path1${NC} $i_rm files removed for shared"
  echo -e "${GREEN}$path1${NC} $i_ke files kept for shared"
  cd $path0
done
echo "end"
