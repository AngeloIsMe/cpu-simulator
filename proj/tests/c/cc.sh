"/cygdrive/c/Users/thelink2012/projects/lcc/build/lcc.exe" "$@" -target=rpis/le -S && cat "C:/Users/thelink2012/projects/rpis-cpu/Project-I/tests/c/crt.s" "${@%%.*}.asm" >"$TMP/_rpis_cc.asm" && py -2 ../../assembler.py "$(cygpath -w $TMP/_rpis_cc.asm)" -o "${1%%.*}.hex"