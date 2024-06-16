#!/bin/bash
echo
echo =-=-=-=-=-=
echo
echo "Hi AASS Engine Dev!"
echo "Speed-running the Website huh?"
echo "Good luck!"
echo "Usefull ONLY if you are adjusting or changing SCSS"
echo
echo =-=-=-=-=-=
echo

# Yep, easy auto watch SCSS script
sass --watch scss/main_style.scss:css/main_style.css &

wait
