#!/bin/bash

case "$1" in

  build_generator)
    docker build -t mountain-generator ./generator
    ;;

  run_generator)
    mkdir -p data
    docker run --rm -v "$(pwd)/data:/data" mountain-generator
    ;;

  build_reporter)
    docker build -t mountain-reporter ./reporter
    ;;

  run_reporter)
    mkdir -p data
    docker run --rm -v "$(pwd)/data:/data" mountain-reporter
    ;;

  clear_data)
    rm -f data/*.csv
    rm -f data/*.html
    ;;

  structure)
    find . -not -path "./.git/*"
    ;;

  *)
    echo "Commands:"
    echo "build_generator"
    echo "run_generator"
    echo "build_reporter"
    echo "run_reporter"
    echo "clear_data"
    echo "structure"
    ;;

esac