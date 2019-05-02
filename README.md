# Gong-Fu-timer
A small gong fu timer written in python for CLI.

Allows you to set the initial infusion time, as well as the interval for subsequent infusions.

You may also set a max number of infusions and the system will let you know when you've had a set number of infusions.

You may simply launch the program, and follow the promts, or use command line arguments.

-t "tea" : This names the tea and will be more important for future functionality.

-ib "initial brew" : Sets the initial brew time.

-bi "brew Interval" : Sets the brew interval to be added to the initial brew time for each subsequent infusion.

-ms[optional] "max steeps" : Sets the max number of steeps. The program will exit out and let you know when you're finished with your session.

Example: drink.py -t "Alishan Cream" -ib 20 -bi 5 -ms 8

If you'd like to store teas for later use use the -nt argument with the name of the tea in quotes or with no spaces.

Example: drink.py -nt "Alishan Cream"

This will prompt you to enter the rest of the parameters.

When you'd like to brew your tea simply enter:

drink.py -t "Alishan Cream"
