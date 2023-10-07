/* useful files: object.h, listobject.h, pytypedefs.h, cpython/object.h */
/* they exist in Python include directory  /usr/include/python<version> */
#include <Python.h>

/**
 * print_python_list_info - with the help of Cpython
 * @p: the list object you want to print info about
 */
void print_python_list_info(PyObject *p)
{
	Py_ssize_t idx, list_size, Allocated;
	const char *item_type;

	if (p && PyList_CheckExact(p))
	{
		list_size = PyList_GET_SIZE(p);
		Allocated = ((PyListObject *)p)->allocated;
		printf("[*] Size of the Python List = %lu\n[*] Allocated = %lu\n",
											list_size, Allocated);

		for (idx = 0; idx < list_size; idx++)
		{
			item_type = Py_TYPE(PyList_GetItem(p, idx))->tp_name;
			printf("Element %lu: %s\n", idx, item_type);
		}
	}
}
