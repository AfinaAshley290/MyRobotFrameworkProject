echo off
echo *****************************************************************
echo Starting execution on %COMPUTERNAME%
echo *****************************************************************
echo *****************************************************************
echo Setting-up environment variables for the tests 
echo *****************************************************************
call ./set_env.bat
echo *****************************************************************
echo Starting the tests
echo *****************************************************************
call pybot %PybotParams% --dryrun --noncritical TBD --reporttitle KYC --suitestatlevel 2  --exclude preconditions --tagstatexclude FINAL_SWITCH --RemoveKeywords WUKS --tagstatexclude QC* --tagstatexclude AUTOASSIGNED --outputdir ./results ./TestCases/
echo *****************************************************************
echo Test run was done
echo *****************************************************************