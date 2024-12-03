#!/bin/bash

# shellcheck disable=SC1091

PRJ_ROOT="/opt/AdventofCode/"
BIN_DIR=$PRJ_ROOT/bin

pfc.java_template () {
    if [ -z "$1" ] || [ -z "$2" ] || [ -z "$3" ]; then
        echo "Usage: pfc.java_template <year> <day> <part>"
        return 1
    fi
    cat <<EOF
package _${1}.day${2};

public class Advent${1}Day${2}Part1 {
    public static void main(String[] args) {
        System.out.println("Advent of Code ${1} - Day ${2} - Part ${3}");
    }
}
EOF
}

pfc.mkday () {
    local lang year day
    lang="$1"
    year="$2"
    day="$3"

    if [ -z "$1" ] || [ -z "$2" ] || [ -z "$3" ]; then
        echo "Usage: pfc.mkday <python|java> <year:int> <day:int>"
    fi
    mkdir -p "$PRJ_ROOT/$year/$lang/${day}_day"
    echo "Creating day /$year/$lang/${day}_day"
}


pfc.new_python () {
    local year day
    year="$1"
    day="$2"
    if [ -z "$day" ]; then
        echo "Usage: pfc.new_python <day>"
        return 1
    fi
    cp -r "$PRJ_ROOT/$year/template/python" "$PRJ_ROOT/$year/python/${day}_day" || return 1
    echo "Creating day $day in $PRJ_ROOT/$year/python"
}

pfc.new_java () {
    local year day target part
    year="$1"
    day="$2"
    if [ -z "$day" ]; then
        echo "Usage: pfc.new_java <day>"
        return 1
    fi
    part="Advent${year}Day${day}Part"
    target="$PRJ_ROOT/$year/java/${day}_day"
    touch "$target/${part}1.java"
    touch "$target/${part}2.java"
    pfc.java_template "$year" "$day" "1" > "$target/${part}1.java"
    pfc.java_template "$year" "$day" "2" > "$target/${part}2.java"
    echo "Creating day $day in $year/java"
}

pfc.run_java () {
    local year day part target_class file_name
    year="$1"
    day="$2"
    part="$3"
    
    if [ -z "$year" ] || [ -z "$day" ] || [ -z "$part" ]; then
        echo "Usage: pfc.run_java <year> <day> <part>"
        return 1
    fi

    target_class="_${year}.day${day}.Advent${year}Day${day}Part${part}"
    file_name="Advent${year}Day${day}Part${part}.java"
    target_dir="$PRJ_ROOT/$year/java/${day}_day"

    javac -d "$PRJ_ROOT/bin" "$target_dir/$file_name"
    if ! java -cp "$PRJ_ROOT/bin" "$target_class"; then
        echo "Execution failed for $target_class"
    fi
}

pfc.new () {
    local lang year day
    lang="$1"
    year="$2"
    day="$3"
    shift
    pfc.mkday "$lang" "$year" "$day"
    case "$lang" in
        python)
            pfc.new_python "$@"
            ;;
        java)
            pfc.new_java "$@"
            ;;
        *)
            echo "Unknown language: '$lang'"
            echo "Usage: pfc.new <python|java> <year> <day>"
            ;;
    esac
}

pfc.run () {
    local lang year day part
    lang="$1"
    year="$2"
    day="$3"
    part="$4"
    shift
    case "$lang" in
        java)
            pfc.run_java "$@"
            ;;
        *)
            echo "Unknown language: '$lang'"
            ;;
    esac
}

pfc () {
    cmd="$1"
    shift
    case "$cmd" in
        new)
            pfc.new "$@"
            ;;
        run)
            pfc.run "$@"
            ;;
        *)
            echo "Unknown command: '$cmd'"
            ;;
    esac
}


export -f pfc
export PYTHONPATH="$PYTHONPATH:$PRJ_ROOT/lib/"
