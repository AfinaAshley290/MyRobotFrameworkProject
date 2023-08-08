del *.html

python -m robot.testdoc -T Functional_tests  -e TBC -e preconditions  ./TestCases ATS_Functional.html

python -m robot.testdoc -N All ./TestCases ATS_ALL.html
