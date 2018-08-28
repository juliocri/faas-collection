# Installation

* Install kubeless (https://kubeless.io/docs/quick-start/)
* ``` $ git clone https://github.com/juliocri/faas-collection.git ```

# Usage

* ``` $ cd dbaas-kubeless ```

### General

*  ``` $ make deploy ``` deploys all functions inside `functions` dir.
*  ``` $ make delete ``` deletes all functions inside `functions` dir from k8's.
*  ``` $ make update ``` updates all functions inside `functions` dir.

### Specific function

* ``` $ cd functions/{function-name} ```
* ``` $ make deploy ``` deploys the function in the current dir to k8's.
* ``` $ make delete ``` deletes function with the current dir name from k8's.
* ``` $ make update ``` updates the function in k8's with the content of ```func.go``` and deps in ```Gopkg.toml``` in the current dir.
