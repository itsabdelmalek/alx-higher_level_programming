#include <stdio.h>
#include <stdlib.h>
#include <Python.h>

/**
 * print_python_list - Prints basic information about Python lists
 * @p: PyObject pointer to the Python list object
 */
void print_python_list(PyObject *p)
{
	Py_ssize_t size;
	Py_ssize_t i;

	if (!PyList_Check(p))
	{
		printf("  [ERROR] Invalid Python list\n");
		return;
	}

	size = PyList_Size(p);

	printf("[*] Python list info\n");
	printf("[*] Size of the list: %ld\n", size);
	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

	for (i = 0; i < size; i++)
	{
		PyObject *item = PyList_GetItem(p, i);
		const char *item_type = item->ob_type->tp_name;

		printf("Element %ld: %s\n", i, item_type);
	}
}

/**
 * print_python_bytes - Prints basic information about Python bytes objects
 * @p: PyObject pointer to the Python bytes object
 */
void print_python_bytes(PyObject *p)
{
	Py_ssize_t size;
	Py_ssize_t i;
	char *data;

	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Python bytes object\n");
		return;
	}

	size = ((PyVarObject *)p)->ob_size;

	printf("[.] Bytes object info\n");
	printf("  Size: %ld\n", size);
	printf("  trying string: %s\n", ((PyBytesObject *)p)->ob_sval);

	if (size > 10)
		size = 10;

	data = ((PyBytesObject *)p)->ob_sval;

	printf("  first %ld bytes: ", size);
	for (i = 0; i < size; i++)
	{
		printf("%02x", (unsigned char)data[i]);
		if (i < size - 1)
			printf(" ");
	}
	printf("\n");
}
