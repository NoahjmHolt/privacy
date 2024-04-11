
obj-m += hello.o

all:
	make modules -C /lib/modules/$(shell uname -r)/build M=$(shell pwd)

clean:
	make -C /lib/modules/$(shell uname -r)/build M=$(shell pwd) clean

