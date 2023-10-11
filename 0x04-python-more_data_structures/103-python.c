#include <Python.h>
#include <stddef.h>
#include <string.h>

/**
 * print_python_bytes - prints infos about a python list
 * @p: a Python bytes object passed from a python script
 */
void print_python_bytes(PyObject *p)
{
	Py_ssize_t bytes_size, n_bytes, i;
	char *try_str;

	write(STDIN_FILENO, "[.] bytes object info\n", 22);
	if (p == NULL || strcmp((p->ob_type)->tp_name, "bytes") != 0)
	{
		write(STDIN_FILENO, "  [ERROR] Invalid Bytes Object\n", 31);
		return;
	}

	bytes_size = ((PyVarObject *)p)->ob_size;
	printf("  size: %lu\n", bytes_size);
	try_str = ((PyBytesObject *)p)->ob_sval;
	printf("  trying string: %s\n", try_str);
	n_bytes = bytes_size > 9 ? 10 : bytes_size + 1;
	printf("  first %lu bytes:", n_bytes);
	for (i = 0; i < n_bytes; i++)
	{
		printf(" %02x", (unsigned char)try_str[i]);
	}
	putchar('\n');
}

/**
 * print_python_list - prints infos about a python list
 * @p: a Python list object passed from a python script
 */
void print_python_list(PyObject *p)
{
	Py_ssize_t idx, list_size, Allocated;
	const char *item_type;

	write(STDIN_FILENO, "[*] Python list info\n", 21);
	if (p && PyList_CheckExact(p))
	{
		list_size = PyList_GET_SIZE(p);
		Allocated = ((PyListObject *)p)->allocated;
		printf("[*] Size of the Python List = %lu\n[*] Allocated = %lu\n",
											list_size, Allocated);

		for (idx = 0; idx < list_size; idx++)
		{
/*			item_type = Py_TYPE(PyList_GetItem(p, idx))->tp_name;*/
			item_type = (PyList_GET_ITEM(p, idx)->ob_type)->tp_name;
			printf("Element %lu: %s\n", idx, item_type);
			if (strcmp(item_type, "bytes") == 0)
				print_python_bytes(p);
		}
	}
}
