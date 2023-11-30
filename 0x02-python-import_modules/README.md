#	@Author Gitau Muguro
This directory deals with modules in python.
Modules are files containing Python definations (functions & variables) and statements. 
a module can contain executable staements as well as function definations. Each module has 
its wown private namespace, which is used as the global namespace by all functions defined in the module.
modules can import other modules. it is customary but not required to place all import statements at the 
begining of a module. the imported module names, if placed at the top level of a module (outside ay functions or classes) 
are added to the module's global namespace.

If you know what you are doing you can touch a module's global variable with the same notation used to refer to its functions.
	modname.itemname

also possible to import specific fucntion form a given module as follows
	from modname import fucntname 
		i.e from calculator import addition

Python comes with a library of standard modules, described in a separate document, the Python Library Reference 
