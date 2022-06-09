#include "Python.h"
#include <stdio.h>
/**
 * print_python_list_info -prnts some basic info abouth Python lists
 * @p: a PyObject
 *
 * Return: void
 */
void print_python_list_info(PyObject *p)
{
	Py_ssize_t i = 0;
	Py_ssize_t sz = PyList_GET_SIZE(p);

	printf("[*] Size of Python List = %ld\n", sz);
	printf("[*] Allocated = %ld\n", ((PyListObject *) p)->allocated);

	for (i = 0; i < sz; i++)
		printf("Element %ld: %s\n", i, Py_TYPE(PyList_GET_ITEM(p, i))->tp_name);
}
