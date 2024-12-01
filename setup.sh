#!/bin/bash

# shellcheck disable=SC1091

PRJ_ROOT="/opt/AdventofCode/"
CURRENT_YEAR="2024"
CURR_DIR=$PRJ_ROOT/$CURRENT_YEAR

pfc.current_day () {
    local days
    days=$(ls -1 "$CURR_DIR" | grep -E '[0-9]+_day' | sort)
    echo "$days" | tail -n 1 | cut -d'_' -f1
}

pfc.next_day () {
    local current_day next_day
    current_day=$(pfc.current_day)
    next_day=$((current_day + 1))
    echo "$next_day"
}

pfc.mkday () {
    local day
    day=$(pfc.next_day)
    cp -r "$CURR_DIR/template/" "$CURR_DIR/${day}_day" || return 1
    echo "Copied templates to day $day"
}

pfc.cd () {
    local day
    day=$(pfc.current_day)
    cd "$CURR_DIR/${day}_day" || return 1
}


pfc () {
    cmd="$1"
    shift
    case "$cmd" in
        new)
            pfc.mkday
            ;;
        cd)
            pfc.cd
            ;;
        *)
            echo "Unknown command: $cmd"
            ;;
    esac
}


export -f pfc
export PYTHONPATH="$PYTHONPATH:$PRJ_ROOT/lib/"

RED_DOLLAR="\[\e[31;2m\]\$\[\e[0m\]"
GREEN_ARROW="\[\e[32;2m\]→\[\e[0m\]"
NEW_PROMP=" $RED_DOLLAR $GREEN_ARROW "

if [[ "$PS1" != "$NEW_PROMP" ]]; then
    export PS1="$NEW_PROMP"
fi

