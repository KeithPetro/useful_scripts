#!/bin/bash

#Usage: ./chrome_session_reader.sh INPUT_FILE OUTPUT_FILE

file=$1

strings "$1" | grep -o 'http.*' > $2
