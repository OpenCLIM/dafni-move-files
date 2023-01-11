# dafni-move-files
A tool for moving files around on DAFNI

## Description
This tool was designed to sit between two models. Taking the outputs from one, it sorts specificed files into folders as directed by the user to fit into the directory system of a subsequent model. 

## Input Variables
* Folder Names
  * Description: The destination folder path, this should be the same as the target dataslot. This model is limited to one folder.
* File Paths
  * Description: The name and type of the files to be moved. The code will search for the file within the /data/inputs directory and place it in the specified folder. Multiple files going into the same folder can be added  - they must be seperated by a comma with no spaces. 
