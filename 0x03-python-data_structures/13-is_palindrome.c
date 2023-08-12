#include "lists.h"
/**
 * is_palindrome - chek if linked list is a palindrome
 * @head: the head of the linked list
 * Return: 1 if the list palindrome or 0 otherwise
 */
int is_palindrome(listint_t **head)
{
	listint_t *new_head = (*head);
	int *values = NULL;
	int count = 0, middle;

	if (!head || !(*head))
		return (1);
	while (new_head)
	{
		count++;
		new_head = new_head->next;
	}
	values = malloc(sizeof(int) * count);
	if (!values)
		return (0);
	new_head = (*head);
	count = 0;
	while (new_head)
	{
		values[count] = new_head->n;
		new_head = new_head->next;
		count++;
	}
	count--;
	middle = count;
	count = 0;
	while (count < middle)
	{
		if (values[count] != values[middle])
		{
			free(values);
			return (0);
		}
		count++, middle--;
	}
	free(values);
	return (1);
}
