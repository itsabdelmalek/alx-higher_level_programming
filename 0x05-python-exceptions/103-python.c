#include <Python.h>
#include <stdio.h>

/**
 * print_python_list - Prints information about Python lists
 * @p: Pointer to the PyObject representing the list
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
 * print_python_bytes - Prints information about Python bytes
 * @p: Pointer to the PyObject representing the bytes object
 */
void print_python_bytes(PyObject *p)
{
	Py_ssize_t size, i;
	char *str;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	size = PyBytes_Size(p);
	str = PyBytes_AsString(p);

	printf("  size: %ld\n", size);
	printf("  trying string: %s\n", str);

	printf("  first %ld bytes: ", (size < 10) ? size + 1 : 10);
	for (i = 0; i <= size && i < 10; i++)
	{
		printf("%02hhx", str[i]);
		if (i == 9 && size >= 10)
			printf("...");
	}
	printf("\n");
}

/**
 * print_python_float - Prints information about Python float objects
 * @p: Pointer to the PyObject representing the float object
 */
void print_python_float(PyObject *p)
{
	PyObject *repr_str;
	char *str;

	printf("[.] float object info\n");
	if (!PyFloat_Check(p))
	{
		printf("  [ERROR] Invalid Float Object\n");
		return;
	}

	repr_str = PyObject_Repr(p);
	str = PyUnicode_AsUTF8(repr_str);

	printf("  value: %s\n", str);
	Py_DECREF(repr_str);
}
