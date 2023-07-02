#include <Python.h>
#include <stdio.h>

/**
 * print_python_string - Prints information about a Python string object
 * @p: Pointer to the Python string object
 */
void print_python_string(PyObject *p)
{
	Py_ssize_t length;
	Py_UNICODE *buffer;

	if (!PyUnicode_Check(p))
	{
		fprintf(stderr, "Invalid Python string object\n");
		return;
	}

	length = PyUnicode_GET_LENGTH(p);
	buffer = PyUnicode_AsUnicode(p);

	printf("[.] %ls\n", buffer);
	printf("  Length: %ld\n", length);
}

