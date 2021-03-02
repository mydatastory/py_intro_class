## Py4AI

The episodes in this course are derived from work that is Copyrighted © by Software Carpentry.  Additional information can be
found at: http://software-carpentry.org/.  The Creative Commons license which governs this work is located at:
https://creativecommons.org/licenses/by/4.0/. The original Software Carpentry episodes have been modified and/or extended to meet the specific learning goals of this class.  

## Original Software Carpentry Course
[python-novice-gapminder](https://github.com/swcarpentry/python-novice-gapminder)

## Running the Nvidia Worksheets on HiperGator

Within the OnDemand application, click on the Interactive Apps dropdown and select Jupyter Notebook in the Servers section.  Then fill out the Jupyter Notebook slurm submission form as follows:  select <kbd>hwgui</kbd> or <kbd>gpu</kbd> from the dropdown menu for the *Cluster partition* field.  In the *Generic Resource Request* field, enter `gpu:geforce:1`.  You will also want to ask for `18` GB of memory in the Maximum Memory field for all worksheets used in this mini-course.

## Notes
- The Jupyter notebooks are rendered using [nbviewer](https://nbviewer.jupyter.org/).
- Matt Gitzendanner's Python class materials can be found [here](https://github.com/CompTools/Class_Files).
- Mindy McAdams' Python class materials can be found [here](https://github.com/macloo/python-beginners).
