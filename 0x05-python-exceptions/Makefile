CC=gcc
CFLAGS=-Wall -Werror -Wextra -pedantic -std=c99
libdir=/home/yah/.venv/rel/src/Python-3.4.10/Include

libPython: 103-python.c
	$(CC) 103-python.c $(CFLAGS) -shared -fPIC -I$(libdir) -Wl,-soname,libPython.so  -o libPython.so

clean:
	rm -rf *.o *.out *.so
