#include <Python.h>
#include <stddef.h>
#include <string.h>
#include <stdio.h>
#include <math.h>

void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);
void print_python_float(PyObject *p);
/**
 * print_python_list - prints infos about a python list
 * @p: a Python list object passed from a python script
 */
void print_python_list(PyObject *p)
{
	Py_ssize_t idx, list_size, Allocated;
	const char *item_type;
	PyObject *item;

	fflush(stdout);
	printf("[*] Python list info\n");
	if (p == NULL || PyList_CheckExact(p) == 0)
	{
		printf("  [ERROR] Invalid List Object\n");
		return;
	}

	list_size = PyList_GET_SIZE(p);
	Allocated = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %lu\n", list_size);
	printf("[*] Allocated = %lu\n", Allocated);

	for (idx = 0; idx < list_size; idx++)
	{
		item = PyList_GET_ITEM(p, idx);
		item_type = item->ob_type->tp_name;
		printf("Element %lu: %s\n", idx, item_type);

		if (strcmp(item_type, "bytes") == 0)
			print_python_bytes(PyList_GET_ITEM(p, idx));
		else if (strcmp(item_type, "float") == 0)
			print_python_float(PyList_GET_ITEM(p, idx));
	}
	fflush(stdout);
}

/**
 * print_python_bytes - prints infos about a python list
 * @p: a Python bytes object passed from a python script
 */
void print_python_bytes(PyObject *p)
{
	Py_ssize_t bytes_size, n_bytes, i;
	char *try_str;

	fflush(stdout);
	printf("[.] bytes object info\n");
	if (p == NULL || strcmp((p->ob_type)->tp_name, "bytes") != 0)
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	bytes_size = ((PyVarObject *)p)->ob_size;
	try_str = ((PyBytesObject *)p)->ob_sval;
	n_bytes = bytes_size > 9 ? 10 : bytes_size + 1;

	printf("  size: %lu\n", bytes_size);
	printf("  trying string: %s\n", try_str);
	printf("  first %lu bytes:", n_bytes);

	for (i = 0; i < n_bytes; i++)
		printf(" %02x", (unsigned char)try_str[i]);
	fflush(stdout);
	putchar('\n');
}

/**
 * print_python_float - prints infos about a python list
 * @p: a Python bytes object passed from a python script
 */
void print_python_float(PyObject *p)
{
	double val;
	char *repr;

	fflush(stdout);
	printf("[.] float object info\n");
	if (p == NULL || strcmp((p->ob_type)->tp_name, "float") != 0)
	{
		printf("  [ERROR] Invalid Float Object\n");
		return;
	}

	val = ((PyFloatObject *)p)->ob_fval;
	repr = PyOS_double_to_string(val, 'r', 0, 2, NULL);
	/* go to file pystrtod.h and .c */

	printf("  value: %s\n", repr);
	fflush(stdout);
}
