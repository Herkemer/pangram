#!/bin/bash

APIBASE=http://localhost:8080/pangram

rawurlencode() {
  local string="${1}"
  local strlen=${#string}
  local encoded=""
  local pos c o

  for (( pos=0 ; pos<strlen ; pos++ )); do
     c=${string:$pos:1}
     case "$c" in
        [-_.~a-zA-Z0-9] ) o="${c}" ;;
        * )               printf -v o '%%%02x' "'$c"
     esac
     encoded+="${o}"
  done
  echo "${encoded}"    # You can either set a return variable (FASTER) 
  REPLY="${encoded}"   #+or echo the result (EASIER)... or both... :p
}

while IFS='' read -r line || [[ -n "$line" ]]; do
    echo "Test: $line"
    encoded=$( rawurlencode "$line" )
    echo "Encoded: $encoded"
    curl --silent --url "${APIBASE}/${encoded}" | jq .
    echo ""
done < "$1"
