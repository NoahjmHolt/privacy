
#include <linux/module.h>
#include <linux/kernel.h>
#include <linux/init_task.h>
#include <linux/sched.h>


static int my_param = 0;

module_param(my_param, int, S_IRUSR | S_IWUSR | S_IRGRP | S_IROTH);


int __init print_other_init(void){

	struct task_struct *task = current;

	while (task->pid != 1) { // 1 is given to init

		if (my_param == task->pid) {
			printk(KERN_INFO "Parent Process: %s, id: %d, State: %ld\n", task->comm, task->pid, task->state);
		}

		task = task->parent;		

	}

	return 0;

}


void __exit print_other_exit(void){

	printk(KERN_INFO "Exiting Print Other\n");
}


module_init(print_other_init);
module_exit(print_other_exit);


