cd ./sources
call set_env.bat
cd ..
call pybot %PybotParams%  --reporttitle KYC --suitestatlevel 2 --exclude TBD --outputdir ./results ./sources/Testcases