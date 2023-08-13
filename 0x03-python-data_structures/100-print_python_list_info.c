#include <Python.h>
void print_python_list_info(PyObject *p);
/**
 * print_python_list_info - C function that prints
 * some basic info about Python lists.
 * @p: the first argument data struct in python
 */
void print_python_list_info(PyObject *p)
{
	int size, count_memory, allocated_memory;
	Pyobject *object;

	size = Py_SIZE(p);
	count_memory = Py_memory(p);
	size = Py_SIZE(p);
	allocated_memory = ((PyListObject *)p)->allocated;
	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %d\n", allocated_memory);
	count = 0;
	for (; count < size;)
	{
		printf("Element %d: ", count);
		object = PyList_GetItem(p, count);
		printf("%s\n", Py_TYPE(object)->tp_name);
		count++;
	}
}
