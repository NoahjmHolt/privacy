
#include <linux/module.h>
#include <linux/kernel.h>
#include <linux/init_task.h>
#include <linux/sched.h>

int __init print_self_init(void){

	struct task_struct *task = current;

	printk(KERN_INFO "Process Name: %s, id: %d, State: %ld\n", task->comm, task->pid, task->state);

	while (task->pid != 1) { // 1 is given to init

		task = task->parent;
		printk(KERN_INFO "Parent Process: %s, id: %d, State: %ld\n", task->comm, task->pid, task->state);

	}

	return 0;

}


void __exit print_self_exit(void){

	printk(KERN_INFO "Exiting Print Self\n");
}


module_init(print_self_init);
module_exit(print_self_exit);


