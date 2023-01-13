*** Settings ***
Library           SeleniumLibrary

*** Variables ***
${RESOURCE URL}      http://localhost:5000/resource
${DIRECTORY URL}      http://localhost:5000/directory
${BINARYFILE URL}      http://localhost:5000/binaryfile
${LOGTEXTFILE URL}      http://localhost:5000/logtextfile
${BUFFERFILE URL}      http://localhost:5000/bufferfile
${BROWSER}        Chrome

*** Test Cases ***
Valid Resource Input Directory
    Open Browser To Resource Page
    Input Resource    directory
    Submit Credentials
    Directory Page Should Be Open
    [Teardown]    Close Browser

Valid Resource Input BinaryFile
    Open Browser To Resource Page
    Input Resource    binaryfile
    Submit Credentials
    BinaryFile Page Should Be Open
    [Teardown]    Close Browser

Valid Resource Input LogTextFile
    Open Browser To Resource Page
    Input Resource    logtextfile
    Submit Credentials
    LogTextFile Page Should Be Open
    [Teardown]    Close Browser

Valid Resource Input BufferFile
    Open Browser To Resource Page
    Input Resource    bufferfile
    Submit Credentials
    BufferFile Page Should Be Open
    [Teardown]    Close Browser

Valid Directory Creation
    Open Browser To Directory
    Input Directory    create
    Submit Credentials
    Create Page Should Be Open
    Input Create Directory    dir1   20    root
    Submit Credentials
    Page Should Contain    Added successfully dir1 in root
    Open Browser To Directory
    Input Directory    create
    Submit Credentials
    Create Page Should Be Open
    Input Create Directory    dir2   20    root
    Submit Credentials
    Page Should Contain    Added successfully dir2 in root
    [Teardown]    Close Browser

Valid Directory Move
    Open Browser To Directory
    Input Directory    move
    Submit Credentials
    Move Page Should Be Open
    Input Move Directory    root/dir2   root/dir1
    Submit Credentials
    Page Should Contain    Moved successfully into dir1
    [Teardown]    Close Browser

Valid Directory Delete
    Open Browser To Directory
    Input Directory    delete
    Submit Credentials
    Delete Page Should Be Open
    Input Delete Directory    root/dir1/dir2
    Submit Credentials
    Page Should Contain    Deleted
    [Teardown]    Close Browser

Valid BinaryFile Creation
    Open Browser To BinaryFile
    Input BinaryFile    create
    Submit Credentials
    Create Page Should Be Open
    Input Create BinaryFile    binf1   this is the content    root
    Submit Credentials
    Page Should Contain    Added successfully binf1 in root
    Open Browser To BinaryFile
    Input BinaryFile    create
    Submit Credentials
    Create Page Should Be Open
    Input Create BinaryFile    binf2   this is the content of binf2    root/dir1
    Submit Credentials
    Page Should Contain    Added successfully binf2 in dir1
    [Teardown]    Close Browser

Valid BinaryFile Move
    Open Browser To BinaryFile
    Input BinaryFile    move
    Submit Credentials
    Move Page Should Be Open
    Input Move BinaryFile    root/binf1   root/dir1
    Submit Credentials
    Page Should Contain    Moved successfully into dir1
    [Teardown]    Close Browser

Valid BinaryFile Read
    Open Browser To BinaryFile
    Input BinaryFile    read
    Submit Credentials
    Read Page Should Be Open
    Input Read BinaryFile    root/dir1/binf1
    Submit Credentials
    Page Should Contain    this is the content
    [Teardown]    Close Browser

Valid BinaryFile Delete
    Open Browser To BinaryFile
    Input BinaryFile    delete
    Submit Credentials
    Delete Page Should Be Open
    Input Delete BinaryFile    root/dir1/binf2
    Submit Credentials
    Page Should Contain    Deleted
    [Teardown]    Close Browser

Valid LogTextFile Creation
    Open Browser To LogTextFile
    Input LogTextFile    create
    Submit Credentials
    Create Page Should Be Open
    Input Create LogTextFile    logtf1   this is the content    root
    Submit Credentials
    Page Should Contain    Added successfully logtf1 in root
    Open Browser To LogTextFile
    Input LogTextFile    create
    Submit Credentials
    Create Page Should Be Open
    Input Create LogTextFile    logtf2   this is the content of logtf2    root/dir1
    Submit Credentials
    Page Should Contain    Added successfully logtf2 in dir1
    [Teardown]    Close Browser

Valid LogTextFile Move
    Open Browser To LogTextFile
    Input LogTextFile    move
    Submit Credentials
    Move Page Should Be Open
    Input Move LogTextFile    root/logtf1   root/dir1
    Submit Credentials
    Page Should Contain    Moved successfully into dir1
    [Teardown]    Close Browser

Valid LogTextFile Read
    Open Browser To LogTextFile
    Input LogTextFile    read
    Submit Credentials
    Read Page Should Be Open
    Input Read LogTextFile    root/dir1/logtf1
    Submit Credentials
    Page Should Contain    this is the content
    [Teardown]    Close Browser

Valid LogTextFile Append
    Open Browser To LogTextFile
    Input LogTextFile    append
    Submit Credentials
    Append Page Should Be Open
    Input Append LogTextFile    this is the line    root/dir1/logtf1
    Submit Credentials
    Page Should Contain    Line was added successfully
    [Teardown]    Close Browser

Valid LogTextFile Delete
    Open Browser To LogTextFile
    Input LogTextFile    delete
    Submit Credentials
    Delete Page Should Be Open
    Input Delete LogTextFile    root/dir1/logtf2
    Submit Credentials
    Page Should Contain    Deleted
    [Teardown]    Close Browser

Valid BufferFile Creation
    Open Browser To BufferFile
    Input BufferFile    create
    Submit Credentials
    Create Page Should Be Open
    Input Create BufferFile    buf1   20    root
    Submit Credentials
    Page Should Contain    Added successfully buf1 in root
    Open Browser To BufferFile
    Input BufferFile    create
    Submit Credentials
    Create Page Should Be Open
    Input Create BufferFile    buf2   20    root/dir1
    Submit Credentials
    Page Should Contain    Added successfully buf2 in dir1
    [Teardown]    Close Browser

Valid BufferFile Move
    Open Browser To BufferFile
    Input BufferFile    move
    Submit Credentials
    Move Page Should Be Open
    Input Move BufferFile    root/buf1   root/dir1
    Submit Credentials
    Page Should Contain    Moved successfully into dir1
    [Teardown]    Close Browser

Valid BufferFile Push
    Open Browser To BufferFile
    Input BufferFile    push
    Submit Credentials
    Push Page Should Be Open
    Input Push BufferFile    this is the element    root/dir1/buf1
    Submit Credentials
    Page Should Contain    Pushed successfully
    [Teardown]    Close Browser

Valid BufferFile Consume
    Open Browser To BufferFile
    Input BufferFile    consume
    Submit Credentials
    Consume Page Should Be Open
    Input Consume BufferFile    root/dir1/buf1
    Submit Credentials
    Page Should Contain    Consumed successfully
    [Teardown]    Close Browser

Valid BufferFile Delete
    Open Browser To BufferFile
    Input BufferFile    delete
    Submit Credentials
    Delete Page Should Be Open
    Input Delete BufferFile    root/dir1/buf2
    Submit Credentials
    Page Should Contain    Deleted
    [Teardown]    Close Browser

Valid Directory Display
    Open Browser To Directory
    Input Directory    display
    Submit Credentials
    Display Page Should Be Open
    Input Display Directory    root
    Submit Credentials
    Page Should Contain    [root - dir: [dir1 - file: binf1 - file: logtf1 - file: buf1]]
    # [Teardown]    Close Browser

*** Keywords ***

# tests with opening resources
Open Browser To Resource Page
    Open Browser    ${RESOURCE URL}    ${BROWSER}
    Title Should Be    Resource

Input Resource
    [Arguments]    ${res}
    Input Text    res    ${res}

Submit Credentials
    Click Button    Submit

Directory Page Should Be Open
    Title Should Be    Directory

BinaryFile Page Should Be Open
    Title Should Be    BinaryFile

LogTextFile Page Should Be Open
    Title Should Be    LogTextFile

BufferFile Page Should Be Open
    Title Should Be    BufferFile

# interaction with directory
Open Browser To Directory
    Open Browser    ${DIRECTORY URL}    ${BROWSER}
    Title Should Be    Directory

Input Directory
    [Arguments]    ${res}
    Input Text    res    ${res}

Create Page Should Be Open
    Title Should Be    Create

Input Create Directory
    [Arguments]    ${name}    ${max_size}    ${parent}
    Input Text    name    ${name}
    Input Text    max_size    ${max_size}
    Input Text    parent    ${parent}

Move Page Should Be Open
    Title Should Be    Move

Input Move Directory
    [Arguments]    ${path}    ${new_parent}
    Input Text    path    ${path}
    Input Text    new_parent    ${new_parent}

Display Page Should Be Open
    Title Should Be    Display

Input Display Directory
    [Arguments]    ${name}
    Input Text    name    ${name}

Delete Page Should Be Open
    Title Should Be    Delete

Input Delete Directory
    [Arguments]    ${path}
    Input Text    path    ${path}

# interaction with binaryfile
Open Browser To BinaryFile
    Open Browser    ${BINARYFILE URL}    ${BROWSER}
    Title Should Be    BinaryFile

Input BinaryFile
    [Arguments]    ${res}
    Input Text    res    ${res}

Input Create BinaryFile
    [Arguments]    ${name}    ${content}    ${parent}
    Input Text    name    ${name}
    Input Text    content    ${content}
    Input Text    parent    ${parent}

Input Move BinaryFile
    [Arguments]    ${path}    ${new_parent}
    Input Text    path    ${path}
    Input Text    new_parent    ${new_parent}

Read Page Should Be Open
    Title Should Be    Read

Input Read BinaryFile
    [Arguments]    ${path}
    Input Text    path    ${path}

Input Delete BinaryFile
    [Arguments]    ${path}
    Input Text    path    ${path}

# interaction with logtextfile
Open Browser To LogTextFile
    Open Browser    ${LOGTEXTFILE URL}    ${BROWSER}
    Title Should Be    LogTextFile

Input LogTextFile
    [Arguments]    ${res}
    Input Text    res    ${res}

Input Create LogTextFile
    [Arguments]    ${name}    ${content}    ${parent}
    Input Text    name    ${name}
    Input Text    content    ${content}
    Input Text    parent    ${parent}

Input Move LogTextFile
    [Arguments]    ${path}    ${new_parent}
    Input Text    path    ${path}
    Input Text    new_parent    ${new_parent}

Input Read LogTextFile
    [Arguments]    ${path}
    Input Text    path    ${path}

Append Page Should Be Open
    Title Should Be    Append

Input Append LogTextFile
    [Arguments]    ${line}    ${path}
    Input Text    line    ${line}
    Input Text    path    ${path}

Input Delete LogTextFile
    [Arguments]    ${path}
    Input Text    path    ${path}

# interaction with bufferfile
Open Browser To BufferFile
    Open Browser    ${BUFFERFILE URL}    ${BROWSER}
    Title Should Be    BufferFile

Input BufferFile
    [Arguments]    ${res}
    Input Text    res    ${res}

Input Create BufferFile
    [Arguments]    ${name}    ${max_size}    ${parent}
    Input Text    name    ${name}
    Input Text    max_size    ${max_size}
    Input Text    parent    ${parent}

Input Move BufferFile
    [Arguments]    ${path}    ${new_parent}
    Input Text    path    ${path}
    Input Text    new_parent    ${new_parent}

Push Page Should Be Open
    Title Should Be    Push

Input Push BufferFile
    [Arguments]    ${element}    ${path}
    Input Text    element    ${element}
    Input Text    path    ${path}

Consume Page Should Be Open
    Title Should Be    Consume

Input Consume BufferFile
    [Arguments]    ${path}
    Input Text    path    ${path}

Input Delete BufferFile
    [Arguments]    ${path}
    Input Text    path    ${path}
