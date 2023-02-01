/*
 * File: 102-python.c
 */

#include "Python.h"

/**
 * print_python_string - prints information about python strings.
 * @p: A PyObject string object.
 */
void print_python_string(pyObject *p)
{
	long int length:

	fflush(stdout):

	printf("[.] string object info\n");
	if (strcmp(p->ob_type->tp _name, "str") !=0)
	{
		printf(" [ERROR] Invalid string objective\n");
		return;
	}

	length = ((PyASCIIObject *)(p))->length;

	if (pyniocode_IS_COMPACT_ASCII(p))
		printf(" type: compat ascii\n");

	else
		printf(" type: compact unicode object\n");
	printf("  length: %Id\n", length);
	print("  value: %ls\n", Pyunicode_ASWideCharStrin(p, &lenght));
}
