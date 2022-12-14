#!/bin/bash
set -x
set -euo pipefail

DIR=$(dirname "0")

if [ $# -lt 1 ]; then
  echo "Usage: $(basename $0) INPUT [OUTPUT]"
  echo
  echo "Parse modlists copied from HTML, not the HTML itself"
  echo "Outputs to output.txt by default"
  exit 1
fi

input=$1
output=${2:-output.txt}

tempfile=$(mktemp)
sed 's/|/-/' $input | sed 's/Steam//' | sed 's/  /|/' | sed 's/http.*=//' > $tempfile
python3 $DIR/parse.py $tempfile $output
#rm $tempfile
