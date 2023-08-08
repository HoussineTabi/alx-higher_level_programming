#include "lists.h"
/**
 * insert_node - is a function inserts a node in order
 * @head: first parameter the adress of the head
 * @number: the data to inset in the list
 * Return: the address of the nude or null
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node = NULL, *previouse = NULL, *newhead = *head;

	if (head == NULL)
		return (NULL);
	node = malloc(sizeof(listint_t));
	if (!node)
		return (NULL);
	node->next = NULL, node->n = number;
	if (!(*head))
	{
		(*head) = node;
		return (node);
	}
	while (newhead)
	{
		if (newhead->n < number)
		{
			previouse = newhead;
			newhead = newhead->next;
			continue;
		}
		node->next = newhead;
		previouse->next = node;
		return (node);
	}
	free(node);
	return (NULL);
}
