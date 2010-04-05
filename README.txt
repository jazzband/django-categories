This app attempts to provide a generic category system that multiple apps could use. It uses MPTT for the tree storage and provides a custom admin for better visualization (copied and modified from feinCMS).

Goals of the project

* Have a generic method for handling hierarchical data

* Allow multiple independent trees, or just one tree

* Have a widget for use in forms

* In templates:

	+ Show one level of a tree 
		- All root categories
		- Just children of a specified category

	+ Show multiple levels
		- Ancestors of category, category and all children of category
		- Category and its children

	+ An inclusion tag for common methods of formatting categories
		- Grandparent :: Parent :: Child <-- current node
			- Add relative links for ancestors
		- Unordered list:
			* Grandparent
			    * Parent <-- current node
			        * Child 1
			        * Child 2
			        * Child n
