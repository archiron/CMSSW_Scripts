#!/bin/bash

a=($(ls -d */))
i=0
for item in "${a[@]}"
do
  name=${item::-1}
  if [[ -f $name ]];
  then
    #echo "$name is a file"
    b=2
  elif [[ -d $name ]];
  then
    firstchar=${name:0:4}
    if [[ $firstchar == "10_6" ]];
    then
      #echo "$name is a directory"
      printf "%2s - %s\n" "$(($i+1))" "$name"
      rm -rf $name
      ((i=i+1))
    fi
  else
    echo "$name is not a directory nor a file"  
  fi
done

