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
call pybot %PybotParams% --reporttitle KYC --suitestatlevel 2  --RemoveKeywords WUKS --exclude TBD --exclude SKIP --tagstatexclude QC* --tagstatexclude AUTOASSIGNED --tagstatcombine C-KYC-* --tagstatcombine KYC-*  --exclude group_1  --exclude group_2  --exclude group_3  --include group_4 --exclude group_5 --outputdir ./results ./TestCases/KYC/2eyes/B01_Submission2eyes
echo *****************************************************************
echo Test run was done
echo *****************************************************************
