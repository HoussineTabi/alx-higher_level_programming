#include "lists.h"

/**
 * check_cycle - checks if there is a cycle
 * @list: the list to check
 *
 * Return: 0 if there is no cycle and 1 if there is one
 */
int check_cycle(listint_t *list)
{
	listint_t *previouse = list;

	while (list)
	{
		list = list->next;
		if (list > previouse)
			return (1);
		previouse = list;
	}
	return (0);
}
