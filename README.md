
# Purpose

  

The project concerns the creation of an REST API for finding items within a tree. Starting from 2 JSON structured at several levels, the API must allow to search in each of them (separately) the last level elements that contain a given string in 2 modes:

  

Search for the leaves on the whole tree

Search for leaves on a specific sublayer (passed in input to the API)

A plus is the realization of automatic tests.

For the implementation we want you to use Python.

The purpose is to see how you approach to solving problems and how to set up a project from scratch (methodologies / tools / maintainability of the code are aspects that we will take much into consideration).

  

Attached are the 2 JSON files:

  

Categories.json: the search must be done for the name field. The children are identified by the children field

Psychographics.json: the research must be done for the label field. The children are identified by the values ​​field

  

We leave you wide freedom regarding implementation

  

# Dev Setup

  

 -  run **make venv** to create the virtualenv
 -  run **source env/bin/activate** to acrivate the virtualenv
 -  run **make install** to install dependencies and packages
 -  run **make tests** to run the tests
 -  run **make start** to start the server
