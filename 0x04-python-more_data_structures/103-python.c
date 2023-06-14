#include <Python.h>
#include <stdio.h>

/**
 * print_python_bytes - Prints bytes informations
 *
 * @p: Python Object
 * Return: void
 */
void print_python_bytes(PyObject *p)
{
	char *str;
	long int size, i, lim;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	size = ((PyVarObject *)(p))->ob_size;
	str = ((PyBytesObject *)p)->ob_sval;

	printf("  size: %ld\n", size);
	printf("  trying string: %s\n", str);

	if (size >= 10)
		lim = 10;
	else
		lim = size + 1;

	printf("  first %ld bytes:", lim);

	for (i = 0; i < lim; i++)
		if (str[i] >= 0)
			printf(" %02x", str[i]);
		else
			printf(" %02x", 256 + str[i]);

	printf("\n");
}

/**
 * print_python_list - Prints list informations
 *
 * @p: Python Object
 * Return: void
 */
void print_python_list(PyObject *p)
{
	long int size, a;
	PyListObject *list;
	PyObject *obj;

	size = ((PyVarObject *)(p))->ob_size;
	list = (PyListObject *)p;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", list->allocated);

	for (a = 0; a < size; a++)
	{
		obj = ((PyListObject *)p)->ob_item[a];
		printf("Element %ld: %s\n", a, ((obj)->ob_type)->tp_name);
		if (PyBytes_Check(obj))
			print_python_bytes(obj);
	}
}
