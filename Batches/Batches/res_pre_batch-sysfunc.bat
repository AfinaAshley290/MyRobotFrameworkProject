echo off
echo *****************************************************************
echo Starting execution on node %COMPUTERNAME%
echo *****************************************************************
echo *****************************************************************
echo Setting-up environment variables for the tests
echo *****************************************************************
call ./set_env.bat
echo *****************************************************************
echo Starting the tests
echo *****************************************************************
call pybot %PybotParams% --reporttitle KYC --suitestatlevel 2  --RemoveKeywords WUKS --exclude TBD --exclude SKIP --tagstatexclude QC* --tagstatexclude AUTOASSIGNED --tagstatcombine C-KYC-* --tagstatcombine KYC-*  --include preconditions --outputdir ./results ./TestCases/KYC/B40_System_functions/Preconditions
echo *****************************************************************
echo Test run was done
echo *****************************************************************
