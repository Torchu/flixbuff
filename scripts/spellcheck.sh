# Comprueba que los ficheros estén escritos correctamente

#!/bin/bash
SpellingError () {
    error=0;
    echo "";
    echo "Checking file" $1":";
    n_line=1;
    while IFS= read -r line
    do
        resultado=$(echo $line | aspell --mode=tex  --lang=en --list | aspell --mode=tex  --lang=es --list --home-dir=. --personal=.github/actions/check-spelling/allowed_words.txt);
        if [[ ! -z "$resultado" ]]
        then
         echo "Spell error in line $n_line : $resultado"
         let "error = 1";
        fi
        let "n_line += 1"
    done < $1
    return $error;
}
export -f SpellingError;
exitValue=0

# Check ReadMe.md
SpellingError README.md
let "exitValue += $?"

# Check portada
for file in $(find ./doc/portada -name "*.tex")
do
    SpellingError $file
    let "exitValue += $?"
done

# Check prefacios
for file in $(find ./doc/prefacios -name "*.tex")
do
    SpellingError $file
    let "exitValue += $?"
done

# Check secciones
for file in $(find ./doc/secciones -name "*.tex")
do
    SpellingError $file
    let "exitValue += $?"
done

exit $exitValue