NAME OF PROJECT:
===============
CS4500-002
Project 2: Kernel and Module and Processes

MEMBERS:
=======
Annabel Fuina
Noah Holt

STATEMENT:
==========
We have neither given nor received unauthorized assistance on this work.


VIRTUAL MACHINE (VM) INFORMATION:
================================
NAME OF VIRTUAL MACHINE (VM): afuina-vm1
USERNAME:annabelfuina
PASSWORD:OperatingSystems2024$

Files are located in Desktop > CS4500 > proj2

Each part has its own directory within proj2 containing the appropriate files.

Parts 1, 2, and 3 contain: .c file, Makefile, and outputs.

Part 4 contains the example code from the article to test. 

 
ROOT PASSWORD:
==============
OperatingSystems2024!


PROBLEM DESCRIPTION AND REMEDIATION:
===================================
	
	PART 0: SET UP
	==============
	
	PART 1: Hello World!
	===================
	What was error when running make? (5 pts)
		The function names already exist in the kernel module.
	Fix:
		Added a 2 to the function names in hello.c

	Difference in time stamps: (15 pts)
		hello: 14:15:16 2024
		Goodbye: 14:16:49 2024

	Print to std output: (5 pts)
		To print to the console you would add a printf as well as
		the printk that is already there.


	PART 2: Print Self Kernel Module
	==========================

	ADD ANSWERS TO QUESTIONS 1-3 HERE

	I needed to google how to access the process info, but otherwise was 
	a fairly straight forward fucntion.



	PART 3: Create a print_other Kernel Module
	==========================

	step 1:
		copied over step 2 files since just an extension of that

	step 2:
		adjust so that file names are differnt
	
		Questions:
		1)Which process is current?
			17006 insmod is first stated and so the current one

		2)What is new main process called? What is output?
			New process looks to be systemd (id = 1)

		3)Which states are observed?
			states 0 for insmod and sudo and state 1 for systemd, teminal, and bash


	step 3:
		get input arg was complicated, turns out you need a different
		function to pull it all together.

		to run change one thing:
			insmod print_other.ko my_param=3097

	PART 4: Kernel Modules and System Calls
	==========================
	1. What is the difference between a kernel module and a system call?

	Kernel modules (also known as loadable modules) are pieces of code 
	that can be loaded and unloaded into the kernel on demand in order to 
	extend its functionality without needing to reboot the machine.This
	makes it easier for the programmer since they will not need to rebuild 
	the kernel in every cycle of kernel development -- making it less prone
	to errors. 

	System calls are entry-points to the kernel from user-mode. This can
	happen when a user program needs to request the OS's services, which 
	are accessed only through kernel mode.Since kernel mode has direct
	access to the hardware, it can be dangerous to operate in kernel mode.
	System calls provide a safe way for user programs to operate and interact
	with necessary resources without the risks. Unlike kernel modules, system 
	calls are bound to the kernel implementation. 

 
	2. This article is over 20 years old. If you try this example from the
	article in your VM, does it still work? Use your own words to explain why 
	you think this may be a good (or bad) thing. 
	
	The example did not work when I tried to run it. This is a good thing,
	because modern operating systems are consistently being updated to 
	prevent attacks and vulnerabilities. For this example specifically, 
	being able to intercept system calls by accessing the system call table
	can introduce security risks if not done carefully. If a threat actor
	was able to gain unauthorized access and tamper with the system call
	functionality, this could cause harm to the system and cause it to
	not work properly. 
	













