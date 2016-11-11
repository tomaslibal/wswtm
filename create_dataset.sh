#!/usr/bin/env bash

processdir() {
    dir=$1
    class_label=$(basename $dir)

    echo "processing images in ${dir}"
    echo "using class ${class_label}"

    for f in $dir/*.jpg ; do
        python src/python/add.py ${f} --labels=${class_label}
    done
}

backup_existing() {
    out_file=$1
    timestamp=$(date +"%s")

    if [ -f ${out_file} ]; then
        mv ${out_file} ${out_file}.${timestamp}.bak
    fi
}

target_dir=$1
target_dir=${target_dir:="/mnt/images/classes"}
out_file="resources/images/training.csv"

backup_existing $out_file

for d in ${target_dir}/*/ ; do
    processdir $d
done
