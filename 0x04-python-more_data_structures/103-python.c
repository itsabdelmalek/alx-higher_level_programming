#include <Python.h>
#include <stdio.h>

/**
 * print_python_list - Prints basic information about Python lists
 * @p: Pointer to the PyObject list object
 */
void print_python_list(PyObject *p)
{
	Py_ssize_t size, i;
	PyObject *item;

	size = PyList_Size(p);
	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

	for (i = 0; i < size; i++)
	{
		item = PyList_GetItem(p, i);
		printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
	}
}

/**
 * print_python_bytes - Prints basic information about Python bytes objects
 * @p: Pointer to the PyObject bytes object
 */
void print_python_bytes(PyObject *p)
{
	Py_ssize_t size, i;
	char *bytes_str;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	size = PyBytes_Size(p);
	bytes_str = ((PyBytesObject *)p)->ob_sval;

	printf("  size: %ld\n", size);
	printf("  trying string: %s\n", bytes_str);

	printf("  first %ld bytes: ", (size + 1 > 10) ? 10 : size + 1);
	for (i = 0; i < size + 1 && i < 10; i++)
		printf("%02hhx%s", bytes_str[i], (i == 9 || i == size) ? "\n" : " ");
}
