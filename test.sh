#!/bin/bash

run_command="python3 main.py"
test_folder="tests"

declare -a file_base=("t01" "t02" "t03" "t04" "t05" "t06" "t07" "t08" "t09" "t10" "t11" "t12" "t13" "t14" "t15" "t16")

for file in "${file_base[@]}"; do
    file_in="${test_folder}/${file}.ttp"
    file_out="${test_folder}/${file}.out"
    file_out_test="${test_folder}/${file}.out.test"

    echo "Running test for ${file_in}"
    SECONDS=0    
    $run_command < $file_in > $file_out_test

    if diff $file_out $file_out_test; then
        duration=$SECONDS
        echo "Test passed after $((duration / 60))m $((duration % 60))s"
    else
        echo "Test failed"
    fi

done