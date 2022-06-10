#include "Python.h"

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
		printf(" [ERROR] Invalid Bytes Object\n");
		return;
	}

	sz = PyBytes_Size(p);
	printf(" size: %ld\n", sz);
	printf(" trying string: %s\n", PyBytes_AsString(p));

	sz = sz > 10 ? 10 : sz + 1;
	p = PyBytes_FromStringAndSize(PyBytes_AsString(p), sz);
	s = PyBytes_AsString(p);
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
	Py_ssize_t len = PyList_GET_SIZE(p);
	Py_ssize_t i = 0;
	PyObject *tmp;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", len);
	printf("[*] Allocated = %ld\n", ((PyListObject *) p)->allocated);
	for (i = 0; i < len; i++)
	{
		tmp = PyList_GET_ITEM(p, i);
		printf("Element %ld: %s\n", i, tmp->ob_type->tp_name);
		if (PyBytes_Check(tmp))
			print_python_bytes(tmp);
	}
}
