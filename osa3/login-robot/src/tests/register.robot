*** Settings ***
Resource  resource.robot
Test Setup  Input New Command

*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  kalle  kalle123
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input Credentials  kalle  kalle123
    Output Should Contain  New user registered
    Input New Command
    Input Credentials  kalle  kalle123
    Output Should Contain  Username is already taken

Register With Too Short Username And Valid Password
    Input Credentials  ka  kalle123
    Output Should Contain  Username is too short

Register With Enough Long But Invalid Username And Valid Password
    Input Credentials  kall3  kalle123
    Output Should Contain  Invalid username

Register With Valid Username And Too Short Password
    Input Credentials  kalle  salasa
    Output Should Contain  Password is too short

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  kalle  kallekallekalle
    Output Should Contain  Password must contain numbers or special characters