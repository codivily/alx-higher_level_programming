#include "Python.h"
#include <ctype.h>

PyAPI_FUNC(void) print_python_bytes(PyObject * p);
PyAPI_FUNC(void) print_python_list(PyObject * p);

/**
 * print_python_bytes - print some basic info about Python lists
 * @p: A PyObject
 *
 * Return: void
 */
void print_python_bytes(PyObject *p)
{
	Py_ssize_t i, sz;
	char *s;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		perror("  [ERROR] Invalid Bytes Object\n");
		return;
	}
	sz = PyBytes_Size(p);
	s = PyBytes_AsString(p);
	printf("  size: %ld\n", sz);
	printf("  trying string: ");
	for (i = 0; i < sz; i++)
	{
		printf("%c", *s);
		if (!isprint(*s++))
			break;
	}
	printf("\n");
	sz = sz > 10 ? 10 : sz;
	printf("first %ld bytes:", sz);
	for (i = 0; i < sz; i++)
		printf(" %02x", (unsigned char)*s++);
	printf("\n");
}

/**
 * print_python_list - print python list
 * @p: A PyObject
 *
 * Return: void
 */
void print_python_list(PyObject *p)
{
	Py_ssize_t len;
	Py_ssize_t i = 0;
	PyObject *tmp;

	if (!p)
		return;
	len = PyList_Size(p);

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", len);
	printf("[*] Allocated = %ld\n", ((PyListObject *) p)->allocated);
	for (i = 0; i < len; i++)
	{
		tmp = ((PyListObject *)p)->ob_item[i];
		printf("Element %ld: %s\n", i, tmp->ob_type->tp_name);
		if (PyBytes_Check(tmp))
			print_python_bytes(tmp);
	}
}
